#!/usr/bin/env python3

"""
Student Progress Page for CFA Level I Quiz App
"""

import streamlit as st
import firebase_auth
import role_management
import user_stats
import sqlite3
import os
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Student Progress - CFA Level I Quiz App",
    page_icon="📊",
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

def get_all_students():
    """Get all users with student role from Firebase Auth"""
    try:
        # Initialize Firebase Admin SDK
        firebase_auth.initialize_firebase_admin()
        
        # Get all users
        users = role_management.get_all_users(limit=500)
        
        # Filter to students only
        students = [user for user in users if user['role'] == 'student']
        
        return students
    except Exception as e:
        st.error(f"Error getting students: {e}")
        return []

def get_student_stats(students):
    """Get stats for all students"""
    student_stats = []
    
    for student in students:
        # Get user stats from Firestore
        stats = user_stats.get_user_stats(student['uid'])
        
        if stats:
            # Get quiz history
            quiz_history = user_stats.get_quiz_history(student['uid'], limit=100)
            
            # Calculate recent activity
            last_active = stats.get('last_active_date')
            if last_active:
                if isinstance(last_active, datetime):
                    days_since_active = (datetime.now() - last_active).days
                else:
                    # Handle timestamp format from Firestore
                    days_since_active = 999  # Default if can't parse
            else:
                days_since_active = 999
            
            # Get topic performance
            topic_performance = stats.get('topic_performance', {})
            weak_areas = stats.get('weak_areas', [])
            strong_areas = stats.get('strong_areas', [])
            
            student_stats.append({
                'uid': student['uid'],
                'email': student['email'],
                'displayName': student['displayName'],
                'total_quizzes': stats.get('total_quizzes_taken', 0),
                'total_questions': stats.get('total_questions_attempted', 0),
                'average_score': stats.get('average_score', 0),
                'days_since_active': days_since_active,
                'streak_days': stats.get('streak_days', 0),
                'topic_performance': topic_performance,
                'weak_areas': weak_areas,
                'strong_areas': strong_areas,
                'quiz_history': quiz_history
            })
        else:
            # No stats yet
            student_stats.append({
                'uid': student['uid'],
                'email': student['email'],
                'displayName': student['displayName'],
                'total_quizzes': 0,
                'total_questions': 0,
                'average_score': 0,
                'days_since_active': 999,
                'streak_days': 0,
                'topic_performance': {},
                'weak_areas': [],
                'strong_areas': [],
                'quiz_history': []
            })
    
    return student_stats

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
    
    # Check if user has instructor role or higher
    if not role_management.check_user_access(user_uid, 'instructor'):
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
    
    # Student Progress
    st.title("Student Progress")
    
    # Connect to database for topic names
    db_path = os.path.join(Path(__file__).parent, 'database', 'cfa_questions.db')
    conn = connect_to_db(db_path)
    
    if not conn:
        st.error("Could not connect to database. Please check the database file.")
        return
    
    # Get all students
    with st.spinner("Loading student data..."):
        students = get_all_students()
        
        if not students:
            st.warning("No students found.")
            conn.close()
            return
        
        # Get student stats
        student_stats = get_student_stats(students)
    
    # Create tabs for different views
    tab1, tab2 = st.tabs(["Overview", "Student Details"])
    
    with tab1:
        st.header("Student Overview")
        
        # Summary metrics
        active_students = sum(1 for s in student_stats if s['days_since_active'] < 7)
        avg_score = sum(s['average_score'] for s in student_stats if s['total_quizzes'] > 0) / max(1, sum(1 for s in student_stats if s['total_quizzes'] > 0))
        total_quizzes = sum(s['total_quizzes'] for s in student_stats)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Students", len(students))
        col2.metric("Active Students (7 days)", active_students)
        col3.metric("Average Score", f"{avg_score:.1f}%")
        
        # Student table
        st.subheader("Student List")
        
        # Convert to DataFrame for easier display
        student_df = pd.DataFrame([
            {
                'Student': s['displayName'],
                'Email': s['email'],
                'Quizzes Taken': s['total_quizzes'],
                'Avg Score': f"{s['average_score']:.1f}%" if s['total_quizzes'] > 0 else "N/A",
                'Last Active': f"{s['days_since_active']} days ago" if s['days_since_active'] < 365 else "Never",
                'Current Streak': s['streak_days'],
                'View': s['uid']
            } for s in student_stats
        ])
        
        # Display the table with selection
        selected_student = st.data_editor(
            student_df,
            column_config={
                "Student": st.column_config.TextColumn("Student", width="medium"),
                "Email": st.column_config.TextColumn("Email", width="medium"),
                "Quizzes Taken": st.column_config.NumberColumn("Quizzes", width="small"),
                "Avg Score": st.column_config.TextColumn("Avg Score", width="small"),
                "Last Active": st.column_config.TextColumn("Last Active", width="small"),
                "Current Streak": st.column_config.NumberColumn("Streak", width="small"),
                "View": st.column_config.SelectboxColumn(
                    "Select",
                    width="small",
                    options=student_df['View'].tolist(),
                    required=True
                )
            },
            hide_index=True,
            use_container_width=True,
            disabled=["Student", "Email", "Quizzes Taken", "Avg Score", "Last Active", "Current Streak"]
        )
        
        # Handle selected student
        if selected_student is not None and 'View' in selected_student:
            selected_uid = selected_student['View'].iloc[0] if not selected_student['View'].empty else None
            if selected_uid:
                # Store the selected student UID in session state
                st.session_state.selected_student_uid = selected_uid
                # Switch to the Student Details tab
                st.rerun()
    
    with tab2:
        st.header("Student Details")
        
        # Check if a student is selected
        if 'selected_student_uid' in st.session_state:
            selected_uid = st.session_state.selected_student_uid
            
            # Find the selected student in our data
            selected_student = next((s for s in student_stats if s['uid'] == selected_uid), None)
            
            if selected_student:
                st.subheader(f"Student: {selected_student['displayName']} ({selected_student['email']})")
                
                # Student metrics
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Quizzes Taken", selected_student['total_quizzes'])
                col2.metric("Questions Attempted", selected_student['total_questions'])
                col3.metric("Average Score", f"{selected_student['average_score']:.1f}%" if selected_student['total_quizzes'] > 0 else "N/A")
                col4.metric("Current Streak", f"{selected_student['streak_days']} days")
                
                # Topic performance
                st.subheader("Topic Performance")
                
                topic_performance = selected_student['topic_performance']
                if topic_performance:
                    # Get topic names
                    topic_ids = list(topic_performance.keys())
                    topic_names = user_stats.get_topic_names(conn, topic_ids)
                    
                    # Create a dataframe for the topic performance
                    topic_data = []
                    
                    for topic_id, stats in topic_performance.items():
                        topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
                        questions = stats.get('questions_attempted', 0)
                        correct = stats.get('correct_answers', 0)
                        score = stats.get('average_score', 0)
                        
                        topic_data.append({
                            'Topic': topic_name,
                            'Questions': questions,
                            'Correct': correct,
                            'Score': f"{score:.1f}%"
                        })
                    
                    topic_df = pd.DataFrame(topic_data)
                    st.dataframe(topic_df, use_container_width=True)
                    
                    # Create a bar chart of scores by topic
                    chart_data = pd.DataFrame([
                        {'Topic': row['Topic'], 'Score': float(row['Score'].replace('%', ''))} 
                        for row in topic_data
                    ])
                    st.bar_chart(chart_data.set_index('Topic'))
                    
                    # Display weak and strong areas
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Areas to Improve")
                        weak_areas = selected_student['weak_areas']
                        if weak_areas:
                            for topic_id in weak_areas:
                                topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
                                score = topic_performance.get(topic_id, {}).get('average_score', 0)
                                st.markdown(f"- {topic_name}: {score:.1f}%")
                        else:
                            st.info("No weak areas identified yet")
                    
                    with col2:
                        st.subheader("Strong Areas")
                        strong_areas = selected_student['strong_areas']
                        if strong_areas:
                            for topic_id in strong_areas:
                                topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
                                score = topic_performance.get(topic_id, {}).get('average_score', 0)
                                st.markdown(f"- {topic_name}: {score:.1f}%")
                        else:
                            st.info("No strong areas identified yet")
                else:
                    st.info("No topic performance data available yet.")
                
                # Quiz history
                st.subheader("Quiz History")
                quiz_history = selected_student['quiz_history']
                
                if quiz_history:
                    # Convert to DataFrame for easier display
                    quiz_df = pd.DataFrame([
                        {
                            'Date': quiz.get('date').strftime("%Y-%m-%d %H:%M") if isinstance(quiz.get('date'), datetime) else "Unknown",
                            'Score': f"{quiz.get('score', 0):.1f}%",
                            'Questions': quiz.get('num_questions', 0),
                            'Correct': quiz.get('correct_answers', 0),
                            'Time': f"{quiz.get('time_taken_seconds', 0)//60}m {quiz.get('time_taken_seconds', 0)%60}s"
                        } for quiz in quiz_history
                    ])
                    
                    st.dataframe(quiz_df, use_container_width=True)
                    
                    # Create a line chart of scores over time
                    if len(quiz_history) > 1:
                        chart_data = pd.DataFrame([
                            {
                                'Date': quiz.get('date') if isinstance(quiz.get('date'), datetime) else datetime.now(),
                                'Score': quiz.get('score', 0)
                            } for quiz in quiz_history
                        ])
                        chart_data = chart_data.sort_values('Date')
                        st.line_chart(chart_data.set_index('Date'))
                else:
                    st.info("No quiz history available yet.")
            else:
                st.error(f"Student with UID {selected_uid} not found.")
        else:
            st.info("Select a student from the Overview tab to view details.")
    
    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
