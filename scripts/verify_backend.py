import requests
import sys

def verify_backend():
    base_url = "http://localhost:3001"
    
    print(f"--- Verifying Backend at {base_url} ---")
    
    # 1. Check Health (if there was a health endpoint, otherwise just try to connect)
    try:
        # Since we don't have a /health endpoint, we try /api/chat with empty body
        # or just check if the port is open
        response = requests.get(base_url)
        print(f"[OK] Connection established. Status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"[FAIL] Could not connect to {base_url}. Is the server running?")
        return False
    
    # 2. Verify /api/chat endpoint
    print("\n[Testing] /api/chat with mock message...")
    data = {
        "message": "Hola, ¿quién eres?",
        "userContext": {"name": "TestBot", "company": "Verification Services"}
    }
    try:
        response = requests.post(f"{base_url}/api/chat", json=data)
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Chat Response received: {result.get('response')[:50].encode('ascii', 'ignore').decode('ascii')}...")
        else:
            print(f"[FAIL] Chat endpoint returned status {response.status_code}")
            print(f"Details: {response.text}")
    except Exception as e:
        print(f"[ERROR] Exception during chat test: {e}")
    
    print("\n--- Verification Complete ---")
    return True

if __name__ == "__main__":
    if not verify_backend():
        sys.exit(1)
