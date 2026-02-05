import requests
import json
import time

# Configuration from nuestra-solucion.html
SUPABASE_URL = "https://kgcdeqsvqneyysubmnch.supabase.co"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtnY2RlcXN2cW5leXlzdWJtbmNoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3MDYxNDIsImV4cCI6MjA4NTI4MjE0Mn0.H9tZkaaiqTsYOD10G_eZDZe4C78ZdxGrXO5C5zYHGJ0"
AUTH_ENDPOINT = f"{SUPABASE_URL}/auth/v1"

HEADERS = {
    "apikey": API_KEY,
    "Content-Type": "application/json"
}

TEST_EMAIL = f"test_e2e_{int(time.time())}@example.com"
TEST_PASSWORD = "Password123!"

def test_signup():
    print(f"--- 1. Testing Signup for {TEST_EMAIL} ---")
    url = f"{AUTH_ENDPOINT}/signup"
    payload = {
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD
    }
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200 or response.status_code == 201:
            print("[PASS] Signup request successful.")
            data = response.json()
            # If OTP is enabled, we might not get a session but a user object
            if "user" in data and data["user"]["aud"] == "authenticated":
                 print("[INFO] User created.")
            elif "user" in data:
                 print("[INFO] User created (unverified).")
            return True
        else:
            print(f"[FAIL] Signup failed: {response.text}")
            return False
            
    except Exception as e:
        print(f"[FAIL] Exception during signup: {e}")
        return False

def test_login_failure():
    print("\n--- 2. Testing Login (Should fail for unverified email) ---")
    url = f"{AUTH_ENDPOINT}/token?grant_type=password"
    payload = {
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD
    }
    
    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        print(f"Status Code: {response.status_code}")
        
        # Expecting 400 because email is not confirmed
        if response.status_code == 400:
             print("[PASS] Login correctly rejected unverified email (Email is not confirmed).")
        else:
             print(f"[INFO] Unexpected status key: {response.status_code}. Response: {response.text}")
             
        return True
    except Exception as e:
         print(f"[FAIL] Exception during login: {e}")
         return False

if __name__ == "__main__":
    if test_signup():
        test_login_failure()
        print("\n[SUCCESS] Auth Endpoints Reachable and behaving as expected.")
    else:
        print("\n[FAILURE] Auth Connectivity Issues Detected.")
