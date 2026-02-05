import os
import re

def verify_implementation():
    print("Starting verification of PDF Limit Increase implementation...")

    # 1. Check process_pdf/index.ts
    process_pdf_path = "supabase/functions/process_pdf/index.ts"
    if not os.path.exists(process_pdf_path):
        print(f"[ERROR] {process_pdf_path} not found.")
        return False
    
    with open(process_pdf_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check limit of 100
    if "chunks.slice(0, 100)" in content:
        print("[OK] Limit of 100 chunks found in process_pdf.")
    else:
        print("[ERROR] Limit of 100 chunks NOT found in process_pdf.")
        return False

    # Check batch embedding logic
    if "input: limitedChunks.map(c => c.content.substring(0, 8000))" in content and ".insert(inserts)" in content:
        print("[OK] Batch embedding and insertion logic found in process_pdf.")
    else:
        print("[ERROR] Batch logic NOT found in process_pdf.")
        return False

    # 2. Check chat/index.ts
    chat_path = "supabase/functions/chat/index.ts"
    if not os.path.exists(chat_path):
        print(f"[WARNING] {chat_path} not found.")
    else:
        with open(chat_path, "r", encoding="utf-8") as f:
            chat_content = f.read()
        
        if "match_count: 10" in chat_content:
            print("[OK] match_count: 10 found in chat function.")
        else:
            print("[ERROR] match_count: 10 NOT found in chat function.")
            return False

    # 3. Check documentation
    doc_path = "docs/CONFIGURACION_SUPABASE_OBLIGATORIA.md"
    if os.path.exists(doc_path):
        with open(doc_path, "r", encoding="utf-8") as f:
            doc_content = f.read()
        if "- **File size limit:** 10MB" in doc_content:
            print("[OK] 10MB limit documentation confirmed.")
        else:
            print("[WARNING] 10MB limit not found in documentation.")
    
    print("\nAll code-level verifications passed!")
    return True

if __name__ == "__main__":
    if verify_implementation():
        exit(0)
    else:
        exit(1)
