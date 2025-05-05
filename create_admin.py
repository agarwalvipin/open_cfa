#!/usr/bin/env python3

"""
Utility script to create an admin user or update an existing user to admin role
"""

import firebase_auth
import sys

def create_admin_user(email, password):
    """Create a new user with admin role"""
    # Create user
    result = firebase_auth.signup(email, password)
    
    if result['success']:
        # Set admin role
        uid = result['user']['localId']
        role_result = firebase_auth.set_user_role(uid, 'admin')
        
        if role_result['success']:
            print(f"Successfully created admin user: {email}")
            return True
        else:
            print(f"User created but failed to set admin role: {role_result['message']}")
            return False
    else:
        print(f"Failed to create user: {result['message']}")
        return False

def update_user_to_admin(email):
    """Update an existing user to admin role"""
    # Initialize Firebase Admin SDK
    firebase_auth.initialize_firebase_admin()
    
    # Get user by email
    try:
        from firebase_admin import auth
        user = auth.get_user_by_email(email)
        uid = user.uid
        
        # Set admin role
        role_result = firebase_auth.set_user_role(uid, 'admin')
        
        if role_result['success']:
            print(f"Successfully updated user to admin role: {email}")
            return True
        else:
            print(f"Failed to set admin role: {role_result['message']}")
            return False
    except Exception as e:
        print(f"Error finding user: {e}")
        return False

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  To create a new admin: python create_admin.py create <email> <password>")
        print("  To update existing user: python create_admin.py update <email>")
        return
    
    action = sys.argv[1]
    
    if action == "create" and len(sys.argv) >= 4:
        email = sys.argv[2]
        password = sys.argv[3]
        create_admin_user(email, password)
    elif action == "update" and len(sys.argv) >= 3:
        email = sys.argv[2]
        update_user_to_admin(email)
    else:
        print("Invalid arguments.")
        print("Usage:")
        print("  To create a new admin: python create_admin.py create <email> <password>")
        print("  To update existing user: python create_admin.py update <email>")

if __name__ == "__main__":
    main()
