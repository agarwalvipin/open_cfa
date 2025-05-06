#!/usr/bin/env python3

"""
Admin Dashboard for CFA Level I Quiz App
"""

import streamlit as st
import firebase_auth
import role_management
import user_stats
import os
import pandas as pd
from pathlib import Path
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

# Only set page config when running this file directly, not when imported
if __name__ == "__main__":
    # Set page configuration
    st.set_page_config(
        page_title="Admin Dashboard - CFA Level I Quiz App",
        page_icon="🔑",
        layout="wide",
        initial_sidebar_state="expanded",
    )

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

def get_system_stats(conn):
    """Get system-wide statistics"""
    stats = {}
    
    # Get total questions count
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as count FROM questions")
    result = cursor.fetchone()
    stats['total_questions'] = result['count'] if result else 0
    
    # Get questions by topic
    cursor.execute("""
        SELECT t.name as topic, COUNT(q.question_id) as count 
        FROM questions q
        JOIN topics t ON q.topic_id = t.topic_id
        GROUP BY t.name
        ORDER BY count DESC
    """)
    stats['questions_by_topic'] = cursor.fetchall()
    
    # Get questions by week
    cursor.execute("""
        SELECT w.week_number as week, COUNT(q.question_id) as count 
        FROM questions q
        JOIN weeks w ON q.week_id = w.week_id
        GROUP BY w.week_number
        ORDER BY w.week_number
    """)
    stats['questions_by_week'] = cursor.fetchall()
    
    # Get questions by difficulty
    cursor.execute("""
        SELECT d.name as difficulty, d.difficulty_id, COUNT(q.question_id) as count 
        FROM questions q
        JOIN difficulty_levels d ON q.difficulty_id = d.difficulty_id
        GROUP BY d.name, d.difficulty_id
        ORDER BY d.difficulty_id
    """)
    stats['questions_by_difficulty'] = cursor.fetchall()
    
    return stats

def cleanup_questions(conn, topic_id=None, week_id=None, confirm=False):
    """Clean up questions and related data based on filters"""
    if not confirm:
        return "Confirmation required for cleanup operation", False
    
    cursor = conn.cursor()
    
    try:
        # Start a transaction
        cursor.execute("BEGIN")
        
        # Build the WHERE clause based on filters
        where_clause = ""
        params = []
        
        if topic_id:
            where_clause += " topic_id = %s"
            params.append(topic_id)
        
        if week_id:
            if where_clause:
                where_clause += " AND"
            where_clause += " week_id = %s"
            params.append(week_id)
        
        # If no filters are provided, require explicit confirmation
        if not where_clause and not confirm:
            return "Confirmation required for full database cleanup", False
        
        # Prepare the final WHERE clause
        if where_clause:
            where_clause = " WHERE" + where_clause
        
        # Get the list of question IDs to be deleted
        query = f"SELECT question_id FROM questions{where_clause}"
        cursor.execute(query, params)
        question_ids = [row['question_id'] for row in cursor.fetchall()]
        
        if not question_ids:
            return "No questions found matching the criteria", False
        
        # Delete related data first (foreign key constraints)
        # Note: SQLite with ON DELETE CASCADE should handle this automatically,
        # but we're being explicit for safety
        
        # Delete from question_tags
        placeholders = ','.join(['%s'] * len(question_ids))
        cursor.execute(f"DELETE FROM question_tags WHERE question_id IN ({placeholders})", question_ids)
        tags_deleted = cursor.rowcount
        
        # Delete from explanations
        cursor.execute(f"DELETE FROM explanations WHERE question_id IN ({placeholders})", question_ids)
        explanations_deleted = cursor.rowcount
        
        # Delete from answer_options
        cursor.execute(f"DELETE FROM answer_options WHERE question_id IN ({placeholders})", question_ids)
        options_deleted = cursor.rowcount
        
        # Finally delete the questions
        cursor.execute(f"DELETE FROM questions{where_clause}", params)
        questions_deleted = cursor.rowcount
        
        # Commit the transaction
        conn.commit()
        
        # Return success message with counts
        return f"Successfully deleted {questions_deleted} questions, {options_deleted} answer options, {explanations_deleted} explanations, and {tags_deleted} question tags.", True
        
    except Exception as e:
        # Rollback in case of error
        conn.rollback()
        return f"Error during cleanup: {str(e)}", False

def get_user_activity_stats():
    """Get user activity statistics from Firestore"""
    try:
        db = user_stats.initialize_firestore()
        
        # Get total user count
        users_ref = db.collection('user_stats')
        users = users_ref.stream()
        user_count = sum(1 for _ in users)
        
        # Get recent quiz attempts
        quiz_ref = db.collection('quiz_attempts').order_by('date', direction='DESCENDING').limit(50)
        quizzes = quiz_ref.stream()
        
        quiz_data = []
        for quiz in quizzes:
            data = quiz.to_dict()
            quiz_data.append({
                'user_uid': data.get('user_uid', 'unknown'),
                'date': data.get('date'),
                'score': data.get('score', 0),
                'num_questions': data.get('num_questions', 0),
                'time_taken_seconds': data.get('time_taken_seconds', 0)
            })
        
        return {
            'user_count': user_count,
            'recent_quizzes': quiz_data
        }
    except Exception as e:
        st.error(f"Error getting user activity stats: {e}")
        return {
            'user_count': 0,
            'recent_quizzes': []
        }

def main():
    # Check if user is logged in
    if 'user_uid' not in st.session_state:
        st.warning("Please log in to access this page.")
        if st.button("Go to Login Page"):
            import subprocess
            import sys
            import os
            # Launch the main app
            subprocess.Popen([sys.executable, '-m', 'streamlit', 'run', 'quiz_app.py'], 
                             cwd=os.path.dirname(os.path.abspath(__file__)))
            st.stop()
        return
    
    user_uid = st.session_state['user_uid']
    
    # Check if user has admin role
    if not role_management.check_user_access(user_uid, 'admin'):
        st.error("You do not have permission to access this page.")
        if st.button("Go to Home Page"):
            import subprocess
            import sys
            import os
            # Launch the main app
            subprocess.Popen([sys.executable, '-m', 'streamlit', 'run', 'quiz_app.py'], 
                             cwd=os.path.dirname(os.path.abspath(__file__)))
            st.stop()
        return
    
    # Display sidebar based on user role
    role_management.show_role_based_sidebar(user_uid)
    
    # Admin Dashboard
    st.title("Admin Dashboard")
    
    # Connect to PostgreSQL database
    conn = connect_to_db()
    # Database connection message removed

    
    if not conn:
        st.error("Could not connect to database. Please check the database file.")
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
        
        def clean_orphaned_data(connection):
            """Function to clean orphaned data from the database"""
            try:
                # Create a new cursor
                with connection.cursor() as curs:
                    # Start transaction
                    curs.execute("BEGIN")
                    
                    # Delete orphaned tags
                    curs.execute("""
                        DELETE FROM tags 
                        WHERE tag_id NOT IN (SELECT DISTINCT tag_id FROM question_tags)
                    """)
                    tags_deleted = curs.rowcount
                    
                    # Delete orphaned learning objectives
                    curs.execute("""
                        DELETE FROM learning_objectives 
                        WHERE los_id NOT IN (SELECT DISTINCT los_id FROM questions WHERE los_id IS NOT NULL)
                    """)
                    los_deleted = curs.rowcount
                    
                    # Delete orphaned modules
                    curs.execute("""
                        DELETE FROM modules 
                        WHERE module_id NOT IN (SELECT DISTINCT module_id FROM questions WHERE module_id IS NOT NULL)
                    """)
                    modules_deleted = curs.rowcount
                    
                    # Delete orphaned readings
                    curs.execute("""
                        DELETE FROM readings 
                        WHERE reading_id NOT IN (SELECT DISTINCT reading_id FROM questions WHERE reading_id IS NOT NULL)
                    """)
                    readings_deleted = curs.rowcount
                
                # Commit the transaction
                connection.commit()
                
                return True, tags_deleted, los_deleted, modules_deleted, readings_deleted
                
            except Exception as e:
                # Rollback the transaction
                connection.rollback()
                return False, str(e), 0, 0, 0
        
        if st.button("Clean Orphaned Data", type="secondary"):
            success, *results = clean_orphaned_data(conn)
            
            if success:
                tags_deleted, los_deleted, modules_deleted, readings_deleted = results
                st.success(f"Successfully cleaned up orphaned data: {tags_deleted} tags, {los_deleted} learning objectives, {modules_deleted} modules, and {readings_deleted} readings.")
            else:
                error_msg = results[0]
                st.error(f"Error cleaning orphaned data: {error_msg}")
    
    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
