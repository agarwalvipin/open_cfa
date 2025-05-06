import streamlit as st
from firebase_admin import auth as admin_auth

import firebase_auth

# Role-based access control functions


def check_user_access(user_uid, required_role):
    """Check if a user has the required role or higher

    Args:
        user_uid: User's Firebase UID
        required_role: Minimum role required (student, instructor, admin)

    Returns:
        Boolean indicating if the user has access

    """
    if not user_uid:
        return False

    # Get user's current role
    user_role = firebase_auth.get_user_role(user_uid)

    # Role hierarchy
    role_levels = {
        "student": 1,
        "instructor": 2,
        "admin": 3,
    }

    # Check if user's role level is >= required role level
    return role_levels.get(user_role, 0) >= role_levels.get(required_role, 0)


def get_all_users(limit=100):
    """Get all users from Firebase Auth

    Args:
        limit: Maximum number of users to return

    Returns:
        List of user dictionaries with uid, email, displayName, role

    """
    try:
        # Initialize Firebase Admin SDK
        firebase_auth.initialize_firebase_admin()

        # Get users from Firebase Auth
        users = []
        page = admin_auth.list_users()
        count = 0

        for user in page.users:
            if count >= limit:
                break

            # Get user role
            role = firebase_auth.get_user_role(user.uid)

            users.append(
                {
                    "uid": user.uid,
                    "email": user.email,
                    "displayName": user.display_name or user.email.split("@")[0],
                    "role": role,
                },
            )

            count += 1

        return users
    except Exception as e:
        st.error(f"Error getting users: {e}")
        return []


def display_user_management():
    """Display user management interface for admins"""
    st.header("User Management")

    # Get current user
    user_uid = st.session_state.get("user_uid")
    if not user_uid:
        st.warning("You must be logged in to access this page.")
        if st.button("Go to Login Page"):
            st.session_state.current_page = "dashboard"
            st.rerun()
        return

    # Check if user has admin role
    if not check_user_access(user_uid, "admin"):
        st.error("You do not have permission to access this page.")
        if st.button("Go to Home Page"):
            st.session_state.current_page = "dashboard"
            st.rerun()
        return

    # Get all users
    users = get_all_users()

    if not users:
        st.warning("No users found or error retrieving users.")
        return

    # Get available roles
    available_roles = firebase_auth.get_available_roles()
    role_options = list(available_roles.keys())

    # Display users in a table with role management
    st.subheader(f"Manage Users ({len(users)} users)")

    # Create a container for the user list
    user_container = st.container()

    with user_container:
        # Use columns for layout
        cols = st.columns([3, 2, 2, 3])
        cols[0].markdown("**Email**")
        cols[1].markdown("**Display Name**")
        cols[2].markdown("**Current Role**")
        cols[3].markdown("**Actions**")

        st.divider()

        for user in users:
            # Skip the current admin user (can't change own role)
            if user["uid"] == user_uid:
                cols = st.columns([3, 2, 2, 3])
                cols[0].text(user["email"])
                cols[1].text(user["displayName"])
                cols[2].text(f"{user['role']} (you)")
                cols[3].text("Cannot modify own role")
                continue

            cols = st.columns([3, 2, 2, 3])
            cols[0].text(user["email"])
            cols[1].text(user["displayName"])
            cols[2].text(user["role"])

            # Role selection and update button
            with cols[3]:
                with st.form(key=f"role_form_{user['uid']}", border=False):
                    new_role = st.selectbox(
                        "New Role",
                        options=role_options,
                        index=role_options.index(user["role"]),
                        key=f"role_select_{user['uid']}",
                        label_visibility="collapsed",
                    )

                    if st.form_submit_button("Update", use_container_width=True):
                        if new_role != user["role"]:
                            result = firebase_auth.set_user_role(user["uid"], new_role)
                            if result["success"]:
                                st.success(f"Updated {user['email']} to {new_role}")
                                st.rerun()
                            else:
                                st.error(result["message"])


def show_role_based_sidebar(user_uid):
    """Display sidebar options based on user role

    Args:
        user_uid: User's Firebase UID

    """
    if not user_uid:
        return

    # Initialize current_page in session state if it doesn't exist
    if "current_page" not in st.session_state:
        st.session_state.current_page = "dashboard"

    user_role = firebase_auth.get_user_role(user_uid)

    # All users can see these options

    # Student options (available to all roles)
    if check_user_access(user_uid, "student"):
        st.sidebar.title("Navigation")

        # Main navigation options
        if st.sidebar.button(
            "Dashboard",
            type="primary"
            if st.session_state.current_page == "dashboard"
            else "secondary",
            key="nav_dashboard",
        ):
            st.session_state.current_page = "dashboard"
            st.rerun()

        if st.sidebar.button(
            "Create Quiz",
            type="primary"
            if st.session_state.current_page == "create_quiz"
            else "secondary",
            key="nav_create_quiz",
        ):
            st.session_state.current_page = "create_quiz"
            # Always initialize quiz wizard state to ensure it's set correctly
            st.session_state.quiz_wizard_step = 1
            st.rerun()

        if st.sidebar.button(
            "Take Quiz",
            type="primary" if st.session_state.current_page == "quiz" else "secondary",
            key="nav_take_quiz",
        ):
            st.session_state.current_page = "quiz"
            st.rerun()

        if st.sidebar.button(
            "Load Questions",
            type="primary"
            if st.session_state.current_page == "load_questions"
            else "secondary",
            key="nav_load_questions",
        ):
            st.session_state.current_page = "load_questions"
            st.rerun()

    # Instructor options
    if check_user_access(user_uid, "instructor"):
        st.sidebar.divider()
        st.sidebar.subheader("Instructor Tools")

        if st.sidebar.button("Manage Questions 📝", key="nav_question_management"):
            # Launch question management as a separate app

            st.session_state["launching_external"] = True
            st.rerun()

        if st.sidebar.button("Student Progress 📈", key="nav_student_progress"):
            # We'll implement this later
            st.info("Student progress tracking coming soon!")

    # Admin options
    if check_user_access(user_uid, "admin"):
        st.sidebar.divider()
        st.sidebar.subheader("Admin Tools")

        if st.sidebar.button("Admin Dashboard 🔑", key="nav_admin_dashboard"):
            # Set the current page to admin_dashboard
            st.session_state.current_page = "admin_dashboard"
            st.rerun()

        if st.sidebar.button("User Management 👥", key="nav_user_management"):
            # We'll implement this later
            st.info("User management coming soon!")

    # Show user role
    st.sidebar.divider()
    st.sidebar.caption(f"Logged in as: {user_role.capitalize()}")
