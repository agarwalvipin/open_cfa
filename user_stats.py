from datetime import datetime

import firebase_admin
import streamlit as st
from firebase_admin import firestore


# Initialize Firestore
def initialize_firestore():
    """Initialize Firestore if not already initialized"""
    if not firebase_admin._apps:
        # This will use the credentials from firebase_config.py
        from firebase_auth import initialize_firebase_admin

        initialize_firebase_admin()

    return firestore.client()


# User Stats Schema
"""
Firestore Collection: user_stats
Document ID: user_uid
Fields:
    - total_quizzes_taken: int
    - total_questions_attempted: int
    - total_correct_answers: int
    - average_score: float
    - total_time_spent_seconds: int
    - last_quiz_date: timestamp
    - streak_days: int
    - last_active_date: timestamp
    - topic_performance: map (topic_id -> {questions_attempted, correct_answers, average_score})
    - weak_areas: array of topic_ids
    - strong_areas: array of topic_ids
    - badges: array of badge_ids
    - quiz_history: array of quiz_ids

Firestore Collection: quiz_attempts
Document ID: auto-generated
Fields:
    - user_uid: string
    - date: timestamp
    - topics: array of topic_ids
    - weeks: array of week_ids
    - num_questions: int
    - score: float
    - correct_answers: int
    - time_taken_seconds: int
    - questions: array of {question_id, user_answer, correct_answer, is_correct}
"""


# Save quiz results to Firestore
def save_quiz_results(user_uid, topics, weeks, question_results, time_taken_seconds):
    """Save quiz results to Firestore

    Args:
        user_uid: User's Firebase UID
        topics: List of topic IDs included in the quiz
        weeks: List of week IDs included in the quiz
        question_results: Dict of {question_id: {user_answer, correct_answer, is_correct}}
        time_taken_seconds: Time taken to complete the quiz in seconds

    """
    if not user_uid:
        st.warning("User not logged in. Quiz results will not be saved.")
        return False

    try:
        db = initialize_firestore()

        # Calculate quiz statistics
        num_questions = len(question_results)
        correct_answers = sum(
            1 for q in question_results.values() if q.get("is_correct", False)
        )
        score = (correct_answers / num_questions) * 100 if num_questions > 0 else 0

        # Create quiz attempt record
        quiz_data = {
            "user_uid": user_uid,
            "date": datetime.now(),
            "topics": topics if topics else [],
            "weeks": weeks if weeks else [],
            "num_questions": num_questions,
            "score": score,
            "correct_answers": correct_answers,
            "time_taken_seconds": time_taken_seconds,
            "questions": [
                {
                    "question_id": q_id,
                    "user_answer": data.get("user_answer"),
                    "correct_answer": data.get("correct_answer"),
                    "is_correct": data.get("is_correct", False),
                }
                for q_id, data in question_results.items()
            ],
        }

        # Add quiz attempt to Firestore
        quiz_ref = db.collection("quiz_attempts").document()
        quiz_ref.set(quiz_data)
        quiz_id = quiz_ref.id

        # Update user stats
        update_user_stats(db, user_uid, quiz_id, quiz_data)

        return True
    except Exception as e:
        st.error(f"Error saving quiz results: {e}")
        return False


# Update user statistics
def update_user_stats(db, user_uid, quiz_id, quiz_data):
    """Update user statistics based on quiz results

    Args:
        db: Firestore client
        user_uid: User's Firebase UID
        quiz_id: ID of the quiz attempt
        quiz_data: Quiz data dictionary

    """
    user_ref = db.collection("user_stats").document(user_uid)
    user_doc = user_ref.get()

    # Get current date for streak calculation
    today = datetime.now().date()

    if user_doc.exists:
        # Update existing user stats
        user_stats = user_doc.to_dict()

        # Update basic stats
        total_quizzes = user_stats.get("total_quizzes_taken", 0) + 1
        total_questions = (
            user_stats.get("total_questions_attempted", 0) + quiz_data["num_questions"]
        )
        total_correct = (
            user_stats.get("total_correct_answers", 0) + quiz_data["correct_answers"]
        )
        total_time = (
            user_stats.get("total_time_spent_seconds", 0)
            + quiz_data["time_taken_seconds"]
        )

        # Calculate new average score
        avg_score = (
            (total_correct / total_questions) * 100 if total_questions > 0 else 0
        )

        # Update streak
        last_active = user_stats.get("last_active_date")
        streak = user_stats.get("streak_days", 0)

        if last_active:
            last_active_date = last_active.date()
            # If last active was yesterday, increment streak
            if (today - last_active_date).days == 1:
                streak += 1
            # If last active was today already, keep streak
            elif (today - last_active_date).days == 0:
                pass
            # If more than 1 day gap, reset streak
            else:
                streak = 1
        else:
            streak = 1

        # Update topic performance
        topic_performance = user_stats.get("topic_performance", {})

        # Process each question to update topic performance
        for question in quiz_data["questions"]:
            # Get topic for this question (would need to query from database)
            # For now, we'll use the first topic in the quiz as a placeholder
            if quiz_data["topics"]:
                topic_id = str(
                    quiz_data["topics"][0],
                )  # Convert to string for Firestore keys

                # Initialize topic if not exists
                if topic_id not in topic_performance:
                    topic_performance[topic_id] = {
                        "questions_attempted": 0,
                        "correct_answers": 0,
                        "average_score": 0,
                    }

                # Update topic stats
                topic_performance[topic_id]["questions_attempted"] += 1
                if question.get("is_correct", False):
                    topic_performance[topic_id]["correct_answers"] += 1

                # Recalculate topic average
                topic_questions = topic_performance[topic_id]["questions_attempted"]
                topic_correct = topic_performance[topic_id]["correct_answers"]
                topic_performance[topic_id]["average_score"] = (
                    topic_correct / topic_questions
                ) * 100

        # Identify weak and strong areas (topics with scores below 60% and above 80%)
        weak_areas = []
        strong_areas = []

        for topic_id, stats in topic_performance.items():
            # Only consider topics with at least 5 questions attempted
            if stats["questions_attempted"] >= 5:
                if stats["average_score"] < 60:
                    weak_areas.append(topic_id)
                elif stats["average_score"] > 80:
                    strong_areas.append(topic_id)

        # Get existing quiz history or initialize
        quiz_history = user_stats.get("quiz_history", [])
        quiz_history.append(quiz_id)

        # Update user stats document
        user_ref.update(
            {
                "total_quizzes_taken": total_quizzes,
                "total_questions_attempted": total_questions,
                "total_correct_answers": total_correct,
                "average_score": avg_score,
                "total_time_spent_seconds": total_time,
                "last_quiz_date": datetime.now(),
                "streak_days": streak,
                "last_active_date": datetime.now(),
                "topic_performance": topic_performance,
                "weak_areas": weak_areas,
                "strong_areas": strong_areas,
                "quiz_history": quiz_history,
            },
        )
    else:
        # Create new user stats document
        user_ref.set(
            {
                "total_quizzes_taken": 1,
                "total_questions_attempted": quiz_data["num_questions"],
                "total_correct_answers": quiz_data["correct_answers"],
                "average_score": quiz_data["score"],
                "total_time_spent_seconds": quiz_data["time_taken_seconds"],
                "last_quiz_date": datetime.now(),
                "streak_days": 1,
                "last_active_date": datetime.now(),
                "topic_performance": {},  # Will be populated as user takes more quizzes
                "weak_areas": [],
                "strong_areas": [],
                "badges": [],
                "quiz_history": [quiz_id],
            },
        )


# Get user statistics
def get_user_stats(user_uid):
    """Get user statistics from Firestore

    Args:
        user_uid: User's Firebase UID

    Returns:
        Dictionary of user statistics or None if not found

    """
    if not user_uid:
        return None

    try:
        db = initialize_firestore()
        user_ref = db.collection("user_stats").document(user_uid)
        user_doc = user_ref.get()

        if user_doc.exists:
            return user_doc.to_dict()
        return None
    except Exception as e:
        st.error(f"Error retrieving user stats: {e}")
        return None


# Get user's quiz history
def get_quiz_history(user_uid, limit=10):
    """Get user's quiz history from Firestore

    Args:
        user_uid: User's Firebase UID
        limit: Maximum number of quiz attempts to return

    Returns:
        List of quiz attempts

    """
    if not user_uid:
        return []

    try:
        db = initialize_firestore()
        quiz_ref = db.collection("quiz_attempts")

        try:
            # Try the query with the index first
            query = (
                quiz_ref.where("user_uid", "==", user_uid)
                .order_by("date", direction=firestore.Query.DESCENDING)
                .limit(limit)
            )
            quiz_history = []
            for doc in query.stream():
                quiz_data = doc.to_dict()
                quiz_data["id"] = doc.id
                quiz_history.append(quiz_data)

            return quiz_history
        except Exception:
            # Fallback if index doesn't exist: get all documents for the user and sort them in memory
            st.warning(
                "Firestore index not yet created. Using fallback method to retrieve quiz history.",
            )
            st.info(
                "To improve performance, please create the suggested index in the Firebase console.",
            )

            # Get all documents for this user without ordering
            query = quiz_ref.where("user_uid", "==", user_uid)
            all_quizzes = []
            for doc in query.stream():
                quiz_data = doc.to_dict()
                quiz_data["id"] = doc.id
                all_quizzes.append(quiz_data)

            # Sort in memory by date (descending)
            if all_quizzes:
                # Check if date is a timestamp or string
                if all_quizzes[0].get("date") and hasattr(
                    all_quizzes[0]["date"], "timestamp",
                ):
                    # Sort by timestamp
                    all_quizzes.sort(
                        key=lambda x: x.get("date").timestamp() if x.get("date") else 0,
                        reverse=True,
                    )
                else:
                    # Sort by string representation or other format
                    all_quizzes.sort(key=lambda x: str(x.get("date", "")), reverse=True)

            # Return limited number of quizzes
            return all_quizzes[:limit]
    except Exception as e:
        st.error(f"Error retrieving quiz history: {e}")
        return []


# Get topic names for display
def get_topic_names(conn, topic_ids):
    """Get topic names from SQLite database

    Args:
        conn: SQLite connection
        topic_ids: List of topic IDs

    Returns:
        Dictionary of topic_id -> topic_name

    """
    if not conn or not topic_ids:
        return {}

    try:
        cursor = conn.cursor()
        topic_names = {}

        for topic_id in topic_ids:
            cursor.execute("SELECT name FROM topics WHERE topic_id = ?", (topic_id,))
            result = cursor.fetchone()
            if result:
                topic_names[str(topic_id)] = result["name"]
            else:
                topic_names[str(topic_id)] = f"Topic {topic_id}"

        return topic_names
    except Exception as e:
        st.error(f"Error retrieving topic names: {e}")
        return {}


# Check and award badges
def check_and_award_badges(user_uid):
    """Check if user qualifies for any new badges

    Args:
        user_uid: User's Firebase UID

    Returns:
        List of newly awarded badge IDs

    """
    if not user_uid:
        return []

    try:
        db = initialize_firestore()
        user_ref = db.collection("user_stats").document(user_uid)
        user_doc = user_ref.get()

        if not user_doc.exists:
            return []

        user_stats = user_doc.to_dict()
        current_badges = set(user_stats.get("badges", []))
        new_badges = []

        # Define badge criteria
        badge_criteria = {
            "first_quiz": lambda stats: stats.get("total_quizzes_taken", 0) >= 1,
            "five_quizzes": lambda stats: stats.get("total_quizzes_taken", 0) >= 5,
            "ten_quizzes": lambda stats: stats.get("total_quizzes_taken", 0) >= 10,
            "perfect_score": lambda stats: any(
                q.get("score", 0) == 100 for q in get_quiz_history(user_uid)
            ),
            "streak_3": lambda stats: stats.get("streak_days", 0) >= 3,
            "streak_7": lambda stats: stats.get("streak_days", 0) >= 7,
            "hundred_questions": lambda stats: stats.get("total_questions_attempted", 0)
            >= 100,
            "mastery": lambda stats: len(stats.get("strong_areas", [])) >= 3,
        }

        # Check each badge
        for badge_id, check_func in badge_criteria.items():
            if badge_id not in current_badges and check_func(user_stats):
                new_badges.append(badge_id)
                current_badges.add(badge_id)

        # Update badges if new ones were earned
        if new_badges:
            user_ref.update(
                {
                    "badges": list(current_badges),
                },
            )

        return new_badges
    except Exception as e:
        st.error(f"Error checking badges: {e}")
        return []


# Get badge details
def get_badge_details():
    """Get details for all badges

    Returns:
        Dictionary of badge_id -> badge_details

    """
    return {
        "first_quiz": {
            "name": "First Steps",
            "description": "Completed your first quiz",
            "icon": "🏁",
        },
        "five_quizzes": {
            "name": "Getting Started",
            "description": "Completed 5 quizzes",
            "icon": "🔥",
        },
        "ten_quizzes": {
            "name": "Dedicated Learner",
            "description": "Completed 10 quizzes",
            "icon": "📚",
        },
        "perfect_score": {
            "name": "Perfect Score",
            "description": "Achieved 100% on a quiz",
            "icon": "🌟",
        },
        "streak_3": {
            "name": "Consistency",
            "description": "Maintained a 3-day streak",
            "icon": "📆",
        },
        "streak_7": {
            "name": "Weekly Warrior",
            "description": "Maintained a 7-day streak",
            "icon": "🗓️",
        },
        "hundred_questions": {
            "name": "Century",
            "description": "Attempted 100 questions",
            "icon": "💯",
        },
        "mastery": {
            "name": "Topic Mastery",
            "description": "Mastered 3 or more topics",
            "icon": "🧠",
        },
    }


# Display user dashboard
def display_user_dashboard(conn, user_uid):
    """Display user dashboard with statistics and quiz history

    Args:
        conn: SQLite database connection
        user_uid: User's Firebase UID

    """
    if not user_uid:
        st.warning("Please log in to view your dashboard")
        return

    # Get user statistics
    user_stats = get_user_stats(user_uid)

    if not user_stats:
        st.info("No quiz data available yet. Take a quiz to see your statistics!")
        return

    # Display user statistics
    st.header("Your CFA Study Dashboard")

    # Create columns for stats
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Quizzes Taken", user_stats.get("total_quizzes_taken", 0))

    with col2:
        avg_score = user_stats.get("average_score", 0)
        st.metric("Average Score", f"{avg_score:.1f}%")

    with col3:
        streak = user_stats.get("streak_days", 0)
        st.metric("Current Streak", f"{streak} days")

    with col4:
        total_questions = user_stats.get("total_questions_attempted", 0)
        st.metric("Questions Attempted", total_questions)

    # Display badges
    st.subheader("Your Badges")
    badges = user_stats.get("badges", [])
    badge_details = get_badge_details()

    if badges:
        badge_cols = st.columns(min(4, len(badges)))
        for i, badge_id in enumerate(badges):
            badge = badge_details.get(
                badge_id, {"name": badge_id, "description": "", "icon": "🏆"},
            )
            with badge_cols[i % 4]:
                st.markdown(f"### {badge['icon']}")
                st.markdown(f"**{badge['name']}**")
                st.markdown(badge["description"])
    else:
        st.info("Complete quizzes to earn badges!")

    # Check for new badges
    new_badges = check_and_award_badges(user_uid)
    if new_badges:
        st.success(f"Congratulations! You've earned {len(new_badges)} new badge(s)!")
        for badge_id in new_badges:
            badge = badge_details.get(
                badge_id, {"name": badge_id, "description": "", "icon": "🏆"},
            )
            st.markdown(f"{badge['icon']} **{badge['name']}**: {badge['description']}")

    # Display topic performance
    st.subheader("Topic Performance")
    topic_performance = user_stats.get("topic_performance", {})

    if topic_performance:
        # Get topic names
        topic_ids = list(topic_performance.keys())
        topic_names = get_topic_names(conn, topic_ids)

        # Create a dataframe for the topic performance
        import pandas as pd

        topic_data = []

        for topic_id, stats in topic_performance.items():
            topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
            questions = stats.get("questions_attempted", 0)
            correct = stats.get("correct_answers", 0)
            score = stats.get("average_score", 0)

            topic_data.append(
                {
                    "Topic": topic_name,
                    "Questions": questions,
                    "Correct": correct,
                    "Score": f"{score:.1f}%",
                },
            )

        topic_df = pd.DataFrame(topic_data)
        st.dataframe(topic_df, use_container_width=True)

        # Display weak and strong areas
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Areas to Improve")
            weak_areas = user_stats.get("weak_areas", [])
            if weak_areas:
                for topic_id in weak_areas:
                    topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
                    score = topic_performance.get(topic_id, {}).get("average_score", 0)
                    st.markdown(f"- {topic_name}: {score:.1f}%")
            else:
                st.info("No weak areas identified yet")

        with col2:
            st.subheader("Strong Areas")
            strong_areas = user_stats.get("strong_areas", [])
            if strong_areas:
                for topic_id in strong_areas:
                    topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
                    score = topic_performance.get(topic_id, {}).get("average_score", 0)
                    st.markdown(f"- {topic_name}: {score:.1f}%")
            else:
                st.info("No strong areas identified yet")
    else:
        st.info("Take more quizzes to see your topic performance!")

    # Display quiz history
    st.subheader("Recent Quiz History")
    quiz_history = get_quiz_history(user_uid)

    if quiz_history:
        for i, quiz in enumerate(quiz_history):
            quiz_date = quiz.get("date")
            if isinstance(quiz_date, datetime):
                date_str = quiz_date.strftime("%Y-%m-%d %H:%M")
            else:
                date_str = "Unknown date"

            score = quiz.get("score", 0)
            num_questions = quiz.get("num_questions", 0)
            correct = quiz.get("correct_answers", 0)
            time_taken = quiz.get("time_taken_seconds", 0)
            minutes, seconds = divmod(time_taken, 60)

            # Get topic names
            topic_ids = quiz.get("topics", [])
            topic_names_list = []
            if topic_ids:
                topic_names_dict = get_topic_names(conn, topic_ids)
                topic_names_list = [
                    topic_names_dict.get(str(tid), f"Topic {tid}") for tid in topic_ids
                ]

            with st.expander(f"Quiz {i + 1}: {date_str} - Score: {score:.1f}%"):
                st.markdown(f"**Date:** {date_str}")
                st.markdown(f"**Score:** {correct}/{num_questions} ({score:.1f}%)")
                st.markdown(f"**Time:** {minutes} minutes {seconds} seconds")

                if topic_names_list:
                    st.markdown(f"**Topics:** {', '.join(topic_names_list)}")

                # Show question breakdown
                if st.checkbox("Show Question Details", key=f"quiz_{i}_details"):
                    questions = quiz.get("questions", [])
                    for j, q in enumerate(questions):
                        is_correct = q.get("is_correct", False)
                        icon = "✅" if is_correct else "❌"
                        st.markdown(
                            f"{icon} Question {j + 1}: User answered {q.get('user_answer')}, Correct answer: {q.get('correct_answer')}",
                        )
    else:
        st.info("No quiz history available yet")
