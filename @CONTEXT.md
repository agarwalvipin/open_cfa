# CFA Level I Quiz App - Project Context

## Overview
The Open CFA project is a web application for CFA Level I exam preparation. It provides a quiz system based on a question bank organized by weeks and topics. The application allows users to take quizzes, practice individual questions, and track their progress.

## Database Structure

### PostgreSQL Database
- **Database Name**: cfa_db
- **User**: cfauser
- **Password**: cfaPass
- **Host**: localhost
- **Port**: 54320 (mapped to Docker container)
- **Connection Details**: Stored in environment variables via .env file

### Schema
The database schema includes the following tables:
- Questions
- Answer Options
- Explanations
- Topics
- Modules
- Learning Objectives
- Difficulty Levels
- Tags
- Weeks

## Question Bank Structure
- Organized in folders by weeks and topics (e.g., Week1_Quant_Ethics)
- Each week folder contains a `_questions.md` file with multiple questions in markdown format
- Questions have a title, question text, multiple choice options (A, B, C), tags, and an answer with explanation in a details/summary HTML element
- Questions are separated by horizontal rules (---)

## Application Components

### Main Application Files
- **quiz_app.py**: Main Streamlit application for taking quizzes
- **admin_dashboard.py**: Admin interface for managing questions and users
- **role_management.py**: Role-based access control functions
- **firebase_auth.py**: Authentication using Firebase
- **user_stats.py**: User statistics and progress tracking

### Database Utilities
- **database/import_questions.py**: Script for importing questions from markdown files
- **database/schema.sql**: Database schema definition

## Recent Changes

1. **Fixed Duplicate Widget ID Error**
   - Resolved issue with duplicate widget keys in the Streamlit application
   - Modified navigation buttons to prevent conflicts

2. **Code Formatting**
   - Applied ruff formatting to standardize code style across the project
   - Fixed whitespace issues and code formatting

3. **PostgreSQL Database Integration**
   - Set up PostgreSQL database in Docker container
   - Successfully imported questions from Weeks 1-3 (116 questions total)
   - Modified application to use PostgreSQL instead of SQLite

4. **Environment Variable Implementation**
   - Updated all application files to use database connection details from .env file
   - Added dotenv import and load_dotenv() call to each file
   - Removed hardcoded database credentials

5. **VS Code Configuration**
   - Created launch.json for debugging the import_questions.py script
   - Added configuration for command-line arguments

6. **Import Script Improvements**
   - Modified import_questions.py to only process files that end with '_questions.md'
   - Removed unused imports

## Environment Setup
- Python environment managed with uv
- Application runs in a Streamlit server
- PostgreSQL database runs in Docker
