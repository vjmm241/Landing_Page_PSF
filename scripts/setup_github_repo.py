import os
import requests
import sys

def create_github_repo(token, repo_name, profile_url):
    """Creates a new repository on GitHub."""
    print(f"Attempting to create repository: {repo_name} for user via token...")
    
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": False,
        "description": "Landing Page for PSF - Automated Setup"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(f"Successfully created repository: {repo_name}")
        return response.json()["clone_url"]
    elif response.status_code == 422:
        print(f"Repository {repo_name} already exists. Attempting to get details...")
        # Get the repo URL if it already exists
        user_url = "https://api.github.com/user"
        user_res = requests.get(user_url, headers=headers)
        if user_res.status_code == 200:
            username = user_res.json()["login"]
            return f"https://github.com/{username}/{repo_name}.git"
        else:
            print(f"Error fetching user info: {user_res.text}")
            sys.exit(1)
    else:
        print(f"Failed to create repository. Status: {response.status_code}")
        print(f"Message: {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    # In a real scenario, we'd parse CREDENCIALES.txt or use env vars
    # For this script, we'll assume the agent provides them or reads them
    # Since I can't easily parse a non-standard txt file with logic here, 
    # I'll hardcode the known values from my previous view_file call for clarity
    
    # Actually, let's try to be a bit more robust and read the file
    cred_path = r"c:\Users\victo\OneDrive\Documents\Landing_Page_PSF\CREDENCIALES.txt"
    token = None
    
    if os.path.exists(cred_path):
        with open(cred_path, "r") as f:
            for line in f:
                if "GITHUB_TOKEN=" in line:
                    token = line.split("=")[1].strip()
    
    if not token:
        print("GITHUB_TOKEN not found in CREDENCIALES.txt")
        sys.exit(1)
        
    repo_name = "Landing_Page_PSF"
    profile_url = "https://github.com/vjmm241"
    
    repo_url = create_github_repo(token, repo_name, profile_url)
    print(f"REPO_URL_RESULT:{repo_url}")
