import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'
import pdfParse from 'npm:pdf-parse'
import { TextractClient, AnalyzeDocumentCommand } from "npm:@aws-sdk/client-textract"

const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

serve(async (req) => {
    // 1. Handle CORS Preflight
    if (req.method === 'OPTIONS') {
        return new Response('ok', { headers: corsHeaders })
    }

    try {
        // 2. Validate Content-Type
        // Some clients might not send multipart/form-data correctly? 
        // But let's assume req.formData() handles it.

        const formData = await req.formData().catch((err: any) => {
            throw new Error(`Error parsing FormData: ${err.message}`);
        });

        const file = formData.get('pdf') as File
        const userId = formData.get('userId') as string

        if (!file || !file.type.includes('pdf')) {
            return new Response(
                JSON.stringify({ error: 'Archivo PDF requerido. Formato recibido: ' + (file?.type || 'null') }),
                { status: 400, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
            )
        }

        console.log('📄 Procesando para:', userId, 'Archivo:', file.name)
        const arrayBuffer = await file.arrayBuffer()
        const uint8Array = new Uint8Array(arrayBuffer)

        // 3. EXTRACCIÓN INTELIGENTE
        // Wrap logic in internal checks
        let text = await smartExtraction(uint8Array)

        if (!text || text.trim().length === 0) {
            throw new Error('No se pudo extraer texto legible del PDF (vacío o protegido).');
        }

        console.log('✅ Texto extraído:', text.length, 'caracteres')

        // 4. CHUNKING & EMBEDDING
        const chunks = splitIntoChunks(text, 1000)
        console.log('📦 Chunks:', chunks.length)

        const embeddingsWithText = await generateEmbeddings(chunks)

        // 5. SUPABASE OPS
        const supabase = createClient(
            Deno.env.get('SUPABASE_URL') ?? '',
            Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
        )

        // Upsert Document
        const { data: docData, error: insertDocError } = await supabase
            .from('documents')
            .upsert({
                user_id: userId,
                file_name: file.name,
                file_path: `${userId}/${Date.now()}_${file.name}`,
                processed: true,
                created_at: new Date()
            }, { onConflict: 'user_id' }) // Ideally per file, but sticking to existing logic
            .select()
            .single()

        if (insertDocError) throw new Error(`DB Error (Doc): ${insertDocError.message}`)

        const documentId = docData.id

        // Insert Chunks
        const { error: insertError } = await supabase
            .from('document_chunks')
            .insert(embeddingsWithText.map((item, idx) => ({
                document_id: documentId,
                content: item.text,
                embedding: item.embedding,
                chunk_index: idx,
                metadata: {
                    filename: file.name
                }
            })))

        if (insertError) throw new Error(`DB Error (Chunks): ${insertError.message}`)

        // 6. SUCCESS RESPONSE
        return new Response(
            JSON.stringify({
                success: true,
                documentId,
                chunks: embeddingsWithText.length,
                filename: file.name,
                message: 'PDF procesado correctamente'
            }),
            {
                status: 200,
                headers: { ...corsHeaders, 'Content-Type': 'application/json' }
            }
        )

    } catch (error) {
        console.error('❌ SYSTEM ERROR:', error)

        // CRITICAL: Always return JSON, never plain text or HTML
        const safeError = error instanceof Error ? error.message : String(error);

        return new Response(
            JSON.stringify({
                error: safeError,
                details: "Consulte los logs del servidor para más detalles."
            }),
            {
                status: 500,
                headers: { ...corsHeaders, 'Content-Type': 'application/json' }
            }
        )
    }
})

// EXTRACCIÓN INTELIGENTE
async function smartExtraction(pdfBuffer: Uint8Array): Promise<string> {
    try {
        // 1. Primero intenta extracción simple
        const simpleResult = await pdfParse(pdfBuffer)

        // 2. Si tiene suficiente texto (>500 chars), úsalo
        if (simpleResult.text.length > 500) {
            console.log('✅ Extracción simple exitosa')
            return simpleResult.text
        }

        // 3. Si es muy corto, probablemente tiene imágenes → usa Textract
        console.log('⚠️ Texto insuficiente, usando AWS Textract...')
        return await extractWithTextract(pdfBuffer)

    } catch (error) {
        console.log('⚠️ Error en extracción simple, fallback a Textract')
        return await extractWithTextract(pdfBuffer)
    }
}

// AWS TEXTRACT
async function extractWithTextract(pdfBuffer: Uint8Array): Promise<string> {
    if (!Deno.env.get('AWS_ACCESS_KEY_ID')) {
        throw new Error("AWS Credentials MISSING. Please set AWS_ACCESS_KEY_ID in Supabase Secrets.");
    }

    const client = new TextractClient({
        region: Deno.env.get('AWS_REGION') || 'us-east-1',
        credentials: {
            accessKeyId: Deno.env.get('AWS_ACCESS_KEY_ID')!,
            secretAccessKey: Deno.env.get('AWS_SECRET_ACCESS_KEY')!
        }
    })

    // Start Sync Job (AnalyzeDocument)
    const command = new AnalyzeDocumentCommand({
        Document: { Bytes: pdfBuffer },
        FeatureTypes: ["TABLES", "FORMS"]
    })

    const response = await client.send(command)

    let fullText = ""
    for (const block of response.Blocks || []) {
        if (block.BlockType === "LINE") {
            fullText += block.Text + "\n"
        }
    }

    return fullText
}

function splitIntoChunks(text: string, chunkSize: number): string[] {
    const chunks: string[] = []
    const overlap = 200

    for (let i = 0; i < text.length; i += (chunkSize - overlap)) {
        const chunk = text.substring(i, i + chunkSize).trim()
        if (chunk.length > 0) chunks.push(chunk)
    }

    return chunks
}

async function generateEmbeddings(chunks: string[]) {
    const OPENAI_KEY = Deno.env.get('OPENAI_API_KEY')
    const results = []

    for (const chunk of chunks) {
        const response = await fetch('https://api.openai.com/v1/embeddings', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${OPENAI_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'text-embedding-ada-002',
                input: chunk
            })
        })

        const data = await response.json()
        if (data.error) throw new Error("OpenAI: " + data.error.message);
        results.push({
            text: chunk,
            embedding: data.data[0].embedding
        })
    }

    return results
}
