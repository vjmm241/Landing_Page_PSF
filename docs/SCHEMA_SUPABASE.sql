-- SCHEMA PARA PROSMART FACTORIES (SUPABASE / POSTGRESQL)

-- Habilitar extensión pgvector si no existe
CREATE EXTENSION IF NOT EXISTS vector;

-- 1. Tabla de Perfiles (Extiende Auth Users)
CREATE TABLE IF NOT EXISTS profiles (
    id UUID REFERENCES auth.users ON DELETE CASCADE PRIMARY KEY,
    name TEXT NOT NULL,
    company TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Tabla de Documentos (Un solo PDF por usuario según Instrucciones_Demo.md)
CREATE TABLE IF NOT EXISTS documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
    file_path TEXT NOT NULL,
    file_name TEXT NOT NULL,
    processed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_user_document UNIQUE (user_id)
);

-- 3. Tabla de Chunks de Documentos (Búsqueda Vectorial)
CREATE TABLE IF NOT EXISTS document_chunks (
    id BIGSERIAL PRIMARY KEY,
    user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
    document_id UUID REFERENCES documents ON DELETE CASCADE NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536), -- Dimensiones para OpenAI text-embedding-3-small
    page_number INTEGER,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Tabla de Imágenes de Documentos
CREATE TABLE IF NOT EXISTS document_images (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES auth.users ON DELETE CASCADE NOT NULL,
    document_id UUID REFERENCES documents ON DELETE CASCADE NOT NULL,
    image_url TEXT NOT NULL,
    page_number INTEGER,
    context TEXT, -- Contexto textual cercano para búsqueda semántica
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Índices para Búsqueda Vectorial (HNSW para mayor robustez en Free Tier)
CREATE INDEX IF NOT EXISTS document_chunks_embedding_idx ON document_chunks 
USING hnsw (embedding vector_cosine_ops);

-- 6. Políticas de Seguridad (RLS)
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE document_chunks ENABLE ROW LEVEL SECURITY;
ALTER TABLE document_images ENABLE ROW LEVEL SECURITY;

-- Profiles: usuario puede leer/escribir solo su perfil
DROP POLICY IF EXISTS "Users can view own profile" ON profiles;
DROP POLICY IF EXISTS "Users can update own profile" ON profiles;
DROP POLICY IF EXISTS "Users can insert own profile" ON profiles;
CREATE POLICY "Users can view own profile" ON profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own profile" ON profiles FOR UPDATE USING (auth.uid() = id);
CREATE POLICY "Users can insert own profile" ON profiles FOR INSERT WITH CHECK (auth.uid() = id);

-- Documents: usuario puede leer/escribir solo sus documentos
DROP POLICY IF EXISTS "Users can view own documents" ON documents;
DROP POLICY IF EXISTS "Users can manage own documents" ON documents;
CREATE POLICY "Users can view own documents" ON documents FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can manage own documents" ON documents FOR ALL USING (auth.uid() = user_id);

-- Chunks & Images: usuario puede leer solo lo suyo
DROP POLICY IF EXISTS "Users can view own chunks" ON document_chunks;
DROP POLICY IF EXISTS "Users can view own images" ON document_images;
CREATE POLICY "Users can view own chunks" ON document_chunks FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can view own images" ON document_images FOR SELECT USING (auth.uid() = user_id);

-- 7. Función RPC para Búsqueda Vectorial
CREATE OR REPLACE FUNCTION match_document_chunks (
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
