# CFA Question Bank Database Project - Context Summary

## Project Overview

We've created a database system to store and query CFA Level I exam questions from the question bank. The question bank is organized in markdown files with a specific structure, and we've developed tools to parse these files and store the data in both PostgreSQL and SQLite databases.

## Completed Tasks

### 1. Database Schema Design

- Created a PostgreSQL schema (`schema.sql`) that models the question bank structure
- Created a SQLite version of the schema (`sqlite_schema.sql`) for easier local development
- The schema includes tables for:
  - Questions and their metadata
  - Answer options
  - Explanations
  - Topics and modules
  - Learning objectives
  - Difficulty levels
  - Tags
  - Weeks

### 2. Import Tools

- Developed a Python script (`import_questions.py`) for importing questions into PostgreSQL
- Developed a Python script (`import_to_sqlite.py`) for importing questions into SQLite
- Both scripts parse the markdown files to extract:
  - Question metadata (topic, module, difficulty, etc.)
  - Question text
  - Answer options
  - Correct answers
  - Explanations
  - Tags

### 3. Database Creation

- Successfully created a SQLite database (`cfa_questions.db`)
- Imported all 24 ethics questions from Week 3 into the database
- Verified that the database correctly stores all question components

### 4. Query Tools

- Created a Python script (`query_examples.py`) to demonstrate how to query the database
- Implemented functions to query questions by:
  - Topic
  - Module
  - Difficulty level
  - Question ID
  - Random selection

## Question Bank Structure

The question bank is organized in markdown files with the following structure:

- Questions are separated by horizontal rules (`---`)
- Each question has:
  - A title (e.g., `## 🟢 Q1 – Ethical & Professional Standards - Standard I - Professionalism`)
  - Metadata in a `<details>` section with information like ID, level, topic, module, etc.
  - Question text
  - Multiple choice options (A, B, C, D)
  - Answer and explanation in a `<details>` section

## Database Structure

The database schema is designed to efficiently store and query the question bank data:

- **topics**: Main subject areas (e.g., Ethical & Professional Standards)
- **modules**: Specific modules within topics (e.g., Standard I(A) Knowledge of the Law)
- **questions**: The main question data including text, title, and metadata
- **answer_options**: Multiple choice options for each question
- **explanations**: Detailed explanations for the correct answers
- **tags**: Keywords associated with questions for easier searching

## Next Steps

Possible next steps for the project:

1. Import the remaining question files from other weeks and topics
2. ✅ Implement user authentication and progress tracking (Completed with Firebase Auth and Firestore)
3. Add features for spaced repetition learning
4. ✅ Develop analytics to track performance on different topics/modules (Completed with user statistics)
5. ✅ Enhance the quiz app with additional features like timed quizzes and difficulty settings (Completed)
6. ✅ Implement role management for users (Completed with Firebase custom claims)
7. ✅ Add database management tools for administrators (Completed with admin dashboard cleanup functionality)

## Quiz Application

We've developed a Streamlit-based quiz application (`quiz_app.py`) that allows users to:

1. Browse all available topics in the question bank
2. Select multiple topics of interest for their quiz
3. See the total number of questions available for their selected topics
4. Choose how many questions they want in their quiz
5. Take the quiz with interactive question navigation
6. Review their results with explanations for each question

The quiz app uses the SQLite database (`cfa_questions.db`) to fetch questions and provides immediate feedback on user answers.

### Admin Dashboard

We've implemented an Admin Dashboard with the following features:

1. **System Statistics**: Provides an overview of the question database including:
   - Total number of questions
   - Questions by topic (with visualizations)
   - Questions by week (with visualizations)
   - Questions by difficulty level (with visualizations)

2. **User Activity**: Shows statistics about user engagement:
   - Total number of users
   - Recent quiz attempts with scores and time taken

3. **Database Management**: Tools for maintaining the question database:
   - **Question Cleanup**: Allows deleting questions filtered by topic and/or week
   - **Orphaned Data Cleanup**: Removes unused reference data (topics, tags, modules, etc.) that aren't associated with any questions

The admin dashboard is integrated into the main application and accessible only to users with admin privileges.

### Create Quiz Wizard

We've implemented a 'Create Quiz' feature with a step-by-step wizard that allows users to apply multiple filters to customize their quiz:

1. **Topic Selection**: Choose one or more topics (e.g., Ethics, Quantitative Methods)
2. **Week Selection**: Filter questions by specific study weeks
3. **Difficulty Selection**: Filter by difficulty levels (e.g., Easy, Medium, Hard)
4. **Module Selection**: Choose specific modules within topics
5. **Tags and Quiz Size**: Select specific tags and determine the number of questions

Each filter category has an 'All' option by default, allowing users to easily select all items in a category or indicate they don't want to filter by that category.

The wizard shows the total number of available questions based on the selected filters and allows users to start the quiz with their customized selection.

### Quiz Timer

The quiz application includes a timer feature that allocates 90 seconds per question. For example, if a user selects 10 questions for their quiz, they will have 15 minutes (900 seconds) to complete it. The timer displays the remaining time in minutes and seconds during the quiz.

Features of the timer include:

- Automatic countdown during the quiz
- Visual display of remaining time
- Automatic submission when time runs out
- Display of total time taken at the end of the quiz

## User Statistics and Performance Tracking

We've implemented a comprehensive user statistics system using Firebase Firestore to track user performance and progress:

### Firestore Database Schema

1. **user_stats collection**:
   - Document ID: user_uid
   - Fields:
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

2. **quiz_attempts collection**:
   - Document ID: auto-generated
   - Fields:
     - user_uid: string
     - date: timestamp
     - topics: array of topic_ids
     - weeks: array of week_ids
     - num_questions: int
     - score: float
     - correct_answers: int
     - time_taken_seconds: int
     - questions: array of {question_id, user_answer, correct_answer, is_correct}

### User Dashboard

The user dashboard provides a comprehensive view of the user's performance and progress:

1. **Key Metrics**:
   - Total quizzes taken
   - Average score across all quizzes
   - Current streak (consecutive days of quiz taking)
   - Total questions attempted

2. **Badge System**:
   Users can earn badges for various achievements:
   - First Steps: Completed first quiz
   - Getting Started: Completed 5 quizzes
   - Dedicated Learner: Completed 10 quizzes
   - Perfect Score: Achieved 100% on a quiz
   - Consistency: Maintained a 3-day streak
   - Weekly Warrior: Maintained a 7-day streak
   - Century: Attempted 100 questions
   - Topic Mastery: Mastered 3 or more topics

3. **Topic Performance**:
   - Detailed breakdown of performance by topic
   - Identification of strong areas (topics with scores > 80%)
   - Identification of weak areas (topics with scores < 60%)
   - Visual representation of topic performance

4. **Quiz History**:
   - Recent quiz attempts with scores and details
   - Ability to review past quiz questions and answers
   - Time taken for each quiz

### Performance Analytics

The system automatically analyzes user performance to provide insights:

1. **Topic Analysis**:
   - Tracks performance across different topics
   - Identifies topics that need more focus
   - Highlights topics where the user excels

2. **Progress Tracking**:
   - Tracks improvement over time
   - Maintains streak data to encourage regular study
   - Provides visual feedback on progress

3. **Personalized Recommendations**:
   - Based on weak areas, the system can suggest topics to focus on
   - Encourages users to maintain their streak
   - Motivates users through the badge system

This user statistics system provides valuable insights to help users focus their study efforts and track their progress toward CFA exam readiness.

## Role Management System

We've implemented a comprehensive role management system using Firebase Authentication custom claims to control access to different features of the application:

### User Roles

The system supports three distinct user roles with a hierarchical access structure:

1. **Student** (default role):
   - Access to quizzes and personal dashboard
   - Can view their own performance statistics
   - Cannot access administrative or instructor features

2. **Instructor**:
   - All student privileges
   - Access to question management (browse and edit questions)
   - Access to student progress monitoring
   - Cannot manage users or access admin dashboard

3. **Administrator**:
   - All instructor and student privileges
   - User management capabilities (assign/change roles)
   - Access to system-wide statistics and admin dashboard
   - Full access to all system features

### Implementation Details

1. **Firebase Custom Claims**:
   - User roles are stored as custom claims in Firebase Authentication
   - New users are automatically assigned the 'student' role
   - Only administrators can change user roles

2. **Role-Based Access Control**:
   - Each page checks the user's role before allowing access
   - Navigation options are dynamically displayed based on user role
   - Unauthorized access attempts are redirected to the home page

3. **Admin Interface**:
   - User management page for viewing and modifying user roles
   - Admin dashboard with system-wide statistics
   - Monitoring of user activity and performance

4. **Instructor Tools**:
   - Question management interface for browsing and editing questions
   - Student progress monitoring with detailed performance analytics
   - Topic performance visualization across all students

### Recent Enhancements (May 2025)

1. **Improved Navigation System**:
   - Implemented role-based sidebar navigation
   - Dynamically shows options based on user's role
   - Organized navigation into logical sections (main navigation, instructor tools, admin tools)

2. **Admin User Management**:
   - Created utility script (`create_admin.py`) for promoting users to admin role
   - Implemented admin interface for managing user roles
   - Added ability to view all users and change their roles

3. **Session State Management**:
   - Improved handling of Streamlit session state for better navigation
   - Fixed initialization issues with session variables
   - Enhanced logout process to properly clean up session state

4. **Database Integration**:
   - Updated all components to use the correct database file (`cfa_questions.db`)
   - Ensured proper database connections across all application modules
   - Implemented error handling for database connection issues

This role management system ensures proper access control while providing specialized tools for different user types, enhancing both security and usability of the application. The system is fully integrated with Firebase Authentication and Firestore, providing a seamless and secure user experience.
