
CREATE SCHEMA IF NOT EXISTS OnlineAcademy;

CREATE TABLE IF NOT EXISTS OnlineAcademy.students (
    student_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    enrollment_year INT CHECK (enrollment_year >= 2000),
    is_active BOOLEAN DEFAULT TRUE
);
CREATE TABLE IF NOT EXISTS OnlineAcademy.courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    credits INT CHECK (credits > 0)
);
CREATE TABLE IF NOT EXISTS OnlineAcademy.grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES OnlineAcademy.students(student_id),
    course_id INT REFERENCES OnlineAcademy.courses(course_id),
    score DECIMAL(4,2) CHECK (score >= 0 AND score <= 20),
    grade_date DATE DEFAULT CURRENT_DATE
);
