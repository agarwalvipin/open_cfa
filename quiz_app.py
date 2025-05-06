#!/usr/bin/env python3

"""
Streamlit Quiz App for CFA Level I Exam Questions
"""

import streamlit as st
import os
import random
import time
import pandas as pd
from pathlib import Path
import firebase_auth
import user_stats
import requests
import role_management
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import json
from datetime import datetime, timedelta
import pickle
import base64

# Set page configuration
st.set_page_config(
    page_title="CFA Level I Quiz App",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Import admin dashboard functions - must be after set_page_config
from admin_dashboard import get_system_stats, get_user_activity_stats, cleanup_questions

# Import necessary modules for dynamic import
from importlib.util import spec_from_file_location, module_from_spec
import sys
import tempfile

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from environment variables
DB_PARAMS = {
    'dbname': os.getenv('DB_NAME', 'cfa_db'),
    'user': os.getenv('DB_USER', 'cfauser'),
    'password': os.getenv('DB_PASSWORD', 'cfaPass'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '54320')  # Port mapped to Docker container
}

# Database connection function
def connect_to_db(db_path=None):
    """Connect to PostgreSQL database
    
    The db_path parameter is kept for backward compatibility but not used
    """
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**DB_PARAMS)
        # Use DictCursor to enable column access by name (similar to sqlite3.Row)
        conn.cursor_factory = psycopg2.extras.DictCursor
        return conn
    except Exception as e:
        st.error(f"Error connecting to PostgreSQL database: {e}")
        return None

# Get all topics from the database
def get_topics(conn):
    """Get all topics from the database"""
    cursor = conn.cursor()
    cursor.execute("SELECT topic_id, name FROM topics")
    return cursor.fetchall()

# Get question count by filter criteria
def get_question_count(conn, topic_ids=None, week_ids=None):
    """Get count of questions for selected topics and/or weeks"""
    # If no filters are provided, return 0
    if not topic_ids and not week_ids:
        return 0
    
    cursor = conn.cursor()
    
    # Special handling for multiple topics - we want the sum of questions for each topic
    if topic_ids and len(topic_ids) > 1 and not week_ids:
        # For multiple topics without week filter, we want the sum of all questions in those topics
        # Use DISTINCT to avoid counting questions that belong to multiple selected topics more than once
        topic_ids_str = ','.join('%s' for _ in topic_ids)
        query = f"SELECT COUNT(DISTINCT question_id) as count FROM questions WHERE topic_id IN ({topic_ids_str})"
        cursor.execute(query, topic_ids)
        result = cursor.fetchone()
        return result['count'] if result else 0
    
    # Standard filtering with AND logic for other cases
    conditions = []
    params = []
    
    if topic_ids:
        topic_ids_str = ','.join('%s' for _ in topic_ids)
        conditions.append(f"topic_id IN ({topic_ids_str})")
        params.extend(topic_ids)
    
    if week_ids:
        week_ids_str = ','.join('%s' for _ in week_ids)
        conditions.append(f"week_id IN ({week_ids_str})")
        params.extend(week_ids)
    
    query = "SELECT COUNT(*) as count FROM questions"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    
    cursor.execute(query, params)
    result = cursor.fetchone()
    return result['count'] if result else 0

# Get questions by filter criteria
def get_filtered_questions(conn, topic_ids=None, week_ids=None, limit=None):
    """Get questions for selected topics and/or weeks with optional limit"""
    conditions = []
    params = []
    
    if topic_ids:
        topic_ids_str = ','.join('%s' for _ in topic_ids)
        conditions.append(f"q.topic_id IN ({topic_ids_str})")
        params.extend(topic_ids)
    
    if week_ids:
        week_ids_str = ','.join('%s' for _ in week_ids)
        conditions.append(f"q.week_id IN ({week_ids_str})")
        params.extend(week_ids)
    
    if not conditions:
        return []
    
    query = "SELECT q.question_id FROM questions q"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    
    if limit:
        query += " ORDER BY RANDOM() LIMIT %s"
        params.append(limit)
    
    cursor = conn.cursor()
    cursor.execute(query, params)
    return [row['question_id'] for row in cursor.fetchall()]

# Get complete question details
def get_question_details(conn, question_id):
    """Get complete details for a specific question"""
    cursor = conn.cursor()
    
    # Get question data
    cursor.execute("""
        SELECT q.question_id, q.title, q.question_text, 
               t.name as topic, m.name as module, 
               d.name as difficulty, r.name as reading,
               l.text as learning_objective
        FROM questions q
        JOIN topics t ON q.topic_id = t.topic_id
        JOIN modules m ON q.module_id = m.module_id
        JOIN difficulty_levels d ON q.difficulty_id = d.difficulty_id
        LEFT JOIN readings r ON q.reading_id = r.reading_id
        LEFT JOIN learning_objectives l ON q.los_id = l.los_id
        WHERE q.question_id = %s
    """, (question_id,))
    question = cursor.fetchone()
    
    if not question:
        return None
    
    # Get answer options
    cursor.execute("""
        SELECT option_letter, option_text, is_correct
        FROM answer_options
        WHERE question_id = %s
        ORDER BY option_letter
    """, (question_id,))
    options = cursor.fetchall()
    
    # Get explanation
    cursor.execute("""
        SELECT explanation_text
        FROM explanations
        WHERE question_id = %s
    """, (question_id,))
    explanation = cursor.fetchone()
    
    # Get tags
    cursor.execute("""
        SELECT t.name
        FROM tags t
        JOIN question_tags qt ON t.tag_id = qt.tag_id
        WHERE qt.question_id = %s
    """, (question_id,))
    tags = cursor.fetchall()
    
    return {
        'question': dict(question),
        'options': [dict(option) for option in options],
        'explanation': explanation['explanation_text'] if explanation else None,
        'tags': [tag['name'] for tag in tags]
    }

# Function to encode session data for URL parameter
def encode_session_data(data):
    # Convert data to JSON string
    json_data = json.dumps(data)
    # Encode as base64 to make it URL-safe
    encoded = base64.b64encode(json_data.encode()).decode()
    return encoded

# Function to decode session data from URL parameter
def decode_session_data(encoded_data):
    try:
        # Decode base64 string
        json_data = base64.b64decode(encoded_data).decode()
        # Parse JSON data
        data = json.loads(json_data)
        return data
    except Exception as e:
        st.error(f"Error decoding session data: {e}")
        return None

# Function to save authentication data to session state
def save_auth_to_session(user_data, remember_me=False):
    if not remember_me:
        return False
    
    # Prepare auth data
    auth_data = {
        'idToken': user_data.get('idToken', ''),
        'uid': user_data.get('localId', ''),
        'email': user_data.get('email', ''),
        'username': user_data.get('displayName', user_data.get('email', '').split('@')[0]),
        'role': st.session_state.get('user_role', 'student'),
        'expiry': (datetime.now() + timedelta(days=30)).isoformat()  # 30 days expiry
    }
    
    # Save to session state
    st.session_state.auth_token = encode_session_data(auth_data)
    return True

# Function to check if auth token is valid
def is_auth_token_valid(auth_token):
    try:
        auth_data = decode_session_data(auth_token)
        if auth_data and 'expiry' in auth_data:
            # Check if token is still valid (not expired)
            expiry = datetime.fromisoformat(auth_data['expiry'])
            if datetime.now() < expiry:
                return True
    except Exception as e:
        st.error(f"Error validating auth token: {e}")
    return False

# Function to restore session from auth token
def restore_session_from_token(auth_token):
    auth_data = decode_session_data(auth_token)
    if auth_data:
        # Restore session state
        st.session_state.authenticated = True
        st.session_state.user = {'localId': auth_data.get('uid', '')}
        st.session_state.user_uid = auth_data.get('uid', '')
        st.session_state.user_role = auth_data.get('role', 'student')
        st.session_state.username = auth_data.get('username', '')
        st.session_state.remember_me = True
        st.session_state.saved_email = auth_data.get('email', '')
        return True
    return False

# Main app function
def main():
    # Initialize session state variables for authentication
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'auth_page' not in st.session_state:
        st.session_state.auth_page = "login"
    if 'remember_me' not in st.session_state:
        st.session_state.remember_me = False
    if 'saved_email' not in st.session_state:
        st.session_state.saved_email = ""
    if 'auth_token' not in st.session_state:
        st.session_state.auth_token = None
    
    # Check for auth token in URL parameters
    query_params = st.experimental_get_query_params()
    if 'auth' in query_params and not st.session_state.authenticated:
        auth_token = query_params['auth'][0]
        if is_auth_token_valid(auth_token):
            # Restore session from token
            if restore_session_from_token(auth_token):
                st.success(f"Welcome back, {st.session_state.username}! You've been automatically logged in.")
    
    # Set auth token in URL if authenticated and remember_me is enabled
    if st.session_state.authenticated and st.session_state.remember_me and 'auth_token' in st.session_state:
        # Update URL with auth token
        st.experimental_set_query_params(auth=st.session_state.auth_token)
    
    # Check if user has saved credentials
    if st.session_state.remember_me and st.session_state.saved_email and not st.session_state.authenticated:
        st.info(f"Welcome back! Using saved credentials for {st.session_state.saved_email}")
    
    # Connect to PostgreSQL database
    conn = connect_to_db()
    # Database connection message removed
    if not conn:
        return
    
    # Show role-based sidebar if user is logged in
    if 'user_uid' in st.session_state:
        role_management.show_role_based_sidebar(st.session_state['user_uid'])
    
    # Login/Signup screen if not authenticated
    if not st.session_state.authenticated:
        st.title("CFA Level I Quiz App")
        
        # Tabs for login and signup
        login_tab, signup_tab = st.tabs(["Login", "Sign Up"])
        
        # Login tab
        with login_tab:
            with st.form("login_form"):
                # Pre-fill email if remember_me was checked previously
                email = st.text_input("Email", value=st.session_state.saved_email if st.session_state.remember_me else "")
                password = st.text_input("Password", type="password")
                remember_me = st.checkbox("Remember Me", value=True, help="Keep me logged in on this device")
                submit_button = st.form_submit_button("Login")
                
                if submit_button:
                    if email and password:
                        # Use Firebase authentication
                        result = firebase_auth.login(email, password)
                        
                        if result['success']:
                            st.session_state.authenticated = True
                            st.session_state['user'] = result['user']
                            st.session_state['user_uid'] = result['user_info']['users'][0]['localId']
                            
                            # Get user role
                            user_uid = st.session_state['user_uid']
                            user_role = firebase_auth.get_user_role(user_uid)
                            st.session_state['user_role'] = user_role
                            
                            # Save authentication data if remember_me is checked
                            if remember_me:
                                st.session_state.remember_me = True
                                st.session_state.saved_email = email
                                # Save to session state for persistent login
                                save_auth_to_session(result['user'], remember_me=True)
                            
                            st.success(f"Login successful! You are logged in as a {user_role.capitalize()}.")
                            time.sleep(1)
                                
                            st.success(result['message'])
                            st.rerun()  # Rerun to show the main app
                        else:
                            st.error(result['message'])
                    else:
                        st.error("Please enter both email and password")
            
            # Password reset link
            forgot_password = st.checkbox("Forgot Password?")
            if forgot_password:
                with st.form("reset_password_form"):
                    reset_email = st.text_input("Enter your email to reset password")
                    reset_button = st.form_submit_button("Send Reset Link")
                    
                    if reset_button and reset_email:
                        reset_result = firebase_auth.reset_password(reset_email)
                        if reset_result['success']:
                            st.success(reset_result['message'])
                        else:
                            st.error(reset_result['message'])
        
        # Signup tab
        with signup_tab:
            with st.form("signup_form"):
                new_email = st.text_input("Email")
                display_name = st.text_input("Display Name (optional)")
                new_password = st.text_input("Password", type="password")
                confirm_password = st.text_input("Confirm Password", type="password")
                signup_button = st.form_submit_button("Sign Up")
                
                if signup_button:
                    if new_email and new_password:
                        if new_password == confirm_password:
                            # Use Firebase authentication for signup
                            result = firebase_auth.signup(new_email, new_password, display_name)
                            
                            if result['success']:
                                st.success(result['message'])
                                st.info("Please go to the Login tab to sign in with your new account.")
                            else:
                                st.error(result['message'])
                        else:
                            st.error("Passwords do not match")
                    else:
                        st.error("Please enter both email and password")
        
        return  # Exit the function if not authenticated
    
    # Initialize page state for navigation
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'dashboard'
    
    # Logout button in sidebar
    st.sidebar.title("Account")
    if st.sidebar.button("Logout", key="logout_button"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.username = ""
        if 'user_uid' in st.session_state:
            del st.session_state['user_uid']
        if 'user_role' in st.session_state:
            del st.session_state['user_role']
        
        # Handle remember me preference during logout
        if not st.session_state.remember_me:
            # If remember me is not checked, clear saved email too
            st.session_state.saved_email = ""
        
        # Clear auth token
        st.session_state.auth_token = None
        # Clear URL parameters
        st.experimental_set_query_params()
            
        st.session_state.current_page = 'dashboard'  # Reset to dashboard for next login
        st.rerun()
    
    # Import the necessary modules for question import functionality
    import sys
    import tempfile
    from importlib.util import spec_from_file_location, module_from_spec
    
    # Import the import_to_sqlite module dynamically
    def import_module_from_path(module_name, file_path):
        spec = spec_from_file_location(module_name, file_path)
        module = module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    
    # Path to the import_questions.py file (PostgreSQL importer)
    import_script_path = Path(__file__).parent / "database" / "import_questions.py"
    
    # Schema file selection
    schema_path = Path(__file__).parent / "database" / "schema.sql"
    
    # Display the selected page
    if st.session_state.current_page == 'dashboard':
        # Dashboard page
        st.title("CFA Level I Study Dashboard")
        st.markdown(f"Welcome, {st.session_state.username}! 👋")
        
        # Create tabs for dashboard sections
        tab1, tab2 = st.tabs(["Overview", "Performance Stats"])
        
        # Dashboard content for Overview tab
        with tab1:
            st.markdown("""
            ### Your CFA Level I Study Portal
            
            This dashboard provides access to study resources and practice quizzes for your CFA Level I exam preparation.
            
            #### Available Features:
            - **Create Quiz**: Create customized quizzes with specific filters
            - **Take Quiz**: Test your knowledge with topic-specific quizzes
            - **Practice Question**: Practice with individual questions and get immediate feedback
            - **Load Questions**: Upload question files to expand your question bank
            - **Performance Stats**: Monitor your progress in the Performance Stats tab
            """)
            
            # Get question count for dashboard stats
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) as count FROM questions")
            question_count = cursor.fetchone()['count']
            
            cursor.execute("SELECT COUNT(DISTINCT topic_id) as count FROM questions")
            topic_count = cursor.fetchone()['count']
        
            # Quick stats
            st.subheader("Quick Stats")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Questions Available", value=str(question_count))
            with col2:
                st.metric(label="Topics Covered", value=str(topic_count))
            with col3:
                # Get quiz count from user stats if available
                quiz_count = "0"
                if 'user' in st.session_state:
                    user_uid = st.session_state.user.get('localId')
                    user_stats_data = user_stats.get_user_stats(user_uid)
                    if user_stats_data:
                        quiz_count = str(user_stats_data.get('total_quizzes_taken', 0))
                st.metric(label="Your Quizzes Taken", value=quiz_count)
            
            # Call to action
            st.markdown("""
            <div style='text-align: center; margin-top: 2rem;'>
                <h3>Ready to test your knowledge?</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Create Quiz", type="primary", use_container_width=True):
                    st.session_state.current_page = 'create_quiz'
                    # Initialize quiz wizard state
                    if 'quiz_wizard_step' not in st.session_state:
                        st.session_state.quiz_wizard_step = 1
                    st.rerun()
            with col2:
                if st.button("Take Quiz", type="secondary", use_container_width=True):
                    st.session_state.current_page = 'quiz'
                    st.rerun()
            
            col3, col4 = st.columns(2)
            with col3:
                if st.button("Practice Question", type="secondary", use_container_width=True):
                    st.session_state.current_page = 'practice_question'
                    st.rerun()
            with col4:
                if st.button("Load Questions", type="secondary", use_container_width=True):
                    st.session_state.current_page = 'load_questions'
                    st.rerun()
        
        # Performance Stats tab
        with tab2:
            # Only show dashboard if user is logged in
            if 'user' in st.session_state:
                user_uid = st.session_state.user.get('localId')
                
                # Display user dashboard
                user_stats.display_user_dashboard(conn, user_uid)
            else:
                st.info("Please log in to view your performance statistics")
    
    elif st.session_state.current_page == 'load_questions':
        # Load Questions page
        st.title("Load Questions")
        st.markdown("""
        Add CFA Level I questions to your question bank by uploading markdown files or providing a URL to a markdown file.
        
        The file should follow the standard question format with metadata, question text, options, and explanations.
        """)
        
        # Create tabs for different import methods
        upload_tab, url_tab = st.tabs(["Upload File", "Import from URL"])
        
        # Upload File Tab
        with upload_tab:
            # File uploader
            uploaded_file = st.file_uploader("Choose a markdown file", type=['md'])
            
            if uploaded_file is not None:
                # Create a temporary file to save the uploaded content
                with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    temp_path = tmp_file.name
                
                # Show the import options
                st.subheader("Import Options")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Preview File", use_container_width=True, key="preview_upload"):
                        with open(temp_path, 'r') as f:
                            file_content = f.read()
                        st.text_area("File Content Preview", file_content, height=300)
                
                with col2:
                    if st.button("Import Questions", type="primary", use_container_width=True, key="import_upload"):
                        try:
                            # Import the module
                            import_module = import_module_from_path("import_questions", str(import_script_path))
                            
                            # Use functions from the imported module
                            with st.spinner("Importing questions..."):
                                # Parse the questions from the file
                                questions = import_module.parse_question_file(temp_path)
                                
                                # Connect to PostgreSQL database
                                conn = connect_to_db()
                                
                                # Import the questions to the database
                                import_module.import_questions_to_db(questions, conn)
                                
                                # Close the connection
                                conn.close()
                            
                            # Success message
                            st.success(f"Successfully imported {len(questions)} questions!")
                            
                            # Update connection for the main app
                            conn = connect_to_db()
                        except Exception as e:
                            st.error(f"Error importing questions: {str(e)}")
        
        # Import from URL Tab
        with url_tab:
            st.markdown("Enter the URL of a markdown file containing CFA Level I questions.")
            url = st.text_input("URL to markdown file", placeholder="https://example.com/questions.md")
            
            if url:
                # Show the import options
                st.subheader("Import Options")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Preview File", use_container_width=True, key="preview_url"):
                        try:
                            # Fetch content from URL
                            response = requests.get(url)
                            if response.status_code == 200:
                                file_content = response.text
                                st.text_area("File Content Preview", file_content, height=300)
                            else:
                                st.error(f"Failed to fetch content: HTTP {response.status_code}")
                        except Exception as e:
                            st.error(f"Error fetching URL: {str(e)}")
                
                with col2:
                    if st.button("Import Questions", type="primary", use_container_width=True, key="import_url"):
                        try:
                            # Fetch content from URL
                            response = requests.get(url)
                            if response.status_code != 200:
                                st.error(f"Failed to fetch content: HTTP {response.status_code}")
                                st.stop()
                            
                            # Save content to temporary file
                            with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp_file:
                                tmp_file.write(response.content)
                                temp_path = tmp_file.name
                            
                            # Import the module
                            import_module = import_module_from_path("import_questions", str(import_script_path))
                            
                            # Use functions from the imported module
                            with st.spinner("Importing questions..."):
                                # Parse the questions from the file
                                questions = import_module.parse_question_file(temp_path)
                                
                                # Connect to PostgreSQL database
                                conn = connect_to_db()
                                
                                # Import the questions to the database
                                import_module.import_questions_to_db(questions, conn)
                                
                                # Clean up the temporary file
                                os.unlink(temp_path)
                                
                                # Close the connection
                                conn.close()
                            
                            # Success message
                            st.success(f"Successfully imported {len(questions)} questions from URL!")
                            
                            # Update connection for the main app
                            conn = connect_to_db()
                        except Exception as e:
                            st.error(f"Error importing questions: {str(e)}")
        
        # Display file format requirements
        st.markdown("""
        #### File Format Requirements
        
        The markdown file should follow this structure:
        - Question title as a heading (##)
        - Metadata section in a details/summary HTML element
        - Question text and options (with A), B), C) format)
        - Answer and explanation in a details/summary HTML element
        - Questions separated by horizontal rules (---)
        """)
    
    elif st.session_state.current_page == 'admin_dashboard':
        # Admin Dashboard page
        st.title("Admin Dashboard")
        
        # Check if user has admin role
        if not role_management.check_user_access(st.session_state['user_uid'], 'admin'):
            st.error("You do not have permission to access this page.")
            st.session_state.current_page = 'dashboard'
            st.rerun()
            return
        
        # System stats
        st.header("System Statistics")
        
        # Create tabs for different stats
        tab1, tab2, tab3 = st.tabs(["Question Database", "User Activity", "Database Management"])
        
        with tab1:
            # Question database stats
            system_stats = get_system_stats(conn)
            
            # Display total questions
            st.subheader(f"Total Questions: {system_stats['total_questions']}")
            
            # Create columns for different stats
            col1, col2 = st.columns(2)
            
            with col1:
                # Questions by topic
                st.subheader("Questions by Topic")
                if system_stats['questions_by_topic']:
                    topic_data = [dict(row) for row in system_stats['questions_by_topic']]
                    topic_df = pd.DataFrame(topic_data)
                    st.bar_chart(topic_df.set_index('topic'))
                    st.dataframe(topic_df, use_container_width=True)
                else:
                    st.info("No topic data available")
                
                # Questions by difficulty
                st.subheader("Questions by Difficulty")
                if system_stats['questions_by_difficulty']:
                    difficulty_data = [dict(row) for row in system_stats['questions_by_difficulty']]
                    difficulty_df = pd.DataFrame(difficulty_data)
                    st.bar_chart(difficulty_df.set_index('difficulty'))
                    st.dataframe(difficulty_df, use_container_width=True)
                else:
                    st.info("No difficulty data available")
            
            with col2:
                # Questions by week
                st.subheader("Questions by Week")
                if system_stats['questions_by_week']:
                    week_data = [dict(row) for row in system_stats['questions_by_week']]
                    week_df = pd.DataFrame(week_data)
                    st.bar_chart(week_df.set_index('week'))
                    st.dataframe(week_df, use_container_width=True)
                else:
                    st.info("No week data available")
        
        with tab2:
            # User activity stats
            user_activity = get_user_activity_stats()
            
            # Display total users
            st.subheader(f"Total Users: {user_activity['user_count']}")
            
            # Recent quiz attempts
            st.subheader("Recent Quiz Attempts")
            if user_activity['recent_quizzes']:
                # Convert to DataFrame for easier display
                quiz_df = pd.DataFrame(user_activity['recent_quizzes'])
                
                # Format date column
                if 'date' in quiz_df.columns:
                    quiz_df['date'] = quiz_df['date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M") if hasattr(x, 'strftime') else str(x))
                
                # Format time taken
                if 'time_taken_seconds' in quiz_df.columns:
                    quiz_df['time_taken'] = quiz_df['time_taken_seconds'].apply(lambda x: f"{x//60}m {x%60}s")
                
                # Format score as percentage
                if 'score' in quiz_df.columns:
                    quiz_df['score'] = quiz_df['score'].apply(lambda x: f"{x:.1f}%")
                
                # Display the dataframe
                st.dataframe(quiz_df[['date', 'user_uid', 'num_questions', 'score', 'time_taken']], use_container_width=True)
            else:
                st.info("No recent quiz attempts")
        
        # Database Management tab
        with tab3:
            st.subheader("Database Cleanup")
            st.warning("⚠️ Warning: This operation will permanently delete questions and related data from the database. This action cannot be undone.")
            
            # Create filters for cleanup
            col1, col2 = st.columns(2)
            
            with col1:
                # Topic filter
                cursor = conn.cursor()
                cursor.execute("SELECT topic_id, name FROM topics ORDER BY name")
                topics = cursor.fetchall()
                
                topic_options = {"All Topics": None}
                for topic in topics:
                    topic_options[topic['name']] = topic['topic_id']
                
                selected_topic_name = st.selectbox("Select Topic", options=list(topic_options.keys()))
                selected_topic_id = topic_options[selected_topic_name]
            
            with col2:
                # Week filter
                cursor.execute("SELECT week_id, week_number FROM weeks ORDER BY week_number")
                weeks = cursor.fetchall()
                
                week_options = {"All Weeks": None}
                for week in weeks:
                    week_options[f"Week {week['week_number']}"] = week['week_id']
                
                selected_week_name = st.selectbox("Select Week", options=list(week_options.keys()))
                selected_week_id = week_options[selected_week_name]
            
            # Show count of questions that will be affected
            where_clause = ""
            params = []
            
            if selected_topic_id:
                where_clause += " topic_id = %s"
                params.append(selected_topic_id)
            
            if selected_week_id:
                if where_clause:
                    where_clause += " AND"
                where_clause += " week_id = %s"
                params.append(selected_week_id)
            
            if where_clause:
                where_clause = " WHERE" + where_clause
            
            # Get count of affected questions
            cursor.execute(f"SELECT COUNT(*) as count FROM questions{where_clause}", params)
            affected_count = cursor.fetchone()['count']
            
            st.info(f"This operation will delete {affected_count} questions and their related data.")
            
            # Confirmation checkbox
            confirm = st.checkbox("I understand that this operation cannot be undone and confirm the deletion")
            
            # Execute cleanup button
            if st.button("Execute Cleanup", type="primary", disabled=not confirm):
                message, success = cleanup_questions(conn, selected_topic_id, selected_week_id, confirm)
                
                if success:
                    st.success(message)
                    # Refresh stats after cleanup
                    system_stats = get_system_stats(conn)
                else:
                    st.error(message)
            
            # Add option to clean orphaned data
            st.subheader("Clean Orphaned Data")
            st.info("This will remove unused topics, tags, modules, and other reference data that are not associated with any questions.")
            
            if st.button("Clean Orphaned Data", type="secondary"):
                try:
                    cursor = conn.cursor()  # Get cursor
                    cursor.execute("BEGIN TRANSACTION") # Use cursor

                    # Delete orphaned tags
                    cursor.execute("""
                        DELETE FROM tags 
                        WHERE tag_id NOT IN (SELECT DISTINCT tag_id FROM question_tags)
                    """)
                    tags_deleted = cursor.rowcount
                    
                    # Delete orphaned learning objectives
                    cursor.execute("""
                        DELETE FROM learning_objectives 
                        WHERE los_id NOT IN (SELECT DISTINCT los_id FROM questions WHERE los_id IS NOT NULL)
                    """)
                    los_deleted = cursor.rowcount
                    
                    # Delete orphaned modules
                    cursor.execute("""
                        DELETE FROM modules 
                        WHERE module_id NOT IN (SELECT DISTINCT module_id FROM questions WHERE module_id IS NOT NULL)
                    """)
                    modules_deleted = cursor.rowcount
                    
                    # Delete orphaned readings
                    cursor.execute("""
                        DELETE FROM readings 
                        WHERE reading_id NOT IN (SELECT DISTINCT reading_id FROM questions WHERE reading_id IS NOT NULL)
                    """)
                    readings_deleted = cursor.rowcount
                    
                    conn.commit()
                    
                    st.success(f"Successfully cleaned up orphaned data: {tags_deleted} tags, {los_deleted} learning objectives, {modules_deleted} modules, and {readings_deleted} readings.")
                    
                except Exception as e:
                    conn.rollback()
                    st.error(f"Error cleaning orphaned data: {str(e)}")
    
    elif st.session_state.current_page == 'create_quiz':
        # Quiz Creation Wizard
        st.title("Create Your Custom Quiz")
        st.markdown("""
        Follow the steps below to create a customized quiz based on your preferences.
        """)
        
        # Initialize wizard state if not already done
        if 'quiz_wizard_step' not in st.session_state:
            st.session_state.quiz_wizard_step = 1
        if 'quiz_filters' not in st.session_state:
            st.session_state.quiz_filters = {
                'topic_ids': [],
                'week_ids': [],
                'difficulty_ids': [],
                'module_ids': [],
                'tag_ids': []
            }
        
        # Progress bar for the wizard
        st.progress((st.session_state.quiz_wizard_step - 1) / 5)
        
        # Step 1: Topic Selection
        if st.session_state.quiz_wizard_step == 1:
            st.subheader("Step 1: Select Topics")
            
            # Get all topics
            topics = get_topics(conn)
            topic_options = {topic['name']: topic['topic_id'] for topic in topics}
            
            # Check if we have topics
            if not topic_options:
                st.error("No topics found in the database. Please import questions first.")
                st.stop()
            
            # Add 'All' option
            topic_options_with_all = {"All": "all"} | topic_options
            
            if len(topic_options) == 1:
                # If there's only one topic, select it by default
                only_topic = list(topic_options.keys())[0]
                st.info(f"Currently only one topic is available: {only_topic}")
                selected_topic_names = [only_topic]
            else:
                selected_topic_names = st.multiselect(
                    "Select Topics",
                    options=list(topic_options_with_all.keys()),
                    default=["All"] if not st.session_state.quiz_filters['topic_ids'] else [name for name in topic_options.keys() if topic_options[name] in st.session_state.quiz_filters['topic_ids']],
                    help="Choose one or more topics for your quiz",
                    key="create_quiz_topics"
                )
            
            # Get selected topic IDs
            if "All" in selected_topic_names:
                # If 'All' is selected, don't filter by topic
                selected_topic_ids = []
            else:
                selected_topic_ids = [topic_options[name] for name in selected_topic_names]
            
            # Store selected topics in session state
            st.session_state.quiz_filters['topic_ids'] = selected_topic_ids
            
            # Navigation buttons
            col1, col2 = st.columns([1, 5])
            if col2.button("Next: Select Weeks", type="primary"):
                st.session_state.quiz_wizard_step = 2
                st.rerun()
        
        # Step 2: Week Selection
        elif st.session_state.quiz_wizard_step == 2:
            st.subheader("Step 2: Select Weeks")
            
            # Get all weeks
            cursor = conn.cursor()
            cursor.execute("SELECT week_id, week_number FROM weeks ORDER BY week_number")
            weeks = cursor.fetchall()
            week_options = {f"Week {week['week_number']}": week['week_id'] for week in weeks}
            
            # Add 'All' option
            week_options_with_all = {"All": "all"} | week_options
            
            if len(week_options) == 1:
                # If there's only one week, select it by default
                only_week = list(week_options.keys())[0]
                st.info(f"Currently only {only_week} is available")
                selected_week_names = [only_week]
            else:
                selected_week_names = st.multiselect(
                    "Select Weeks",
                    options=list(week_options_with_all.keys()),
                    default=["All"] if not st.session_state.quiz_filters['week_ids'] else [name for name in week_options.keys() if week_options[name] in st.session_state.quiz_filters['week_ids']],
                    help="Choose one or more weeks for your quiz",
                    key="create_quiz_weeks"
                )
            
            # Get selected week IDs
            if "All" in selected_week_names:
                # If 'All' is selected, don't filter by week
                selected_week_ids = []
            else:
                selected_week_ids = [week_options[name] for name in selected_week_names]
            
            # Store selected weeks in session state
            st.session_state.quiz_filters['week_ids'] = selected_week_ids
            
            # Navigation buttons
            col1, col2, col3 = st.columns([1, 1, 4])
            if col1.button("Previous: Topics", type="secondary"):
                st.session_state.quiz_wizard_step = 1
                st.rerun()
            if col2.button("Next: Difficulty", type="primary"):
                st.session_state.quiz_wizard_step = 3
                st.rerun()
        
        # Step 3: Difficulty Selection
        elif st.session_state.quiz_wizard_step == 3:
            st.subheader("Step 3: Select Difficulty Levels")
            
            # Get all difficulty levels
            cursor = conn.cursor()
            cursor.execute("SELECT difficulty_id, name FROM difficulty_levels ORDER BY difficulty_id")
            difficulties = cursor.fetchall()
            difficulty_options = {diff['name']: diff['difficulty_id'] for diff in difficulties}
            
            # Add 'All' option
            difficulty_options_with_all = {"All": "all"} | difficulty_options
            
            if difficulties:
                selected_difficulty_names = st.multiselect(
                    "Select Difficulty Levels",
                    options=list(difficulty_options_with_all.keys()),
                    default=["All"] if not st.session_state.quiz_filters['difficulty_ids'] else [name for name in difficulty_options.keys() if difficulty_options[name] in st.session_state.quiz_filters['difficulty_ids']],
                    help="Choose one or more difficulty levels for your quiz",
                    key="create_quiz_difficulties"
                )
                
                # Get selected difficulty IDs
                if "All" in selected_difficulty_names:
                    # If 'All' is selected, don't filter by difficulty
                    selected_difficulty_ids = []
                else:
                    selected_difficulty_ids = [difficulty_options[name] for name in selected_difficulty_names]
                
                # Store selected difficulties in session state
                st.session_state.quiz_filters['difficulty_ids'] = selected_difficulty_ids
            else:
                st.info("No difficulty levels found in the database.")
            
            # Navigation buttons
            col1, col2, col3 = st.columns([1, 1, 4])
            if col1.button("Previous: Weeks", type="secondary"):
                st.session_state.quiz_wizard_step = 2
                st.rerun()
            if col2.button("Next: Modules", type="primary"):
                st.session_state.quiz_wizard_step = 4
                st.rerun()
        
        # Step 4: Module Selection
        elif st.session_state.quiz_wizard_step == 4:
            st.subheader("Step 4: Select Modules")
            
            # Get all modules
            cursor = conn.cursor()
            cursor.execute("SELECT module_id, name FROM modules ORDER BY name")
            modules = cursor.fetchall()
            module_options = {mod['name']: mod['module_id'] for mod in modules}
            
            # Add 'All' option
            module_options_with_all = {"All": "all"} | module_options
            
            if modules:
                selected_module_names = st.multiselect(
                    "Select Modules",
                    options=list(module_options_with_all.keys()),
                    default=["All"] if not st.session_state.quiz_filters['module_ids'] else [name for name in module_options.keys() if module_options[name] in st.session_state.quiz_filters['module_ids']],
                    help="Choose one or more modules for your quiz",
                    key="create_quiz_modules"
                )
                
                # Get selected module IDs
                if "All" in selected_module_names:
                    # If 'All' is selected, don't filter by module
                    selected_module_ids = []
                else:
                    selected_module_ids = [module_options[name] for name in selected_module_names]
                
                # Store selected modules in session state
                st.session_state.quiz_filters['module_ids'] = selected_module_ids
            else:
                st.info("No modules found in the database.")
            
            # Navigation buttons
            col1, col2, col3 = st.columns([1, 1, 4])
            if col1.button("Previous: Difficulty", type="secondary"):
                st.session_state.quiz_wizard_step = 3
                st.rerun()
            if col2.button("Next: Tags", type="primary"):
                st.session_state.quiz_wizard_step = 5
                st.rerun()
        
        # Step 5: Tags Selection and Quiz Size
        elif st.session_state.quiz_wizard_step == 5:
            st.subheader("Step 5: Select Tags and Quiz Size")
            
            # Get all tags
            cursor = conn.cursor()
            cursor.execute("SELECT tag_id, name FROM tags ORDER BY name")
            tags = cursor.fetchall()
            tag_options = {tag['name']: tag['tag_id'] for tag in tags}
            
            # Add 'All' option
            tag_options_with_all = {"All": "all"} | tag_options
            
            if tags:
                selected_tag_names = st.multiselect(
                    "Select Tags",
                    options=list(tag_options_with_all.keys()),
                    default=["All"] if not st.session_state.quiz_filters['tag_ids'] else [name for name in tag_options.keys() if tag_options[name] in st.session_state.quiz_filters['tag_ids']],
                    help="Choose one or more tags for your quiz",
                    key="create_quiz_tags"
                )
                
                # Get selected tag IDs
                if "All" in selected_tag_names:
                    # If 'All' is selected, don't filter by tag
                    selected_tag_ids = []
                else:
                    selected_tag_ids = [tag_options[name] for name in selected_tag_names]
                
                # Store selected tags in session state
                st.session_state.quiz_filters['tag_ids'] = selected_tag_ids
            else:
                st.info("No tags found in the database.")
            
            # Calculate available questions based on filters
            query = "SELECT COUNT(DISTINCT q.question_id) as count FROM questions q"
            conditions = []
            params = []
            
            # Only add filter conditions if specific options are selected (not 'All')
            if st.session_state.quiz_filters['topic_ids']:
                topic_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['topic_ids'])
                conditions.append(f"q.topic_id IN ({topic_ids_str})")
                params.extend(st.session_state.quiz_filters['topic_ids'])
            
            if st.session_state.quiz_filters['week_ids']:
                week_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['week_ids'])
                conditions.append(f"q.week_id IN ({week_ids_str})")
                params.extend(st.session_state.quiz_filters['week_ids'])
            
            if st.session_state.quiz_filters['difficulty_ids']:
                difficulty_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['difficulty_ids'])
                conditions.append(f"q.difficulty_id IN ({difficulty_ids_str})")
                params.extend(st.session_state.quiz_filters['difficulty_ids'])
            
            if st.session_state.quiz_filters['module_ids']:
                module_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['module_ids'])
                conditions.append(f"q.module_id IN ({module_ids_str})")
                params.extend(st.session_state.quiz_filters['module_ids'])
            
            if st.session_state.quiz_filters['tag_ids']:
                query += " LEFT JOIN question_tags qt ON q.question_id = qt.question_id"
                tag_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['tag_ids'])
                conditions.append(f"qt.tag_id IN ({tag_ids_str})")
                params.extend(st.session_state.quiz_filters['tag_ids'])
            
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
            
            cursor.execute(query, params)
            result = cursor.fetchone()
            question_count = result['count'] if result else 0
            
            # Display available questions count
            st.info(f"Total available questions with selected filters: {question_count}")
            
            # Quiz size selection
            if question_count > 0:
                max_questions = min(question_count, 120)  # Limit to 120 questions max to match real CFA exam format
                quiz_size = st.slider(
                    "Number of Questions",
                    min_value=1,
                    max_value=max_questions,
                    value=min(10, max_questions),
                    help="Select how many questions you want in your quiz"
                )
                
                # Store quiz size in session state
                st.session_state.quiz_size = quiz_size
                
                # Start quiz button
                if st.button("Start Quiz", type="primary", key="create_quiz_start_button"):
                    # Generate the query to get filtered questions
                    query = "SELECT q.question_id FROM questions q"
                    conditions = []
                    params = []
                    
                    # Only add filter conditions if specific options are selected (not 'All')
                    if st.session_state.quiz_filters['topic_ids']:
                        topic_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['topic_ids'])
                        conditions.append(f"q.topic_id IN ({topic_ids_str})")
                        params.extend(st.session_state.quiz_filters['topic_ids'])
                    
                    if st.session_state.quiz_filters['week_ids']:
                        week_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['week_ids'])
                        conditions.append(f"q.week_id IN ({week_ids_str})")
                        params.extend(st.session_state.quiz_filters['week_ids'])
                    
                    if st.session_state.quiz_filters['difficulty_ids']:
                        difficulty_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['difficulty_ids'])
                        conditions.append(f"q.difficulty_id IN ({difficulty_ids_str})")
                        params.extend(st.session_state.quiz_filters['difficulty_ids'])
                    
                    if st.session_state.quiz_filters['module_ids']:
                        module_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['module_ids'])
                        conditions.append(f"q.module_id IN ({module_ids_str})")
                        params.extend(st.session_state.quiz_filters['module_ids'])
                    
                    if st.session_state.quiz_filters['tag_ids']:
                        query += " LEFT JOIN question_tags qt ON q.question_id = qt.question_id"
                        tag_ids_str = ','.join('%s' for _ in st.session_state.quiz_filters['tag_ids'])
                        conditions.append(f"qt.tag_id IN ({tag_ids_str})")
                        params.extend(st.session_state.quiz_filters['tag_ids'])
                    
                    if conditions:
                        query += " WHERE " + " AND ".join(conditions)
                    
                    query += " ORDER BY RANDOM() LIMIT %s"
                    params.append(quiz_size)
                    
                    cursor.execute(query, params)
                    question_ids = [row['question_id'] for row in cursor.fetchall()]
                    
                    if not question_ids:
                        st.warning("No questions found with the selected filters.")
                        st.stop()
                    
                    # Store quiz data in session state
                    st.session_state.quiz_started = True
                    st.session_state.question_ids = question_ids
                    st.session_state.current_question = 0
                    st.session_state.user_answers = {}
                    st.session_state.show_results = False
                    
                    # Set up timer - 90 seconds per question
                    st.session_state.total_time = len(question_ids) * 90  # in seconds
                    st.session_state.start_time = time.time()
                    
                    # Switch to quiz page
                    st.session_state.current_page = 'quiz'
                    st.rerun()
            else:
                st.warning("No questions available with the current selection.")
                st.info("Try selecting different filters or import more questions into the database.")
            
            # Navigation button
            col1, col2 = st.columns([1, 5])
            if col1.button("Previous: Modules", type="secondary"):
                st.session_state.quiz_wizard_step = 4
                st.rerun()
    
    elif st.session_state.current_page == 'quiz':
        # Quiz page
        st.title("CFA Level I Quiz")
        st.markdown("""
        Answer the questions below to test your knowledge.
        """)
        
        # Sidebar for quiz settings
        st.sidebar.header("Quiz Settings")
    
    # Get all topics
    topics = get_topics(conn)
    topic_options = {topic['name']: topic['topic_id'] for topic in topics}
    
    # Check if we have topics
    if not topic_options:
        st.error("No topics found in the database. Please import questions first.")
        st.stop()
    
    # Get all weeks
    cursor = conn.cursor()
    cursor.execute("SELECT week_id, week_number FROM weeks ORDER BY week_number")
    weeks = cursor.fetchall()
    week_options = {f"Week {week['week_number']}": week['week_id'] for week in weeks}
    
    # Only show filter options on quiz-related pages
    if st.session_state.current_page not in ['dashboard', 'load_questions']:
        # Selection mode
        selection_mode = st.sidebar.radio(
            "Filter questions by:",
            options=["Topic", "Week", "Both"],
            index=0
        )
        
        selected_topic_ids = []
        selected_week_ids = []
    else:
        # Default selection mode when on dashboard (won't be used)
        selection_mode = "Topic"
        selected_topic_ids = []
        selected_week_ids = []
    
    # Topic selection - only show on quiz-related pages
    if st.session_state.current_page not in ['dashboard', 'load_questions'] and selection_mode in ["Topic", "Both"]:
        # Add 'All' option
        topic_options_with_all = {"All": "all"} | topic_options
        
        if len(topic_options) == 1:
            # If there's only one topic, select it by default
            only_topic = list(topic_options.keys())[0]
            st.sidebar.info(f"Currently only one topic is available: {only_topic}")
            selected_topic_names = [only_topic]
        else:
            selected_topic_names = st.sidebar.multiselect(
                "Select Topics",
                options=list(topic_options_with_all.keys()),
                default=["All"],
                help="Choose one or more topics for your quiz",
                key="take_quiz_topics"
            )
    else:
        # Default when on dashboard or not in Topic/Both mode
        selected_topic_names = []
    
    # Get selected topic IDs
    if "All" in selected_topic_names:
        # If 'All' is selected, don't filter by topic
        selected_topic_ids = []
    else:
        selected_topic_ids = [topic_options[name] for name in selected_topic_names if name in topic_options]
    
    # Week selection - only show on quiz-related pages
    if st.session_state.current_page not in ['dashboard', 'load_questions'] and selection_mode in ["Week", "Both"]:
        # Add 'All' option
        week_options_with_all = {"All": "all"} | week_options
        
        if len(week_options) == 1:
            # If there's only one week, select it by default
            only_week = list(week_options.keys())[0]
            st.sidebar.info(f"Currently only {only_week} is available")
            selected_week_names = [only_week]
        else:
            selected_week_names = st.sidebar.multiselect(
                "Select Weeks",
                options=list(week_options_with_all.keys()),
                default=["All"],
                help="Choose one or more weeks for your quiz",
                key="take_quiz_weeks"
            )
    else:
        # Default when on dashboard or not in Week/Both mode
        selected_week_names = []
    
    # Get selected week IDs
    if "All" in selected_week_names:
        # If 'All' is selected, don't filter by week
        selected_week_ids = []
    else:
        selected_week_ids = [week_options[name] for name in selected_week_names if name in week_options]
    
    # Show available questions count based on selection mode
    has_selection = False
    question_count = 0
    if selection_mode == "Topic" and selected_topic_ids:
        has_selection = True
        question_count = get_question_count(conn, topic_ids=selected_topic_ids)
        st.sidebar.info(f"Total available questions: {question_count}")
    elif selection_mode == "Week" and selected_week_ids:
        has_selection = True
        question_count = get_question_count(conn, week_ids=selected_week_ids)
        st.sidebar.info(f"Total available questions: {question_count}")
    elif selection_mode == "Both" and (selected_topic_ids or selected_week_ids):
        has_selection = True
        question_count = get_question_count(conn, topic_ids=selected_topic_ids, week_ids=selected_week_ids)
        st.sidebar.info(f"Total available questions: {question_count}")
    elif selection_mode == "Topic" and len(selected_topic_names) > 0 and "All" in selected_topic_names:
        has_selection = True
        question_count = get_question_count(conn, topic_ids=list(topic_options.values()))
        st.sidebar.info(f"Total available questions: {question_count}")
    elif selection_mode == "Week" and len(selected_week_names) > 0 and "All" in selected_week_names:
        has_selection = True
        question_count = get_question_count(conn, week_ids=list(week_options.values()))
        st.sidebar.info(f"Total available questions: {question_count}")
    elif selection_mode == "Both" and ((len(selected_topic_names) > 0 and "All" in selected_topic_names) or (len(selected_week_names) > 0 and "All" in selected_week_names)):
        has_selection = True
        topic_ids = list(topic_options.values()) if "All" in selected_topic_names else selected_topic_ids
        week_ids = list(week_options.values()) if "All" in selected_week_names else selected_week_ids
        question_count = get_question_count(conn, topic_ids=topic_ids, week_ids=week_ids)
        st.sidebar.info(f"Total available questions: {question_count}")
    
    # Debug mode can be enabled for troubleshooting if needed
    debug_mode = False  # Set to True only when debugging is needed
    if debug_mode and not has_selection:
        st.sidebar.warning("Debug: No selection detected")
        st.sidebar.write(f"Selection mode: {selection_mode}")
        st.sidebar.write(f"Topic names: {selected_topic_names}")
        st.sidebar.write(f"Week names: {selected_week_names}")
    
    if has_selection and question_count > 0:
        # Quiz size selection
        max_questions = min(question_count, 50)  # Limit to 50 questions max
        quiz_size = st.sidebar.slider(
            "Number of Questions",
            min_value=1,
            max_value=max_questions,
            value=min(10, max_questions),
            help="Select how many questions you want in your quiz"
        )
        
        # Start quiz button
        start_quiz = st.sidebar.button("Start Quiz", type="primary", key="sidebar_start_quiz_button_")
        
        if start_quiz:
            # Get random questions based on selected filters
            if selection_mode == "Topic":
                # Handle 'All' selection
                if "All" in selected_topic_names:
                    question_ids = get_filtered_questions(conn, topic_ids=list(topic_options.values()), limit=quiz_size)
                else:
                    question_ids = get_filtered_questions(conn, topic_ids=selected_topic_ids, limit=quiz_size)
            elif selection_mode == "Week":
                # Handle 'All' selection
                if "All" in selected_week_names:
                    question_ids = get_filtered_questions(conn, week_ids=list(week_options.values()), limit=quiz_size)
                else:
                    question_ids = get_filtered_questions(conn, week_ids=selected_week_ids, limit=quiz_size)
            else:  # Both
                # Handle 'All' selection for both topics and weeks
                topic_ids = list(topic_options.values()) if "All" in selected_topic_names else selected_topic_ids
                week_ids = list(week_options.values()) if "All" in selected_week_names else selected_week_ids
                question_ids = get_filtered_questions(conn, topic_ids=topic_ids, week_ids=week_ids, limit=quiz_size)
            
            if not question_ids:
                st.warning("No questions found with the selected filters.")
                st.stop()
            
            # Store quiz data in session state
            st.session_state.quiz_started = True
            st.session_state.question_ids = question_ids
            st.session_state.current_question = 0
            st.session_state.user_answers = {}
            st.session_state.show_results = False
            
            # Set up timer - 90 seconds per question
            st.session_state.total_time = len(question_ids) * 90  # in seconds
            st.session_state.start_time = time.time()
            
            # Switch to quiz page
            st.session_state.current_page = 'quiz'
            st.rerun()
    elif not has_selection:
        if selection_mode == "Topic":
            st.info("👈 Please select at least one topic from the sidebar to start.")
        elif selection_mode == "Week":
            st.info("👈 Please select at least one week from the sidebar to start.")
        else:
            st.info("👈 Please select at least one topic or week from the sidebar to start.")
    else:
        st.warning("No questions available with the current selection.")
        st.info("Currently, only ethics questions from Week 3 have been imported into the database.")
        st.info("More questions will be available as they are imported from the question bank.")
    
    # Quiz display
    if 'quiz_started' in st.session_state and st.session_state.quiz_started:
        if not st.session_state.show_results:
            # Display current question
            current_idx = st.session_state.current_question
            total_questions = len(st.session_state.question_ids)
            
            # Progress bar
            st.progress(current_idx / total_questions)
            
            # Timer display
            elapsed_time = int(time.time() - st.session_state.start_time)
            remaining_time = max(0, st.session_state.total_time - elapsed_time)
            minutes, seconds = divmod(remaining_time, 60)
            
            # Display question number
            st.write(f"Question {current_idx + 1} of {total_questions}")
            
            # Create a clickable timer button that updates when clicked and an exit button
            timer_col, exit_col = st.columns([2, 1])
            
            with timer_col:
                timer_color = "red" if remaining_time < 30 else "black"
                timer_label = f"⏱️ {minutes}:{seconds:02d}"
                
                # Make the timer clickable to refresh
                if st.button(timer_label, key="timer_button", help="Click to update timer"):
                    # This will trigger a rerun when clicked
                    pass
                
                # Add a note about clicking to update
                st.caption("Click timer to update")
            
            with exit_col:
                if st.button("Exit Quiz", key="exit_quiz_button", type="secondary"):
                    # Exit the quiz and return to dashboard
                    st.session_state.current_page = 'dashboard'
                    # Clear quiz state
                    for key in ['quiz_started', 'question_ids', 'current_question', 
                               'user_answers', 'show_results']:
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()
                
            # Auto-submit if time runs out
            if remaining_time <= 0 and not st.session_state.show_results:
                st.session_state.show_results = True
                st.warning("Time's up! Your quiz has been automatically submitted.")
                # Timer has ended
                st.rerun()
            
            # Get current question details
            question_id = st.session_state.question_ids[current_idx]
            question_data = get_question_details(conn, question_id)
            
            if question_data:
                # Display question
                st.subheader(question_data['question']['title'])
                st.write(question_data['question']['question_text'])
                
                # Display options and get user answer
                user_answer = None
                for option in question_data['options']:
                    option_key = f"q{question_id}_{option['option_letter']}"
                    if st.button(
                        f"{option['option_letter']}) {option['option_text']}",
                        key=option_key
                    ):
                        user_answer = option['option_letter']
                
                # Store user answer if provided
                if user_answer:
                    st.session_state.user_answers[question_id] = {
                        'user_answer': user_answer,
                        'correct_answer': next(
                            opt['option_letter'] for opt in question_data['options'] 
                            if opt['is_correct']
                        ),
                        'explanation': question_data['explanation']
                    }
                    
                    # Move to next question or show results
                    if current_idx < total_questions - 1:
                        st.session_state.current_question += 1
                        st.rerun()
                    else:
                        st.session_state.show_results = True
                        st.rerun()
                
                # Navigation buttons
                col1, col2 = st.columns(2)
                
                if current_idx > 0:
                    if col1.button("Previous Question"):
                        st.session_state.current_question -= 1
                        st.rerun()
                
                if current_idx < total_questions - 1:
                    if col2.button("Skip Question"):
                        st.session_state.current_question += 1
                        st.rerun()
                else:
                    if col2.button("Finish Quiz"):
                        st.session_state.show_results = True
                        st.rerun()
            
        else:
            # Show quiz results
            st.header("Quiz Results")
            
            # Calculate score
            total_questions = len(st.session_state.question_ids)
            answered_questions = len(st.session_state.user_answers)
            correct_answers = sum(
                1 for q_id, data in st.session_state.user_answers.items()
                if data['user_answer'] == data['correct_answer']
            )
            
            # Calculate time taken
            time_taken_seconds = 0
            if 'start_time' in st.session_state:
                time_taken_seconds = int(time.time() - st.session_state.start_time)
                minutes, seconds = divmod(time_taken_seconds, 60)
                time_info = f"Time taken: {minutes} minutes and {seconds} seconds"
            else:
                time_info = ""
            
            # Display score and time taken
            score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
            st.subheader(f"Your Score: {correct_answers}/{total_questions} ({score_percentage:.1f}%)")
            if time_info:
                st.write(time_info)
                
            # Save quiz results to Firestore if user is logged in
            if 'user' in st.session_state:
                user_uid = st.session_state.user.get('localId')
                
                # Format question results for Firestore
                question_results = {}
                for q_id, data in st.session_state.user_answers.items():
                    question_results[q_id] = {
                        'user_answer': data['user_answer'],
                        'correct_answer': data['correct_answer'],
                        'is_correct': data['user_answer'] == data['correct_answer']
                    }
                
                # Save results
                topic_ids = st.session_state.get('selected_topics', [])
                week_ids = st.session_state.get('selected_weeks', [])
                saved = user_stats.save_quiz_results(
                    user_uid, 
                    topic_ids, 
                    week_ids, 
                    question_results, 
                    time_taken_seconds
                )
                
                if saved:
                    # Check for new badges
                    new_badges = user_stats.check_and_award_badges(user_uid)
                    if new_badges:
                        badge_details = user_stats.get_badge_details()
                        st.success(f"🎉 Congratulations! You've earned {len(new_badges)} new badge(s)!")
                        for badge_id in new_badges:
                            badge = badge_details.get(badge_id, {'name': badge_id, 'description': '', 'icon': '🏆'})
                            st.markdown(f"{badge['icon']} **{badge['name']}**: {badge['description']}")
            
            # Results breakdown
            st.write("### Question Review")
            
            for i, q_id in enumerate(st.session_state.question_ids):
                question_data = get_question_details(conn, q_id)
                
                with st.expander(f"Question {i+1}: {question_data['question']['title']}"):
                    st.write(question_data['question']['question_text'])
                    
                    # Show options with correct/incorrect highlighting
                    for option in question_data['options']:
                        if q_id in st.session_state.user_answers:
                            user_answer = st.session_state.user_answers[q_id]['user_answer']
                            is_correct = option['is_correct']
                            
                            if option['option_letter'] == user_answer:
                                if is_correct:
                                    st.success(f"{option['option_letter']}) {option['option_text']} ✓")
                                else:
                                    st.error(f"{option['option_letter']}) {option['option_text']} ✗")
                            elif is_correct:
                                st.info(f"{option['option_letter']}) {option['option_text']} (Correct Answer)")
                            else:
                                st.write(f"{option['option_letter']}) {option['option_text']}")
                        else:
                            # Question was skipped
                            if option['is_correct']:
                                st.info(f"{option['option_letter']}) {option['option_text']} (Correct Answer)")
                            else:
                                st.write(f"{option['option_letter']}) {option['option_text']}")
                    
                    # Show explanation
                    if question_data['explanation']:
                        st.write("#### Explanation")
                        st.write(question_data['explanation'])
            
            # Restart quiz button
            if st.button("Start New Quiz", type="primary", key="restart_quiz_button"):
                for key in ['quiz_started', 'question_ids', 'current_question', 
                           'user_answers', 'show_results']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
    
    # Practice Question page
    elif st.session_state.current_page == 'practice_question':
        # Practice Question page
        st.title("CFA Level I Practice Questions")
        st.markdown("""
        Practice with individual questions and get immediate feedback after each answer.
        """)
        
        # Initialize practice question state if not exists
        if 'practice_question_answered' not in st.session_state:
            st.session_state.practice_question_answered = False
        if 'practice_current_question' not in st.session_state:
            st.session_state.practice_current_question = None
        if 'practice_user_answer' not in st.session_state:
            st.session_state.practice_user_answer = None
        
        # Get a new question button
        if not st.session_state.practice_question_answered:
            if st.button("Get a New Question", type="primary", key="get_practice_question"):
                # Get random question based on selected filters
                if selection_mode == "Topic":
                    # Handle 'All' selection
                    if "All" in selected_topic_names:
                        questions = get_filtered_questions(conn, topic_ids=list(topic_options.values()), limit=1)
                    else:
                        questions = get_filtered_questions(conn, topic_ids=selected_topic_ids, limit=1)
                elif selection_mode == "Week":
                    # Handle 'All' selection
                    if "All" in selected_week_names:
                        questions = get_filtered_questions(conn, week_ids=list(week_options.values()), limit=1)
                    else:
                        questions = get_filtered_questions(conn, week_ids=selected_week_ids, limit=1)
                else:  # Both
                    # Handle 'All' selection for topics
                    if "All" in selected_topic_names:
                        topic_ids_for_query = list(topic_options.values())
                    else:
                        topic_ids_for_query = selected_topic_ids
                    
                    # Handle 'All' selection for weeks
                    if "All" in selected_week_names:
                        week_ids_for_query = list(week_options.values())
                    else:
                        week_ids_for_query = selected_week_ids
                    
                    questions = get_filtered_questions(conn, topic_ids=topic_ids_for_query, week_ids=week_ids_for_query, limit=1)
                
                if questions:
                    st.session_state.practice_current_question = questions[0]
                    st.session_state.practice_question_answered = False
                    st.session_state.practice_user_answer = None
                    st.rerun()
                else:
                    st.warning("No questions found with the selected filters.")
        
        # Display the question if available
        if st.session_state.practice_current_question:
            question_id = st.session_state.practice_current_question
            question_data = get_question_details(conn, question_id)
            
            if question_data:
                # Display question
                st.subheader(question_data['question']['title'])
                st.write(question_data['question']['question_text'])
                
                # Display options and get user answer if not answered yet
                if not st.session_state.practice_question_answered:
                    for option in question_data['options']:
                        option_key = f"practice_q{question_id}_{option['option_letter']}"
                        if st.button(
                            f"{option['option_letter']}) {option['option_text']}",
                            key=option_key
                        ):
                            st.session_state.practice_user_answer = option['option_letter']
                            st.session_state.practice_question_answered = True
                            
                            # Save the practice attempt to user stats if logged in
                            if 'user' in st.session_state:
                                user_uid = st.session_state.user.get('localId')
                                correct_answer = next(
                                    opt['option_letter'] for opt in question_data['options'] 
                                    if opt['is_correct']
                                )
                                
                                # Format question result for Firestore
                                question_results = {
                                    question_id: {
                                        'user_answer': st.session_state.practice_user_answer,
                                        'correct_answer': correct_answer,
                                        'is_correct': st.session_state.practice_user_answer == correct_answer
                                    }
                                }
                                
                                # Save result
                                topic_ids = selected_topic_ids if selected_topic_ids else []
                                week_ids = selected_week_ids if selected_week_ids else []
                                user_stats.save_quiz_results(
                                    user_uid, 
                                    topic_ids, 
                                    week_ids, 
                                    question_results, 
                                    0  # No time tracking for practice questions
                                )
                                
                                # Check for new badges
                                new_badges = user_stats.check_and_award_badges(user_uid)
                                if new_badges:
                                    badge_details = user_stats.get_badge_details()
                                    st.success(f"🎉 Congratulations! You've earned {len(new_badges)} new badge(s)!")
                                    for badge_id in new_badges:
                                        badge = badge_details.get(badge_id, {'name': badge_id, 'description': '', 'icon': '🏆'})
                                        st.markdown(f"{badge['icon']} **{badge['name']}**: {badge['description']}")
                            
                            st.rerun()
                else:
                    # Show feedback after answering
                    user_answer = st.session_state.practice_user_answer
                    correct_answer = next(
                        opt['option_letter'] for opt in question_data['options'] 
                        if opt['is_correct']
                    )
                    
                    # Display options with correct/incorrect highlighting
                    for option in question_data['options']:
                        if option['option_letter'] == user_answer:
                            if option['is_correct']:
                                st.success(f"{option['option_letter']}) {option['option_text']} ✓")
                            else:
                                st.error(f"{option['option_letter']}) {option['option_text']} ✗")
                        elif option['is_correct']:
                            st.info(f"{option['option_letter']}) {option['option_text']} (Correct Answer)")
                        else:
                            st.write(f"{option['option_letter']}) {option['option_text']}")
                    
                    # Show explanation
                    if question_data['explanation']:
                        st.write("#### Explanation")
                        st.write(question_data['explanation'])
                    
                    # Next question button
                    if st.button("Next Question", type="primary"):
                        st.session_state.practice_question_answered = False
                        st.session_state.practice_current_question = None
                        st.session_state.practice_user_answer = None
                        st.rerun()
            
        # If no question is available yet, show a message
        if not st.session_state.practice_current_question and not st.session_state.practice_question_answered:
            st.info("Select your filters in the sidebar and click 'Get a New Question' to start practicing.")
    
    # Note: Dashboard tab is already handled in the dashboard page section
    
    # Close database connection if it exists
    if 'conn' in locals() and conn is not None:
        conn.close()

if __name__ == "__main__":
    main()
