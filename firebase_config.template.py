# Firebase configuration template
# Copy this file to firebase_config.py and fill in your Firebase project details
import json
import os
from pathlib import Path

# Path to Firebase credentials file
credentials_path = Path(__file__).parent / "firebase-credentials.json"

# Load project ID from credentials file
project_id = "your-project-id"  # Default project ID
if os.path.exists(credentials_path):
    try:
        with open(credentials_path, 'r') as f:
            credentials = json.load(f)
            project_id = credentials.get('project_id', project_id)
    except Exception as e:
        print(f"Error loading Firebase credentials: {e}")

# Firebase web app configuration
# You need to get these values from the Firebase console
# Go to Project Settings > General > Your apps > Web app
firebase_config = {
    "apiKey": "YOUR_API_KEY",  # Replace with your actual API key
    "authDomain": f"{project_id}.firebaseapp.com",
    "databaseURL": f"https://{project_id}.firebaseio.com",
    "projectId": project_id,
    "storageBucket": f"{project_id}.appspot.com",
    "messagingSenderId": "YOUR_MESSAGING_SENDER_ID",  # Replace with your actual sender ID
    "appId": "YOUR_APP_ID"  # Replace with your actual app ID
}

# Service account credentials for admin SDK
credentials_file = credentials_path if os.path.exists(credentials_path) else None
