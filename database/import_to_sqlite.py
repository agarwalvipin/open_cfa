#!/usr/bin/env python3

'''
Script to import CFA questions from markdown files into SQLite database
'''

import os
import re
import sqlite3
import argparse
from pathlib import Path

def create_database(db_path, schema_path):
    """Create SQLite database from schema file"""
    conn = sqlite3.connect(db_path)
    
    # Check if tables already exist
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='topics'")
    tables_exist = cursor.fetchone() is not None
    
    if not tables_exist:
        # Only create tables if they don't exist
        with open(schema_path, 'r') as f:
            schema_sql = f.read()
        
        conn.executescript(schema_sql)
        conn.commit()
        print("Database schema created.")
    else:
        print("Database already exists, skipping schema creation.")
    
    return conn

def parse_metadata(metadata_text):
    """Parse metadata section from question"""
    metadata = {}
    lines = metadata_text.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('- '):
            parts = line[2:].split(':', 1)
            if len(parts) == 2:
                key, value = parts[0].strip(), parts[1].strip()
                metadata[key] = value
            else:
                # Handle tags which are in format: - tags: [tag1, tag2, tag3]
                if line.startswith('- tags:'):
                    tags_str = line[8:].strip()
                    # Extract tags from [tag1, tag2, tag3] format
                    if tags_str.startswith('[') and tags_str.endswith(']'):
                        tags = [tag.strip() for tag in tags_str[1:-1].split(',')]
                        metadata['tags'] = tags
    return metadata

def parse_question_text(question_text):
    """Parse question text and answer options"""
    lines = question_text.strip().split('\n')
    
    # Extract the question text (everything before the first option)
    question_lines = []
    i = 0
    while i < len(lines) and not lines[i].strip().startswith('- '):
        question_lines.append(lines[i])
        i += 1
    
    question = '\n'.join(question_lines).strip()
    
    # Extract options
    options = []
    while i < len(lines):
        if lines[i].strip().startswith('- '):
            option_text = lines[i].strip()[2:]
            # Parse option letter and text (e.g., "A) Option text" -> "A", "Option text")
            match = re.match(r'([A-D])\)(.*)', option_text)
            if match:
                letter, text = match.groups()
                options.append((letter, text.strip()))
        i += 1
    
    return question, options

def parse_answer_explanation(explanation_text):
    """Parse answer and explanation"""
    correct_answer = None
    explanation = ""
    
    lines = explanation_text.strip().split('\n')
    for i, line in enumerate(lines):
        if "Correct Answer:" in line:
            # Extract the correct answer letter
            match = re.search(r'Correct Answer:\s*([A-D])', line)
            if match:
                correct_answer = match.group(1)
        
        # Extract explanation (everything after "Explanation:")
        if "Explanation:" in line and i+1 < len(lines):
            explanation = '\n'.join(lines[i+1:]).strip()
            break
    
    return correct_answer, explanation

def parse_question_file(file_path):
    """Parse a markdown file containing questions"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the file by horizontal rule to get individual questions
    questions_raw = content.split('---')
    
    questions = []
    for q_raw in questions_raw:
        if not q_raw.strip():
            continue
        
        # Extract title
        title_match = re.search(r'##\s*(.*?)\n', q_raw)
        title = title_match.group(1).strip() if title_match else ""
        
        # Extract metadata
        metadata_match = re.search(r'<details>\s*<summary>Meta Data</summary>\s*(.*?)\s*</details>', q_raw, re.DOTALL)
        metadata = {}
        if metadata_match:
            metadata = parse_metadata(metadata_match.group(1))
        
        # Extract question text and options
        question_match = re.search(r'</details>\s*\n\n(.*?)\n\n<details>', q_raw, re.DOTALL)
        question_text = ""
        options = []
        if question_match:
            question_text, options = parse_question_text(question_match.group(1))
        
        # Extract answer and explanation
        explanation_match = re.search(r'<summary>✅ Answer & Explanation</summary>\s*(.*?)\s*(?:</details>|$)', q_raw, re.DOTALL)
        correct_answer = None
        explanation = ""
        if explanation_match:
            correct_answer, explanation = parse_answer_explanation(explanation_match.group(1))
        
        # Extract week from file path
        week_match = re.search(r'Week(\d+)', file_path)
        week = int(week_match.group(1)) if week_match else None
        
        questions.append({
            'title': title,
            'question_text': question_text,
            'options': options,
            'correct_answer': correct_answer,
            'explanation': explanation,
            'metadata': metadata,
            'week': week
        })
    
    return questions

def get_or_create_id(conn, table, column, value, return_column='rowid'):
    """Get ID for a value or create it if it doesn't exist"""
    cursor = conn.cursor()
    
    # Try to get existing ID
    cursor.execute(f"SELECT {return_column} FROM {table} WHERE {column} = ?", (value,))
    result = cursor.fetchone()
    
    if result:
        return result[0]
    
    # Create new entry
    cursor.execute(f"INSERT INTO {table} ({column}) VALUES (?)", (value,))
    conn.commit()
    return cursor.lastrowid

def import_questions_to_db(questions, conn):
    """Import parsed questions into the database"""
    cursor = conn.cursor()
    
    for question in questions:
        # Get or create topic
        topic_id = None
        if 'topic' in question['metadata']:
            topic_id = get_or_create_id(conn, 'topics', 'name', question['metadata']['topic'], 'topic_id')
        
        # Get or create module
        module_id = None
        if 'module' in question['metadata'] and topic_id:
            cursor.execute(
                "SELECT module_id FROM modules WHERE name = ? AND topic_id = ?",
                (question['metadata']['module'], topic_id)
            )
            result = cursor.fetchone()
            
            if result:
                module_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO modules (name, topic_id) VALUES (?, ?)",
                    (question['metadata']['module'], topic_id)
                )
                module_id = cursor.lastrowid
        
        # Get or create reading
        reading_id = None
        if 'reading' in question['metadata']:
            reading_id = get_or_create_id(conn, 'readings', 'name', question['metadata']['reading'], 'reading_id')
        
        # Get or create learning objective
        los_id = None
        if 'los_text' in question['metadata'] and module_id:
            cursor.execute(
                "SELECT los_id FROM learning_objectives WHERE text = ?",
                (question['metadata']['los_text'],)
            )
            result = cursor.fetchone()
            
            if result:
                los_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO learning_objectives (text, module_id) VALUES (?, ?)",
                    (question['metadata']['los_text'], module_id)
                )
                los_id = cursor.lastrowid
        
        # Get question type
        question_type_id = None
        if 'question_type' in question['metadata']:
            question_type_id = get_or_create_id(
                conn, 'question_types', 'name', 
                question['metadata']['question_type'], 'question_type_id'
            )
        
        # Get difficulty level
        difficulty_id = None
        if 'difficulty' in question['metadata']:
            difficulty_id = get_or_create_id(
                conn, 'difficulty_levels', 'name',
                question['metadata']['difficulty'], 'difficulty_id'
            )
        
        # Get or create week
        week_id = None
        if question['week']:
            cursor.execute("SELECT week_id FROM weeks WHERE week_number = ?", (question['week'],))
            result = cursor.fetchone()
            
            if result:
                week_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO weeks (week_number) VALUES (?)",
                    (question['week'],)
                )
                week_id = cursor.lastrowid
        
        # Insert question
        level = int(question['metadata'].get('level', 1))
        external_id = question['metadata'].get('id', None)
        
        cursor.execute(
            """
            INSERT INTO questions (
                external_id, title, question_text, level, reading_id, topic_id, 
                module_id, los_id, question_type_id, difficulty_id, week_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                external_id, question['title'], question['question_text'], level, reading_id,
                topic_id, module_id, los_id, question_type_id, difficulty_id, week_id
            )
        )
        question_id = cursor.lastrowid
        
        # Insert options
        for letter, text in question['options']:
            is_correct = 1 if letter == question['correct_answer'] else 0
            cursor.execute(
                "INSERT INTO answer_options (question_id, option_letter, option_text, is_correct) VALUES (?, ?, ?, ?)",
                (question_id, letter, text, is_correct)
            )
        
        # Insert explanation
        if question['explanation']:
            cursor.execute(
                "INSERT INTO explanations (question_id, explanation_text) VALUES (?, ?)",
                (question_id, question['explanation'])
            )
        
        # Insert tags
        if 'tags' in question['metadata']:
            for tag_name in question['metadata']['tags']:
                tag_id = get_or_create_id(conn, 'tags', 'name', tag_name, 'tag_id')
                try:
                    cursor.execute(
                        "INSERT INTO question_tags (question_id, tag_id) VALUES (?, ?)",
                        (question_id, tag_id)
                    )
                except sqlite3.IntegrityError:
                    # Ignore duplicate entries
                    pass
    
    conn.commit()

def main():
    parser = argparse.ArgumentParser(description='Import CFA questions from markdown file into SQLite')
    parser.add_argument('--file', '-f', required=True, help='Markdown file containing questions')
    parser.add_argument('--db', '-d', default='cfa_questions.db', help='SQLite database file to create')
    parser.add_argument('--schema', '-s', default='sqlite_schema.sql', help='Schema file for SQLite database')
    args = parser.parse_args()
    
    # Create database and tables
    conn = create_database(args.db, args.schema)
    
    try:
        # Parse and import questions
        print(f"Processing {args.file}...")
        questions = parse_question_file(args.file)
        print(f"Found {len(questions)} questions")
        import_questions_to_db(questions, conn)
        print(f"Imported questions from {args.file}")
        
        # Print some stats
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM questions")
        question_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM answer_options")
        option_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM topics")
        topic_count = cursor.fetchone()[0]
        
        print(f"\nDatabase Summary:")
        print(f"- {question_count} questions")
        print(f"- {option_count} answer options")
        print(f"- {topic_count} topics")
        
        print("\nImport completed successfully")
    
    except Exception as e:
        print(f"Error during import: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
