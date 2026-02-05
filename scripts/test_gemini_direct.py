import requests
import os
from dotenv import load_dotenv

# Load .env from server directory
load_dotenv('server/.env')

api_key = os.getenv('GEMINI_API_KEY')

def test_api():
    print(f"Testing API Key: {api_key[:5]}...")
    
    # Try Listing Models
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    print(f"\n[GET] {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        models = response.json().get('models', [])
        print(f"[OK] Found {len(models)} models.")
        for m in models:
            if '1.5-flash' in m['name'] or 'gemini-pro' in m['name']:
                print(f" - {m['displayName']} ({m['name']})")
    else:
        print(f"[FAIL] Status: {response.status_code}")
        print(f"Details: {response.text}")

if __name__ == "__main__":
    test_api()
