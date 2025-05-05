#!/usr/bin/env python3

"""
Streamlit Quiz App for CFA Level I Exam Questions
"""

import streamlit as st
import sqlite3
import os
import random
from pathlib import Path
import firebase_auth

# Set page configuration
st.set_page_config(
    page_title="CFA Level I Quiz App",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Database connection function
def connect_to_db(db_path):
    """Connect to SQLite database"""
    if not os.path.exists(db_path):
        st.error(f"Error: Database file {db_path} not found")
        return None
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # This enables column access by name
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
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
        topic_ids_str = ','.join('?' for _ in topic_ids)
        query = f"SELECT COUNT(DISTINCT question_id) as count FROM questions WHERE topic_id IN ({topic_ids_str})"
        cursor.execute(query, topic_ids)
        result = cursor.fetchone()
        return result['count'] if result else 0
    
    # Standard filtering with AND logic for other cases
    conditions = []
    params = []
    
    if topic_ids:
        topic_ids_str = ','.join('?' for _ in topic_ids)
        conditions.append(f"topic_id IN ({topic_ids_str})")
        params.extend(topic_ids)
    
    if week_ids:
        week_ids_str = ','.join('?' for _ in week_ids)
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
        topic_ids_str = ','.join('?' for _ in topic_ids)
        conditions.append(f"q.topic_id IN ({topic_ids_str})")
        params.extend(topic_ids)
    
    if week_ids:
        week_ids_str = ','.join('?' for _ in week_ids)
        conditions.append(f"q.week_id IN ({week_ids_str})")
        params.extend(week_ids)
    
    if not conditions:
        return []
    
    query = "SELECT q.question_id FROM questions q"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    
    if limit:
        query += " ORDER BY RANDOM() LIMIT ?"
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
        WHERE q.question_id = ?
    """, (question_id,))
    question = cursor.fetchone()
    
    if not question:
        return None
    
    # Get answer options
    cursor.execute("""
        SELECT option_letter, option_text, is_correct
        FROM answer_options
        WHERE question_id = ?
        ORDER BY option_letter
    """, (question_id,))
    options = cursor.fetchall()
    
    # Get explanation
    cursor.execute("""
        SELECT explanation_text
        FROM explanations
        WHERE question_id = ?
    """, (question_id,))
    explanation = cursor.fetchone()
    
    # Get tags
    cursor.execute("""
        SELECT t.name
        FROM tags t
        JOIN question_tags qt ON t.tag_id = qt.tag_id
        WHERE qt.question_id = ?
    """, (question_id,))
    tags = cursor.fetchall()
    
    return {
        'question': dict(question),
        'options': [dict(option) for option in options],
        'explanation': explanation['explanation_text'] if explanation else None,
        'tags': [tag['name'] for tag in tags]
    }

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
    
    # Database path
    db_path = Path(__file__).parent / "database" / "cfa_questions.db"
    
    # Connect to the database
    conn = connect_to_db(db_path)
    if not conn:
        st.stop()
    
    # Login/Signup screen if not authenticated
    if not st.session_state.authenticated:
        st.title("CFA Level I Quiz App")
        
        # Tabs for login and signup
        login_tab, signup_tab = st.tabs(["Login", "Sign Up"])
        
        # Login tab
        with login_tab:
            with st.form("login_form"):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit_button = st.form_submit_button("Login")
                
                if submit_button:
                    if email and password:
                        # Use Firebase authentication
                        result = firebase_auth.login(email, password)
                        
                        if result['success']:
                            st.session_state.authenticated = True
                            st.session_state.user = result['user']
                            st.session_state.username = firebase_auth.get_user_display_name(result['user'])
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
    
    # Sidebar navigation and logout
    st.sidebar.title("Navigation")
    
    # Logout button in sidebar
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.username = ""
        st.session_state.current_page = 'dashboard'  # Reset to dashboard for next login
        st.rerun()
    
    # Navigation buttons
    if st.sidebar.button("Dashboard", type="primary" if st.session_state.current_page == 'dashboard' else "secondary"):
        st.session_state.current_page = 'dashboard'
        st.rerun()
        
    if st.sidebar.button("Take Quiz", type="primary" if st.session_state.current_page == 'quiz' else "secondary"):
        st.session_state.current_page = 'quiz'
        st.rerun()
        
    if st.sidebar.button("Load Questions", type="primary" if st.session_state.current_page == 'load_questions' else "secondary"):
        st.session_state.current_page = 'load_questions'
        st.rerun()
    
    # Import the necessary modules for question import functionality
    import sys
    import tempfile
    import os
    from importlib.util import spec_from_file_location, module_from_spec
    
    # Import the import_to_sqlite module dynamically
    def import_module_from_path(module_name, file_path):
        spec = spec_from_file_location(module_name, file_path)
        module = module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    
    # Path to the import_to_sqlite.py file
    import_script_path = Path(__file__).parent / "database" / "import_to_sqlite.py"
    
    # Display the selected page
    if st.session_state.current_page == 'dashboard':
        # Dashboard page
        st.title("CFA Level I Study Dashboard")
        st.markdown(f"Welcome, {st.session_state.username}! 👋")
        
        # Dashboard content
        st.markdown("""
        ### Your CFA Level I Study Portal
        
        This dashboard provides access to study resources and practice quizzes for your CFA Level I exam preparation.
        
        #### Available Features:
        - **Practice Quizzes**: Test your knowledge with topic-specific quizzes
        - **Load Questions**: Upload question files to expand your question bank
        - **Performance Tracking**: Monitor your progress (coming soon)
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
            st.metric(label="Your Quizzes Taken", value="0")
        
        # Call to action
        st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
            <h3>Ready to test your knowledge?</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start a Quiz", type="primary", use_container_width=True):
                st.session_state.current_page = 'quiz'
                st.rerun()
        with col2:
            if st.button("Load Questions", type="secondary", use_container_width=True):
                st.session_state.current_page = 'load_questions'
                st.rerun()
    
    elif st.session_state.current_page == 'load_questions':
        # Load Questions page
        st.title("Load Questions")
        st.markdown("""
        Upload markdown files containing CFA Level I questions to add them to your question bank.
        
        The file should follow the standard question format with metadata, question text, options, and explanations.
        """)
        
        # File uploader
        uploaded_file = st.file_uploader("Choose a markdown file", type=['md'])
        
        # Schema file selection
        schema_path = Path(__file__).parent / "database" / "sqlite_schema.sql"
        db_path = Path(__file__).parent / "database" / "cfa_questions.db"
        
        if uploaded_file is not None:
            # Create a temporary file to save the uploaded content
            with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                temp_path = tmp_file.name
            
            # Show the import options
            st.subheader("Import Options")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Preview File", use_container_width=True):
                    with open(temp_path, 'r') as f:
                        file_content = f.read()
                    st.text_area("File Content Preview", file_content, height=300)
            
            with col2:
                if st.button("Import Questions", type="primary", use_container_width=True):
                    try:
                        # Import the module
                        import_module = import_module_from_path("import_to_sqlite", str(import_script_path))
                        
                        # Use functions from the imported module
                        with st.spinner("Importing questions..."):
                            # Create or connect to the database
                            conn = import_module.create_database(str(db_path), str(schema_path))
                            
                            # Parse the questions from the file
                            questions = import_module.parse_question_file(temp_path)
                            
                            # Import the questions to the database
                            import_module.import_questions_to_db(questions, conn)
                            
                            # Close the connection
                            conn.close()
                        
                        # Success message
                        st.success(f"Successfully imported {len(questions)} questions!")
                        
                        # Update connection for the main app
                        conn = connect_to_db(db_path)
                    except Exception as e:
                        st.error(f"Error importing questions: {str(e)}")
            
            # Clean up the temporary file
            st.markdown("""
            #### File Format Requirements
            
            The markdown file should follow this structure:
            - Question title as a heading (##)
            - Metadata section in a details/summary HTML element
            - Question text and options (with A), B), C) format)
            - Answer and explanation in a details/summary HTML element
            - Questions separated by horizontal rules (---)
            """)
    
    elif st.session_state.current_page == 'quiz':
        # Quiz page
        st.title("CFA Level I Quiz")
        st.markdown("""
        Select the topics you're interested in and create a customized quiz.
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
    
    # Selection mode
    selection_mode = st.sidebar.radio(
        "Filter questions by:",
        options=["Topic", "Week", "Both"],
        index=0
    )
    
    selected_topic_ids = []
    selected_week_ids = []
    
    # Topic selection
    if selection_mode in ["Topic", "Both"]:
        if len(topic_options) == 1:
            # If there's only one topic, select it by default
            only_topic = list(topic_options.keys())[0]
            st.sidebar.info(f"Currently only one topic is available: {only_topic}")
            selected_topic_names = [only_topic]
        else:
            selected_topic_names = st.sidebar.multiselect(
                "Select Topics",
                options=list(topic_options.keys()),
                help="Choose one or more topics for your quiz"
            )
        
        # Get selected topic IDs
        selected_topic_ids = [topic_options[name] for name in selected_topic_names]
    
    # Week selection
    if selection_mode in ["Week", "Both"]:
        if len(week_options) == 1:
            # If there's only one week, select it by default
            only_week = list(week_options.keys())[0]
            st.sidebar.info(f"Currently only {only_week} is available")
            selected_week_names = [only_week]
        else:
            selected_week_names = st.sidebar.multiselect(
                "Select Weeks",
                options=list(week_options.keys()),
                help="Choose one or more weeks for your quiz"
            )
        
        # Get selected week IDs
        selected_week_ids = [week_options[name] for name in selected_week_names]
    
    # Show available questions count based on selection mode
    has_selection = False
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
        start_quiz = st.sidebar.button("Start Quiz", type="primary")
        
        if start_quiz:
            # Get random questions based on selected filters
            if selection_mode == "Topic":
                question_ids = get_filtered_questions(conn, topic_ids=selected_topic_ids, limit=quiz_size)
            elif selection_mode == "Week":
                question_ids = get_filtered_questions(conn, week_ids=selected_week_ids, limit=quiz_size)
            else:  # Both
                question_ids = get_filtered_questions(conn, topic_ids=selected_topic_ids, week_ids=selected_week_ids, limit=quiz_size)
            
            if not question_ids:
                st.warning("No questions found with the selected filters.")
                st.stop()
            
            # Store quiz data in session state
            st.session_state.quiz_started = True
            st.session_state.question_ids = question_ids
            st.session_state.current_question = 0
            st.session_state.user_answers = {}
            st.session_state.show_results = False
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
            st.write(f"Question {current_idx + 1} of {total_questions}")
            
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
            
            # Display score
            score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
            st.subheader(f"Your Score: {correct_answers}/{total_questions} ({score_percentage:.1f}%)")
            
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
            if st.button("Start New Quiz", type="primary"):
                for key in ['quiz_started', 'question_ids', 'current_question', 
                           'user_answers', 'show_results']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
    
    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
