-- FIX: Grant permissions and refine RLS for documents table
-- Ensures authenticated users can INSERT files correctly

-- 1. Grant low-level table permissions (often the cause of 'permission denied' even if RLS is on)
GRANT ALL ON TABLE public.documents TO postgres;
GRANT ALL ON TABLE public.documents TO authenticated;
GRANT ALL ON TABLE public.documents TO service_role;

-- 2. Refine Policies (Split them for clarity and ensuring INSERT works)
DROP POLICY IF EXISTS "Users can manage own documents" ON public.documents;
DROP POLICY IF EXISTS "Users can view own documents" ON public.documents;
DROP POLICY IF EXISTS "Users can insert own documents" ON public.documents;
DROP POLICY IF EXISTS "Users can update own documents" ON public.documents;
DROP POLICY IF EXISTS "Users can delete own documents" ON public.documents;

-- Policy for SELECT
CREATE POLICY "Users can view own documents" 
ON public.documents FOR SELECT 
USING (auth.uid() = user_id);

-- Policy for INSERT (Critical for Upload)
CREATE POLICY "Users can insert own documents" 
ON public.documents FOR INSERT 
WITH CHECK (auth.uid() = user_id);

-- Policy for UPDATE
CREATE POLICY "Users can update own documents" 
ON public.documents FOR UPDATE 
USING (auth.uid() = user_id);

-- Policy for DELETE
CREATE POLICY "Users can delete own documents" 
ON public.documents FOR DELETE 
USING (auth.uid() = user_id);
