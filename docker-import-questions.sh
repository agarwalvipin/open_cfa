#!/bin/bash

# This script helps import questions into the Docker container

# Ensure the container is running
echo "Ensuring containers are running..."
docker-compose up -d

# Check if QuestionBank directory exists
if [ ! -d "./QuestionBank" ]; then
  echo "Error: QuestionBank directory not found in the current directory."
  echo "Please ensure your question bank is available before running this script."
  exit 1
fi

# Copy the QuestionBank directory to the container
echo "Copying QuestionBank to container..."
CONTAINER_ID=$(docker-compose ps -q quiz-app)
docker cp ./QuestionBank "$CONTAINER_ID":/app/

# Run the import script inside the container
echo "Running import script..."
docker exec "$CONTAINER_ID" python -m database.import_questions --directory /app/QuestionBank

echo "Import process completed!"
