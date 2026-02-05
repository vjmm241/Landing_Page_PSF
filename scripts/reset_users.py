import os
from supabase import create_client, Client

# These should be in .env but for a one-time reset script in this environment
# we can use the values from the previously read CREDENCIALES.txt
SUPABASE_URL = "https://kgcdeqsvqneyysubmnch.supabase.co"
SUPABASE_SERVICE_ROLE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtnY2RlcXN2cW5leXlzdWJtbmNoIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2OTcwNjE0MiwiZXhwIjoyMDg1MjgyMTQyfQ.gHQB6TiKJHrm6k0x3IkxmXavWViwX97WmVtHMFMrxMM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def reset_users():
    print("Fetching users...")
    try:
        # Get all users (admin level)
        users_resp = supabase.auth.admin.list_users()
        users = users_resp.users
        
        if not users:
            print("No users found to delete.")
            return

        print(f"Found {len(users)} users. Starting deletion...")
        
        for user in users:
            print(f"Deleting user: {user.email} ({user.id})")
            supabase.auth.admin.delete_user(user.id)
        
        print("Success: All users deleted.")
        
    except Exception as e:
        print(f"Error during user reset: {e}")

if __name__ == "__main__":
    reset_users()
