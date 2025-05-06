FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for Python package management
RUN pip install uv

# Copy requirements and install dependencies with uv
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy only the necessary application files
COPY quiz_app.py .
COPY admin_dashboard.py .
COPY firebase_auth.py .
COPY user_stats.py .
COPY role_management.py .
COPY .env .
COPY firebase-credentials.json .
COPY database/ ./database/

# Create .streamlit directory
RUN mkdir -p .streamlit

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "quiz_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
