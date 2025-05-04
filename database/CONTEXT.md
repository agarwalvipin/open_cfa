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
2. Implement user authentication and progress tracking
3. Add features for spaced repetition learning
4. Develop analytics to track performance on different topics/modules
5. Enhance the quiz app with additional features like timed quizzes and difficulty settings

## Quiz Application

We've developed a Streamlit-based quiz application (`quiz_app.py`) that allows users to:

1. Browse all available topics in the question bank
2. Select multiple topics of interest for their quiz
3. See the total number of questions available for their selected topics
4. Choose how many questions they want in their quiz
5. Take the quiz with interactive question navigation
6. Review their results with explanations for each question

The quiz app uses the SQLite database (`cfa_questions.db`) to fetch questions and provides immediate feedback on user answers.
