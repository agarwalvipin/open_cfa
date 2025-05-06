# CFA Level I Quiz Application Context

## Application Overview
This is an open-source CFA Level I exam preparation application that provides a quiz platform for users to practice questions from the CFA curriculum. The application is built with Python using Streamlit for the frontend and PostgreSQL for the database.

## Key Features

### User Authentication
- Firebase authentication for user login/signup
- Role-based access (admin and regular users)
- Password reset functionality

### Quiz Functionality
- **Take Quiz**: Complete quizzes with multiple questions and get results at the end
- **Practice Question**: Individual question practice with immediate feedback
- Filter questions by topic, week, difficulty level, module, and tags
- Timer for quiz sessions
- Score tracking and performance statistics

### Question Management
- Import questions from markdown files
- PostgreSQL database for storing questions and user data
- Support for multiple question types and formats

### User Statistics
- Track quiz performance over time
- Badge system for achievements
- Performance visualization

## Database Structure
- PostgreSQL database running in Docker
- Tables for questions, answer options, explanations, topics, modules, learning objectives, difficulty levels, tags, and weeks
- Environment variables for database configuration

## Technical Implementation
- Python with Streamlit for the web interface
- PostgreSQL for database storage
- Docker for containerization
- Firebase for authentication and user data storage
- Makefile for easier application management

## Recent Changes

### Authentication and Session Management
- Enhanced persistent login functionality using browser localStorage and URL parameters
- Implemented robust error handling for authentication token validation
- Added automatic session restoration across page navigation and refreshes
- Fixed login form functionality to properly handle authentication tokens
- Improved logout process to properly clear authentication data

### Feature Enhancements
- Added Practice Question feature that provides immediate feedback after answering each question
- Fixed quiz starting functionality with proper handling of 'All' selection
- Improved error handling throughout the application

### Database and Configuration
- Updated database connection to use environment variables from .env file
- Switched from SQLite to PostgreSQL for better scalability
- Set up PostgreSQL database in Docker container

### Development Improvements
- Added Makefile for easier application management
- Removed debug messages from sidebar
- Modified import_questions.py to only process files that end with '_questions.md'
- Removed unused imports from import_questions.py
- Created VS Code launch.json configuration for easier debugging

## Created on: May 6, 2025
