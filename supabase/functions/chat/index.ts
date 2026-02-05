import { serve } from "https://deno.land/std@0.177.0/http/server.ts"
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.39.7'

const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

serve(async (req) => {
    if (req.method === 'OPTIONS') {
        return new Response('ok', { headers: corsHeaders })
    }

    try {
        const supabaseUrl = Deno.env.get('SUPABASE_URL') ?? '';
        const supabaseKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? '';
        const openaiKey = Deno.env.get('OPENAI_API_KEY') ?? '';

        const supabaseClient = createClient(supabaseUrl, supabaseKey);
        const body = await req.json();

        // --- BRANCH A: PROCESS PDF CHUNKS ---
        if (body.action === 'process') {
            const { document_id: documentId, userId, chunks: clientChunks } = body;
            if (!clientChunks || !clientChunks.length) throw new Error('No chunks provided');

            console.log(`Processing ${clientChunks.length} chunks for ${documentId}`);

            // Clear old
            await supabaseClient.from('document_chunks').delete().eq('user_id', userId);

            // Generate Embeddings
            const embeddingRes = await fetch('https://api.openai.com/v1/embeddings', {
                method: 'POST',
                headers: { 'Authorization': `Bearer ${openaiKey}`, 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    input: clientChunks.slice(0, 50).map((c: any) => c.content.substring(0, 8000)),
                    model: 'text-embedding-3-small'
                })
            });

            if (!embeddingRes.ok) throw new Error(await embeddingRes.text());
            const embeddingData = await embeddingRes.json();

            // Insert
            const inserts = clientChunks.slice(0, 50).map((chunk: any, index: number) => ({
                user_id: userId,
                document_id: documentId,
                content: chunk.content,
                page_number: chunk.page_number,
                embedding: embeddingData.data[index].embedding
            }));

            const { error: insertError } = await supabaseClient.from('document_chunks').insert(inserts);
            if (insertError) throw insertError;

            await supabaseClient.from('documents').update({ processed: true }).eq('id', documentId);
            return new Response(JSON.stringify({ success: true }), { headers: { ...corsHeaders, 'Content-Type': 'application/json' } });
        }

        // --- BRANCH B: CHAT ---
        const { message, userId, image } = body;

        // 1. Generate Embedding for Question
        const embeddingRes = await fetch('https://api.openai.com/v1/embeddings', {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${openaiKey}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({ input: message, model: 'text-embedding-3-small' })
        })
        const embeddingData = await embeddingRes.json()
        if (!embeddingData.data) throw new Error("OpenAI Embedding Failed");
        const queryEmbedding = embeddingData.data[0].embedding

        // 2. Search
        const { data: chunks, error: searchError } = await supabaseClient.rpc('match_document_chunks', {
            query_embedding: queryEmbedding,
            match_threshold: 0.3,
            match_count: 10,
            p_user_id: userId
        })
        if (searchError) throw searchError

        const context = chunks.map((c: any) => `[Página ${c.page_number}]: ${c.content}`).join('\n\n')

        // 3. Images (Retrieved from DB)
        const relevantPages = Array.from(new Set(chunks.map((c: any) => c.page_number)))
        const { data: images } = await supabaseClient
            .from('document_images')
            .select('*')
            .in('page_number', relevantPages)
            .eq('user_id', userId)
            .limit(3)

        // Prepare messages for OpenAI
        const systemMessage = { role: 'system', content: `Eres un ASISTENTE TÉCNICO SENIOR. Responde solo con el CONTEXTO.\nCONTEXTO:\n${context}` };

        const userContent: any[] = [{ type: 'text', text: message }];

        // Add user provided image if exists
        if (image) {
            userContent.push({
                type: 'image_url',
                image_url: {
                    url: image, // Supports URL or base64 data:image/...
                }
            });
        }

        // Add context images if they exist (This logic simulates "seeing" the retrieved documents)
        // Note: For now, we just pass the context text. 
        // If we wanted to pass retrieved images to vision, we would add them here too.

        const messages = [
            systemMessage,
            { role: 'user', content: userContent }
        ];

        // 4. OpenAI
        const chatRes = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${openaiKey}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({
                model: 'gpt-4o',
                messages: messages,
                max_tokens: 1000,
                temperature: 0
            })
        })

        const chatData = await chatRes.json()

        if (chatData.error) {
            throw new Error("OpenAI Chat Error: " + chatData.error.message);
        }

        const responseText = chatData.choices[0].message.content

        return new Response(JSON.stringify({
            response: responseText,
            images: images?.map((img: any) => ({
                url: img.image_url,
                description: img.context || 'Figura relevante'
            })) || []
        }), {
            headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        })

    } catch (error: any) {
        console.error("Function Error:", error);
        return new Response(JSON.stringify({ error: error.message }), {
            headers: { ...corsHeaders, 'Content-Type': 'application/json' },
            status: 200, // Return 200 so frontend can parse JSON error
        })
    }
})
