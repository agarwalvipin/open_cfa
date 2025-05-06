#!/usr/bin/env python3

"""Script to import CFA questions from markdown files into PostgreSQL database"""

import argparse
import os
import re

import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from environment variables
DB_PARAMS = {
    "dbname": os.getenv("DB_NAME", "cfa_db"),
    "user": os.getenv("DB_USER", "cfauser"),
    "password": os.getenv("DB_PASSWORD", "cfaPass"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "54320"),  # Port mapped to Docker container
}


def connect_to_db():
    """Connect to PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def parse_metadata(metadata_text):
    """Parse metadata section from question"""
    metadata = {}
    lines = metadata_text.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("- "):
            parts = line[2:].split(":", 1)
            if len(parts) == 2:
                key, value = parts[0].strip(), parts[1].strip()
                metadata[key] = value
            else:
                # Handle tags which are in format: - tags: [tag1, tag2, tag3]
                if line.startswith("- tags:"):
                    tags_str = line[8:].strip()
                    # Extract tags from [tag1, tag2, tag3] format
                    if tags_str.startswith("[") and tags_str.endswith("]"):
                        tags = [tag.strip() for tag in tags_str[1:-1].split(",")]
                        metadata["tags"] = tags
    return metadata


def parse_question_text(question_text):
    """Parse question text and answer options"""
    lines = question_text.strip().split("\n")

    # Extract the question text (everything before the first option)
    question_lines = []
    i = 0
    while i < len(lines) and not lines[i].strip().startswith("- "):
        question_lines.append(lines[i])
        i += 1

    question = "\n".join(question_lines).strip()

    # Extract options
    options = []
    while i < len(lines):
        if lines[i].strip().startswith("- "):
            option_text = lines[i].strip()[2:]
            # Parse option letter and text (e.g., "A) Option text" -> "A", "Option text")
            match = re.match(r"([A-D])\)(.*)", option_text)
            if match:
                letter, text = match.groups()
                options.append((letter, text.strip()))
        i += 1

    return question, options


def parse_answer_explanation(explanation_text):
    """Parse answer and explanation"""
    correct_answer = None
    explanation = ""

    lines = explanation_text.strip().split("\n")
    for i, line in enumerate(lines):
        if "Correct Answer:" in line:
            # Extract the correct answer letter
            match = re.search(r"Correct Answer:\s*([A-D])", line)
            if match:
                correct_answer = match.group(1)

        # Extract explanation (everything after "Explanation:")
        if "Explanation:" in line and i + 1 < len(lines):
            explanation = "\n".join(lines[i + 1 :]).strip()
            break

    return correct_answer, explanation


def parse_question_file(file_path):
    """Parse a markdown file containing questions"""
    with open(file_path, encoding="utf-8") as file:
        content = file.read()

    # Split the file by horizontal rule to get individual questions
    questions_raw = content.split("---")

    questions = []
    for q_raw in questions_raw:
        if not q_raw.strip():
            continue

        # Extract title
        title_match = re.search(r"##\s*(.*?)\n", q_raw)
        title = title_match.group(1).strip() if title_match else ""

        # Extract metadata
        metadata_match = re.search(
            r"<details>\s*<summary>Meta Data</summary>\s*(.*?)\s*</details>",
            q_raw,
            re.DOTALL,
        )
        metadata = {}
        if metadata_match:
            metadata = parse_metadata(metadata_match.group(1))

        # Extract question text and options
        question_match = re.search(
            r"</details>\s*\n\n(.*?)\n\n<details>", q_raw, re.DOTALL,
        )
        question_text = ""
        options = []
        if question_match:
            question_text, options = parse_question_text(question_match.group(1))

        # Extract answer and explanation
        explanation_match = re.search(
            r"<summary>✅ Answer & Explanation</summary>\s*(.*?)\s*(?:</details>|$)",
            q_raw,
            re.DOTALL,
        )
        correct_answer = None
        explanation = ""
        if explanation_match:
            correct_answer, explanation = parse_answer_explanation(
                explanation_match.group(1),
            )

        # Extract week from file path
        week_match = re.search(r"Week(\d+)", file_path)
        week = int(week_match.group(1)) if week_match else None

        questions.append(
            {
                "title": title,
                "question_text": question_text,
                "options": options,
                "correct_answer": correct_answer,
                "explanation": explanation,
                "metadata": metadata,
                "week": week,
            },
        )

    return questions


def get_or_create_id(conn, table, column, value, return_column="id"):
    """Get ID for a value or create it if it doesn't exist"""
    cursor = conn.cursor()

    # Try to get existing ID
    cursor.execute(f"SELECT {return_column} FROM {table} WHERE {column} = %s", (value,))
    result = cursor.fetchone()

    if result:
        return result[0]

    # Create new entry
    cursor.execute(
        f"INSERT INTO {table} ({column}) VALUES (%s) RETURNING {return_column}",
        (value,),
    )
    conn.commit()
    return cursor.fetchone()[0]


def import_questions_to_db(questions, conn):
    """Import parsed questions into the database"""
    cursor = conn.cursor()

    for question in questions:
        # Get or create topic
        topic_id = None
        if "topic" in question["metadata"]:
            topic_id = get_or_create_id(
                conn, "topics", "name", question["metadata"]["topic"], "topic_id",
            )

        # Get or create module
        module_id = None
        if "module" in question["metadata"] and topic_id:
            cursor.execute(
                "SELECT module_id FROM modules WHERE name = %s AND topic_id = %s",
                (question["metadata"]["module"], topic_id),
            )
            result = cursor.fetchone()

            if result:
                module_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO modules (name, topic_id) VALUES (%s, %s) RETURNING module_id",
                    (question["metadata"]["module"], topic_id),
                )
                module_id = cursor.fetchone()[0]

        # Get or create reading
        reading_id = None
        if "reading" in question["metadata"]:
            reading_id = get_or_create_id(
                conn, "readings", "name", question["metadata"]["reading"], "reading_id",
            )

        # Get or create learning objective
        los_id = None
        if "los_text" in question["metadata"] and module_id:
            cursor.execute(
                "SELECT los_id FROM learning_objectives WHERE text = %s",
                (question["metadata"]["los_text"],),
            )
            result = cursor.fetchone()

            if result:
                los_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO learning_objectives (text, module_id) VALUES (%s, %s) RETURNING los_id",
                    (question["metadata"]["los_text"], module_id),
                )
                los_id = cursor.fetchone()[0]

        # Get question type
        question_type_id = None
        if "question_type" in question["metadata"]:
            question_type_id = get_or_create_id(
                conn,
                "question_types",
                "name",
                question["metadata"]["question_type"],
                "question_type_id",
            )

        # Get difficulty level
        difficulty_id = None
        if "difficulty" in question["metadata"]:
            difficulty_id = get_or_create_id(
                conn,
                "difficulty_levels",
                "name",
                question["metadata"]["difficulty"],
                "difficulty_id",
            )

        # Get or create week
        week_id = None
        if question["week"]:
            cursor.execute(
                "SELECT week_id FROM weeks WHERE week_number = %s", (question["week"],),
            )
            result = cursor.fetchone()

            if result:
                week_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO weeks (week_number) VALUES (%s) RETURNING week_id",
                    (question["week"],),
                )
                week_id = cursor.fetchone()[0]

        # Insert question
        level = int(question["metadata"].get("level", 1))
        external_id = question["metadata"].get("id", None)

        cursor.execute(
            """
            INSERT INTO questions (
                external_id, title, question_text, level, reading_id, topic_id, 
                module_id, los_id, question_type_id, difficulty_id, week_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING question_id
            """,
            (
                external_id,
                question["title"],
                question["question_text"],
                level,
                reading_id,
                topic_id,
                module_id,
                los_id,
                question_type_id,
                difficulty_id,
                week_id,
            ),
        )
        question_id = cursor.fetchone()[0]

        # Insert options
        for letter, text in question["options"]:
            is_correct = letter == question["correct_answer"]
            cursor.execute(
                "INSERT INTO answer_options (question_id, option_letter, option_text, is_correct) VALUES (%s, %s, %s, %s)",
                (question_id, letter, text, is_correct),
            )

        # Insert explanation
        if question["explanation"]:
            cursor.execute(
                "INSERT INTO explanations (question_id, explanation_text) VALUES (%s, %s)",
                (question_id, question["explanation"]),
            )

        # Insert tags
        if "tags" in question["metadata"]:
            for tag_name in question["metadata"]["tags"]:
                tag_id = get_or_create_id(conn, "tags", "name", tag_name, "tag_id")
                cursor.execute(
                    "INSERT INTO question_tags (question_id, tag_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                    (question_id, tag_id),
                )

    conn.commit()


def main():
    parser = argparse.ArgumentParser(
        description="Import CFA questions from markdown files into PostgreSQL",
    )
    parser.add_argument(
        "--directory",
        "-d",
        required=True,
        help="Directory containing question markdown files",
    )
    args = parser.parse_args()

    conn = connect_to_db()
    if not conn:
        return

    try:
        # Find all markdown files in the directory that end with _questions.md
        question_files = []
        for root, _, files in os.walk(args.directory):
            for file in files:
                if file.endswith("_questions.md"):
                    question_files.append(os.path.join(root, file))

        print(f"Found {len(question_files)} question files")

        # Parse and import each file
        for file_path in question_files:
            print(f"Processing {file_path}...")
            questions = parse_question_file(file_path)
            print(f"  Found {len(questions)} questions")
            import_questions_to_db(questions, conn)
            print(f"  Imported questions from {file_path}")

        print("Import completed successfully")

    except Exception as e:
        print(f"Error during import: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
