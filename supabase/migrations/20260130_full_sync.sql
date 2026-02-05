-- SCHEMA PARA PROSMART FACTORIES (FULL SYNC 2026-01-30)

-- Habilitar extensión pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- 1. Tabla de Perfiles (Extiende Auth Users)
-- Obligatoria para el registro de Nombre y Empresa
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
    name TEXT NOT NULL,
    company TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Tabla de Documentos
CREATE TABLE IF NOT EXISTS public.documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
    file_path TEXT NOT NULL,
    file_name TEXT NOT NULL,
    processed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_user_document UNIQUE (user_id)
);

-- 3. Tabla de Chunks de Documentos (Búsqueda Vectorial)
CREATE TABLE IF NOT EXISTS public.document_chunks (
    id BIGSERIAL PRIMARY KEY,
    user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
    document_id UUID REFERENCES documents ON DELETE CASCADE NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536), -- OpenAI text-embedding-3-small
    page_number INTEGER,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Tabla de Imágenes de Documentos (Para el flujo de Figuras en Chat)
CREATE TABLE IF NOT EXISTS public.document_images (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
    document_id UUID REFERENCES documents ON DELETE CASCADE NOT NULL,
    image_url TEXT NOT NULL,
    page_number INTEGER,
    context TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Índices HNSW
CREATE INDEX IF NOT EXISTS document_chunks_embedding_idx ON document_chunks 
USING hnsw (embedding vector_cosine_ops);

-- 6. Configuración de RLS
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.document_chunks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.document_images ENABLE ROW LEVEL SECURITY;

-- Políticas de Seguridad
DO $$ BEGIN
    -- Profiles
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'Users can view own profile') THEN
        CREATE POLICY "Users can view own profile" ON profiles FOR SELECT USING (auth.uid() = id);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'Users can update own profile') THEN
        CREATE POLICY "Users can update own profile" ON profiles FOR UPDATE USING (auth.uid() = id);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'Users can insert own profile') THEN
        CREATE POLICY "Users can insert own profile" ON profiles FOR INSERT WITH CHECK (auth.uid() = id);
    END IF;

    -- Documents
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'Users can view own documents') THEN
        CREATE POLICY "Users can view own documents" ON documents FOR SELECT USING (auth.uid() = user_id);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'Users can manage own documents') THEN
        CREATE POLICY "Users can manage own documents" ON documents FOR ALL USING (auth.uid() = user_id);
    END IF;

    -- Chunks & Images
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'Users can view own chunks') THEN
        CREATE POLICY "Users can view own chunks" ON document_chunks FOR SELECT USING (auth.uid() = user_id);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_policies WHERE policyname = 'Users can view own images') THEN
        CREATE POLICY "Users can view own images" ON document_images FOR SELECT USING (auth.uid() = user_id);
    END IF;
END $$;

-- 7. Función RPC match_document_chunks
CREATE OR REPLACE FUNCTION public.match_document_chunks (
  query_embedding vector(1536),
  match_threshold float,
  match_count int,
  p_user_id uuid
)
RETURNS TABLE (
  id bigint,
  content text,
  page_number int,
  similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    dc.id,
    dc.content,
    dc.page_number,
    1 - (dc.embedding <=> query_embedding) AS similarity
  FROM document_chunks dc
  WHERE dc.user_id = p_user_id
    AND 1 - (dc.embedding <=> query_embedding) > match_threshold
  ORDER BY dc.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;
