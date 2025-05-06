#!/usr/bin/env python3

"""Question Management Page for CFA Level I Quiz App"""

import os
import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

import role_management

# Set page configuration
st.set_page_config(
    page_title="Question Management - CFA Level I Quiz App",
    page_icon="ud83dudcdd",
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


def get_all_questions(
    conn, limit=100, offset=0, search_term=None, topic_id=None, week_id=None,
):
    """Get all questions with optional filtering"""
    cursor = conn.cursor()

    # Build query with filters
    query = """
        SELECT q.question_id, q.title, t.name as topic, w.week_number as week,
               d.name as difficulty, COUNT(ao.option_id) as num_options
        FROM questions q
        LEFT JOIN topics t ON q.topic_id = t.topic_id
        LEFT JOIN weeks w ON q.week_id = w.week_id
        LEFT JOIN difficulty_levels d ON q.difficulty_id = d.difficulty_id
        LEFT JOIN answer_options ao ON q.question_id = ao.question_id
    """

    # Add WHERE clause for filters
    conditions = []
    params = []

    if search_term:
        conditions.append("(q.title LIKE ? OR q.question_text LIKE ?)")
        search_pattern = f"%{search_term}%"
        params.extend([search_pattern, search_pattern])

    if topic_id:
        conditions.append("q.topic_id = ?")
        params.append(topic_id)

    if week_id:
        conditions.append("q.week_id = ?")
        params.append(week_id)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Add GROUP BY, ORDER BY, and LIMIT
    query += """
        GROUP BY q.question_id
        ORDER BY q.question_id DESC
        LIMIT ? OFFSET ?
    """

    params.extend([limit, offset])

    cursor.execute(query, params)
    return cursor.fetchall()


def get_question_details(conn, question_id):
    """Get complete details for a specific question"""
    cursor = conn.cursor()

    # Get question data
    cursor.execute(
        """
        SELECT q.question_id, q.title, q.question_text, 
               t.name as topic, m.name as module, 
               d.name as difficulty, r.name as reading,
               w.week_number as week
        FROM questions q
        LEFT JOIN topics t ON q.topic_id = t.topic_id
        LEFT JOIN modules m ON q.module_id = m.module_id
        LEFT JOIN difficulty_levels d ON q.difficulty_id = d.difficulty_id
        LEFT JOIN readings r ON q.reading_id = r.reading_id
        LEFT JOIN weeks w ON q.week_id = w.week_id
        WHERE q.question_id = ?
    """,
        (question_id,),
    )

    question = cursor.fetchone()
    if not question:
        return None

    # Get answer options
    cursor.execute(
        """
        SELECT option_id, option_letter, option_text, is_correct
        FROM answer_options
        WHERE question_id = ?
        ORDER BY option_letter
    """,
        (question_id,),
    )

    options = cursor.fetchall()

    # Get explanation
    cursor.execute(
        """
        SELECT explanation_text
        FROM explanations
        WHERE question_id = ?
    """,
        (question_id,),
    )

    explanation = cursor.fetchone()
    explanation_text = explanation["explanation_text"] if explanation else ""

    # Get tags
    cursor.execute(
        """
        SELECT t.name
        FROM question_tags qt
        JOIN tags t ON qt.tag_id = t.tag_id
        WHERE qt.question_id = ?
    """,
        (question_id,),
    )

    tags = [tag["name"] for tag in cursor.fetchall()]

    return {
        "question": dict(question),
        "options": [dict(option) for option in options],
        "explanation": explanation_text,
        "tags": tags,
    }


def get_topics(conn):
    """Get all topics from the database"""
    cursor = conn.cursor()
    cursor.execute("SELECT topic_id, name FROM topics ORDER BY name")
    return cursor.fetchall()


def get_weeks(conn):
    """Get all weeks from the database"""
    cursor = conn.cursor()
    cursor.execute("SELECT week_id, week_number FROM weeks ORDER BY week_number")
    return cursor.fetchall()


def main():
    # Check if user is logged in
    if "user_uid" not in st.session_state:
        st.warning("Please log in to access this page.")
        st.page_link("quiz_app.py", label="Go to Login Page", icon="ud83dudd11")
        return

    user_uid = st.session_state["user_uid"]

    # Check if user has instructor role or higher
    if not role_management.check_user_access(user_uid, "instructor"):
        st.error("You do not have permission to access this page.")
        if st.button("Go to Home Page"):
            import os
            import subprocess
            import sys

            # Launch the main app
            subprocess.Popen(
                [sys.executable, "-m", "streamlit", "run", "quiz_app.py"],
                cwd=os.path.dirname(os.path.abspath(__file__)),
            )
            st.stop()
        return

    # Display sidebar based on user role
    role_management.show_role_based_sidebar(user_uid)

    # Question Management
    st.title("Question Management")

    # Connect to database
    db_path = os.path.join(Path(__file__).parent, "database", "cfa_questions.db")
    conn = connect_to_db(db_path)

    if not conn:
        st.error("Could not connect to database. Please check the database file.")
        return

    # Create tabs for different functions
    tab1, tab2 = st.tabs(["Browse Questions", "Edit Question"])

    with tab1:
        st.header("Browse Questions")

        # Filter options
        col1, col2, col3 = st.columns(3)

        with col1:
            search_term = st.text_input(
                "Search in title or question text", key="search_term",
            )

        with col2:
            # Get topics for filter
            topics = get_topics(conn)
            topic_options = [(None, "All Topics")] + [
                (t["topic_id"], t["name"]) for t in topics
            ]
            selected_topic = st.selectbox(
                "Filter by Topic",
                options=[t[0] for t in topic_options],
                format_func=lambda x: next(
                    (t[1] for t in topic_options if t[0] == x), "All Topics",
                ),
                key="topic_filter",
            )

        with col3:
            # Get weeks for filter
            weeks = get_weeks(conn)
            week_options = [(None, "All Weeks")] + [
                (w["week_id"], f"Week {w['week_number']}") for w in weeks
            ]
            selected_week = st.selectbox(
                "Filter by Week",
                options=[w[0] for w in week_options],
                format_func=lambda x: next(
                    (w[1] for w in week_options if w[0] == x), "All Weeks",
                ),
                key="week_filter",
            )

        # Pagination
        items_per_page = 20
        if "page_number" not in st.session_state:
            st.session_state.page_number = 0

        # Get questions with filters
        questions = get_all_questions(
            conn,
            limit=items_per_page,
            offset=st.session_state.page_number * items_per_page,
            search_term=search_term,
            topic_id=selected_topic,
            week_id=selected_week,
        )

        # Display questions in a table
        if questions:
            # Convert to DataFrame for easier display
            questions_df = pd.DataFrame([dict(q) for q in questions])

            # Add a view button column
            questions_df["view"] = "View"

            # Display the table
            selected_rows = st.data_editor(
                questions_df[
                    [
                        "question_id",
                        "title",
                        "topic",
                        "week",
                        "difficulty",
                        "num_options",
                        "view",
                    ]
                ],
                column_config={
                    "question_id": st.column_config.NumberColumn("ID", width="small"),
                    "title": st.column_config.TextColumn("Title", width="large"),
                    "topic": st.column_config.TextColumn("Topic", width="medium"),
                    "week": st.column_config.NumberColumn("Week", width="small"),
                    "difficulty": st.column_config.TextColumn(
                        "Difficulty", width="small",
                    ),
                    "num_options": st.column_config.NumberColumn(
                        "Options", width="small",
                    ),
                    "view": st.column_config.CheckboxColumn("Select", width="small"),
                },
                hide_index=True,
                use_container_width=True,
                disabled=[
                    "question_id",
                    "title",
                    "topic",
                    "week",
                    "difficulty",
                    "num_options",
                ],
            )

            # Handle selected question
            if selected_rows is not None and "view" in selected_rows:
                selected_question_ids = selected_rows[selected_rows["view"]][
                    "question_id"
                ].tolist()
                if selected_question_ids:
                    # Store the selected question ID in session state
                    st.session_state.selected_question_id = selected_question_ids[0]
                    # Switch to the Edit Question tab
                    st.rerun()

            # Pagination controls
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                if st.session_state.page_number > 0:
                    if st.button("Previous Page"):
                        st.session_state.page_number -= 1
                        st.rerun()

            with col2:
                st.write(f"Page {st.session_state.page_number + 1}")

            with col3:
                if (
                    len(questions) == items_per_page
                ):  # If we have a full page, there might be more
                    if st.button("Next Page"):
                        st.session_state.page_number += 1
                        st.rerun()
        else:
            st.info("No questions found with the current filters.")

    with tab2:
        st.header("Edit Question")

        # Check if a question is selected
        if "selected_question_id" in st.session_state:
            question_id = st.session_state.selected_question_id
            question_data = get_question_details(conn, question_id)

            if question_data:
                # Display question details
                st.subheader(
                    f"Question ID: {question_id} - {question_data['question']['title']}",
                )

                # Basic info
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Topic:** {question_data['question']['topic']}")
                    st.write(f"**Module:** {question_data['question']['module']}")
                    st.write(f"**Week:** {question_data['question']['week']}")

                with col2:
                    st.write(
                        f"**Difficulty:** {question_data['question']['difficulty']}",
                    )
                    st.write(f"**Reading:** {question_data['question']['reading']}")
                    st.write(f"**Tags:** {', '.join(question_data['tags'])}")

                # Question text
                st.subheader("Question Text")
                st.write(question_data["question"]["question_text"])

                # Answer options
                st.subheader("Answer Options")
                for option in question_data["options"]:
                    if option["is_correct"]:
                        st.success(
                            f"**{option['option_letter']})** {option['option_text']} ✓",
                        )
                    else:
                        st.write(
                            f"**{option['option_letter']})** {option['option_text']}",
                        )

                # Explanation
                st.subheader("Explanation")
                st.write(question_data["explanation"])

                # Edit form
                with st.expander("Edit Question"):
                    st.warning(
                        "Editing functionality will be implemented in a future update.",
                    )

                    # Placeholder for edit form
                    st.text_input("Title", value=question_data["question"]["title"])
                    st.text_area(
                        "Question Text",
                        value=question_data["question"]["question_text"],
                    )

                    # Options editing would go here

                    # Explanation editing
                    st.text_area("Explanation", value=question_data["explanation"])

                    # Save button (disabled for now)
                    st.button("Save Changes", disabled=True)
            else:
                st.error(f"Question with ID {question_id} not found.")
        else:
            st.info("Select a question from the Browse Questions tab to edit.")

    # Close database connection
    conn.close()


if __name__ == "__main__":
    main()
