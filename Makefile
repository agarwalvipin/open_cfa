# Makefile for CFA Quiz Application

.PHONY: build run stop restart logs shell clean update-context help import-questions

# Default target
.DEFAULT_GOAL := help

# Variables
CONTAINER_NAME = quiz-app
IMAGE_NAME = cfa-quiz-app
PORT = 9501
QUESTION_DIR = question_bank

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the application in Docker
run:
	docker run -d --name $(CONTAINER_NAME) \
		-p $(PORT):8501 \
		--network main_network \
		-e DB_NAME=cfa_db \
		-e DB_USER=cfauser \
		-e DB_PASSWORD=cfaPass \
		-e DB_HOST=db \
		-e DB_PORT=5432 \
		-v $(PWD)/firebase-credentials.json:/app/firebase-credentials.json:ro \
		--restart unless-stopped \
		$(IMAGE_NAME)

# Stop the Docker container
stop:
	docker stop $(CONTAINER_NAME)

# Remove the Docker container
rm:
	docker rm -f $(CONTAINER_NAME) || true

# Restart the Docker container
restart: stop
	docker start $(CONTAINER_NAME)

# Full rebuild and restart
rebuild: rm build
	make run

# View container logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Open a shell in the container
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Clean up Docker resources
clean: rm
	docker rmi $(IMAGE_NAME)

# Run the application locally with Python
run-local:
	cd $(PWD) && streamlit run quiz_app.py

# Import questions from question bank
import-questions:
	cd $(PWD) && python database/import_questions.py --directory $(QUESTION_DIR)

# Update CONTEXT.md with latest changes
update-context:
	@echo "Updating CONTEXT.md with latest changes..."
	@if [ -f CONTEXT.md ]; then \
		echo "\n## Updated on $$(date)\n" >> CONTEXT.md; \
		echo "Recent changes:" >> CONTEXT.md; \
		echo "- Fixed quiz starting functionality with proper handling of 'All' selection" >> CONTEXT.md; \
		echo "- Removed debug messages from sidebar" >> CONTEXT.md; \
		echo "- Added Makefile for easier application management" >> CONTEXT.md; \
	else \
		echo "CONTEXT.md file not found"; \
	fi

# Display help information
help:
	@echo "CFA Quiz Application Makefile Commands:"
	@echo ""
	@echo "  make build           - Build the Docker image"
	@echo "  make run             - Run the application in Docker"
	@echo "  make stop            - Stop the Docker container"
	@echo "  make rm              - Remove the Docker container"
	@echo "  make restart         - Restart the Docker container"
	@echo "  make rebuild         - Rebuild and restart the container"
	@echo "  make logs            - View container logs"
	@echo "  make shell           - Open a shell in the container"
	@echo "  make clean           - Clean up Docker resources"
	@echo "  make run-local       - Run the application locally with Python"
	@echo "  make import-questions - Import questions from question bank"
	@echo "  make update-context  - Update CONTEXT.md with latest changes"
	@echo "  make help            - Display this help information"
