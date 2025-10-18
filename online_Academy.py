import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# ایجاد اسکیمای OnlineAcademy
cur.execute("""
    CREATE SCHEMA IF NOT EXISTS OnlineAcademy;
""")

# جدول دانشجویان
cur.execute("""
    CREATE TABLE IF NOT EXISTS OnlineAcademy.students (
        student_id SERIAL PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE,
        enrollment_year INT CHECK (enrollment_year >= 2000),
        is_active BOOLEAN DEFAULT TRUE
    );
""")

# جدول دروس
cur.execute("""
    CREATE TABLE IF NOT EXISTS OnlineAcademy.courses (
        course_id SERIAL PRIMARY KEY,
        course_name VARCHAR(100) NOT NULL,
        department VARCHAR(50),
        credits INT CHECK (credits > 0)
    );
""")

# جدول نمرات
cur.execute("""
    CREATE TABLE IF NOT EXISTS OnlineAcademy.grades (
        grade_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES OnlineAcademy.students(student_id),
        course_id INT REFERENCES OnlineAcademy.courses(course_id),
        score DECIMAL(4,2) CHECK (score >= 0 AND score <= 20),
        grade_date DATE DEFAULT CURRENT_DATE
    );
""")

conn.commit()
cur.close()
conn.close()

