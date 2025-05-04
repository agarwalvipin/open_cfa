-- PostgreSQL schema for CFA Question Bank

CREATE TABLE topics (
    topic_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE modules (
    module_id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics(topic_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    UNIQUE(topic_id, name)
);

CREATE TABLE readings (
    reading_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE learning_objectives (
    los_id SERIAL PRIMARY KEY,
    text TEXT NOT NULL UNIQUE,
    module_id INTEGER REFERENCES modules(module_id)
);

CREATE TABLE difficulty_levels (
    difficulty_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE question_types (
    question_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE weeks (
    week_id SERIAL PRIMARY KEY,
    week_number INTEGER NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE questions (
    question_id SERIAL PRIMARY KEY,
    external_id VARCHAR(50) UNIQUE,  -- e.g., ETHICS_L1_W3_Revised_1
    title TEXT NOT NULL,
    question_text TEXT NOT NULL,
    level INTEGER NOT NULL,
    reading_id INTEGER REFERENCES readings(reading_id),
    topic_id INTEGER REFERENCES topics(topic_id),
    module_id INTEGER REFERENCES modules(module_id),
    los_id INTEGER REFERENCES learning_objectives(los_id),
    question_type_id INTEGER REFERENCES question_types(question_type_id),
    difficulty_id INTEGER REFERENCES difficulty_levels(difficulty_id),
    week_id INTEGER REFERENCES weeks(week_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE answer_options (
    option_id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(question_id) ON DELETE CASCADE,
    option_letter CHAR(1) NOT NULL,  -- A, B, C, D
    option_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE(question_id, option_letter)
);

CREATE TABLE explanations (
    explanation_id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(question_id) ON DELETE CASCADE,
    explanation_text TEXT NOT NULL,
    UNIQUE(question_id)
);

CREATE TABLE question_tags (
    question_id INTEGER REFERENCES questions(question_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (question_id, tag_id)
);

-- Initial data for difficulty levels
INSERT INTO difficulty_levels (name) VALUES 
    ('easy'), 
    ('medium'), 
    ('hard');

-- Initial data for question types
INSERT INTO question_types (name, description) VALUES 
    ('mcq', 'Multiple Choice Question'),
    ('calculation', 'Calculation-based Question'),
    ('case', 'Case Study Question');

-- Create indexes for better query performance
CREATE INDEX idx_questions_topic ON questions(topic_id);
CREATE INDEX idx_questions_module ON questions(module_id);
CREATE INDEX idx_questions_difficulty ON questions(difficulty_id);
CREATE INDEX idx_questions_week ON questions(week_id);
CREATE INDEX idx_questions_external_id ON questions(external_id);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger to automatically update the updated_at column
CREATE TRIGGER update_questions_modtime
    BEFORE UPDATE ON questions
    FOR EACH ROW
    EXECUTE FUNCTION update_modified_column();
