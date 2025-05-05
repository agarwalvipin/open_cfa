import pyrebase
import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth as admin_auth
from firebase_config import firebase_config, credentials_file

# Initialize Firebase Admin SDK (for server-side operations)
def initialize_firebase_admin():
    if not firebase_admin._apps:
        if credentials_file:
            cred = credentials.Certificate(credentials_file)
            firebase_admin.initialize_app(cred)
        else:
            # Use application default credentials if no service account file is available
            firebase_admin.initialize_app()

# Initialize Firebase (for client-side operations)
def initialize_firebase():
    return pyrebase.initialize_app(firebase_config)

# User Registration
def signup(email, password, display_name=None):
    try:
        # Initialize Firebase
        firebase = initialize_firebase()
        auth = firebase.auth()
        
        # Create user
        user = auth.create_user_with_email_and_password(email, password)
        
        # Update display name if provided
        if display_name:
            auth.update_profile(user['idToken'], display_name=display_name)
            
        # Initialize Firebase Admin SDK to set custom claims if needed
        try:
            initialize_firebase_admin()
            # You can set custom claims here if needed
            # admin_auth.set_custom_user_claims(user['localId'], {'role': 'student'})
        except Exception as admin_error:
            # Log the error but continue - admin SDK is optional
            print(f"Admin SDK error (non-critical): {admin_error}")
            
        return {
            'success': True,
            'user': user,
            'message': 'Account created successfully!'
        }
    except Exception as e:
        error_message = str(e)
        if 'EMAIL_EXISTS' in error_message:
            return {
                'success': False,
                'message': 'Email already exists. Please use a different email or login.'
            }
        return {
            'success': False,
            'message': f'Error creating account: {error_message}'
        }

# User Login
def login(email, password):
    try:
        # Initialize Firebase
        firebase = initialize_firebase()
        auth = firebase.auth()
        
        # Sign in user
        user = auth.sign_in_with_email_and_password(email, password)
        
        # Get user info
        user_info = auth.get_account_info(user['idToken'])
        
        return {
            'success': True,
            'user': user,
            'user_info': user_info,
            'message': 'Login successful!'
        }
    except Exception as e:
        error_message = str(e)
        if 'INVALID_PASSWORD' in error_message:
            return {
                'success': False,
                'message': 'Invalid password. Please try again.'
            }
        elif 'EMAIL_NOT_FOUND' in error_message:
            return {
                'success': False,
                'message': 'Email not found. Please sign up first.'
            }
        return {
            'success': False,
            'message': f'Login error: {error_message}'
        }

# Reset Password
def reset_password(email):
    try:
        # Initialize Firebase
        firebase = initialize_firebase()
        auth = firebase.auth()
        
        # Send password reset email
        auth.send_password_reset_email(email)
        
        return {
            'success': True,
            'message': 'Password reset email sent. Please check your inbox.'
        }
    except Exception as e:
        return {
            'success': False,
            'message': f'Error sending password reset email: {str(e)}'
        }

# Get user display name
def get_user_display_name(user):
    try:
        if 'displayName' in user and user['displayName']:
            return user['displayName']
        return user['email'].split('@')[0]  # Use part of email as fallback
    except:
        return 'User'  # Default fallback

# Get user role (requires admin SDK)
def get_user_role(uid):
    try:
        initialize_firebase_admin()
        user = admin_auth.get_user(uid)
        claims = user.custom_claims or {}
        return claims.get('role', 'student')  # Default role is student
    except Exception as e:
        print(f"Error getting user role: {e}")
        return 'student'  # Default fallback

# Verify ID token (requires admin SDK)
def verify_id_token(id_token):
    try:
        initialize_firebase_admin()
        decoded_token = admin_auth.verify_id_token(id_token)
        return {
            'success': True,
            'uid': decoded_token['uid'],
            'claims': decoded_token.get('claims', {})
        }
    except Exception as e:
        return {
            'success': False,
            'message': f"Error verifying token: {e}"
        }
