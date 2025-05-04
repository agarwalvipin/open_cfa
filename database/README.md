# CFA Question Bank Database

This directory contains the PostgreSQL database schema and import tools for the CFA Question Bank.

## Schema Overview

The database schema is designed to store CFA exam questions with their metadata, answer options, and explanations. The main tables are:

- **topics**: Main subject areas (e.g., Ethical & Professional Standards, Quantitative Methods)
- **modules**: Specific modules within topics (e.g., Standard I(A) Knowledge of the Law)
- **readings**: Reading materials associated with questions
- **learning_objectives**: Learning outcome statements (LOS) for each module
- **questions**: The main question data including text, title, and metadata
- **answer_options**: Multiple choice options for each question
- **explanations**: Detailed explanations for the correct answers
- **tags**: Keywords associated with questions for easier searching
- **weeks**: Week numbers for organizing questions by study schedule

## Database Setup

1. Install PostgreSQL if you haven't already:
   ```bash
   sudo apt-get update
   sudo apt-get install postgresql postgresql-contrib
   ```

2. Create a new database:
   ```bash
   sudo -u postgres createdb cfa_questions
   ```

3. Apply the schema:
   ```bash
   sudo -u postgres psql -d cfa_questions -f schema.sql
   ```

## Importing Questions

The `import_questions.py` script parses the markdown question files and imports them into the PostgreSQL database.

### Prerequisites

1. Install required Python packages:
   ```bash
   pip install psycopg2-binary
   ```

2. Update the database connection parameters in the script if needed:
   ```python
   DB_PARAMS = {
       'dbname': 'cfa_questions',
       'user': 'postgres',
       'password': 'postgres',  # Change this to your actual password
       'host': 'localhost',
       'port': '5432'
   }
   ```

### Running the Import

```bash
python import_questions.py --directory /path/to/QuestionBank
```

For example:
```bash
python import_questions.py --directory /home/vipin/projects/open_cfa/QuestionBank
```

## Sample Queries

Here are some example queries to retrieve data from the database:

### Get all questions for a specific topic

```sql
SELECT q.question_id, q.title, q.question_text 
FROM questions q
JOIN topics t ON q.topic_id = t.topic_id
WHERE t.name = 'Ethical & Professional Standards';
```

### Get all questions with their correct answers

```sql
SELECT q.question_id, q.title, q.question_text, ao.option_letter, ao.option_text
FROM questions q
JOIN answer_options ao ON q.question_id = ao.question_id
WHERE ao.is_correct = true;
```

### Get questions by difficulty level

```sql
SELECT q.question_id, q.title, q.question_text
FROM questions q
JOIN difficulty_levels dl ON q.difficulty_id = dl.difficulty_id
WHERE dl.name = 'hard';
```

### Get questions by tag

```sql
SELECT q.question_id, q.title, q.question_text
FROM questions q
JOIN question_tags qt ON q.question_id = qt.question_id
JOIN tags t ON qt.tag_id = t.tag_id
WHERE t.name = 'Ethics';
```

### Get questions for a specific week

```sql
SELECT q.question_id, q.title, q.question_text
FROM questions q
JOIN weeks w ON q.week_id = w.week_id
WHERE w.week_number = 3;
```
