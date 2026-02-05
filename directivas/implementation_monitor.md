# Implementation Monitor

> **ID:** IMP-2026-01-31
> **Status:** IN PROGRESS
> **Goal:** Rigorous adherence to `Instrucciones_Demo.md`.

## Checklist

### 1. Database & Schema
- [ ] `profiles` table exists (UUID PK, Name, Company)
- [ ] RLS enabled on `profiles` (Users can only see own profile)
- [ ] `documents` table (One PDF per user constraint via logic/policy)
- [ ] `document_chunks` (Vector store)
- [ ] `document_images` (For multimodal chat)

### 2. Edge Functions
- [ ] `process_pdf`:
    - [ ] Extracts text
    - [ ] Extracts images
    - [ ] Stores images in `document_images` bucket
    - [ ] Inserts DB records (`document_images` table)
- [ ] `chat`:
    - [ ] Vector search on text
    - [ ] Context retrieval includes image references
    - [ ] Response format = JSON { steps: [], images: [] }

### 3. Frontend (Auth)
- [ ] Login (Email/Pass)
- [ ] Forgot Password Link -> Redirect to Reset Page
- [ ] Reset Page -> Update Password -> **AUTO LOGOUT**
- [ ] Redirect to Login -> Login -> OTP -> Verify

### 4. Frontend (Chat)
- [ ] Renders Markdown
- [ ] Renders Images from JSON response

## Anomalies & Fixes
| Time | Issue | Fix |
|---|---|---|
| | | |
