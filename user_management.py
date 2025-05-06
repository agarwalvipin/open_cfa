#!/usr/bin/env python3

"""User Management Page for CFA Level I Quiz App"""

import streamlit as st

import role_management

# Set page configuration
st.set_page_config(
    page_title="User Management - CFA Level I Quiz App",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    # Check if user is logged in
    if "user_uid" not in st.session_state:
        st.warning("Please log in to access this page.")
        if st.button("Go to Login Page"):
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

    user_uid = st.session_state["user_uid"]

    # Check if user has admin role
    if not role_management.check_user_access(user_uid, "admin"):
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

    # Display user management interface
    role_management.display_user_management()


if __name__ == "__main__":
    main()
