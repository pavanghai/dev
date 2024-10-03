import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('class.db')
cursor = conn.cursor()

# Create student table
cursor.execute('''
CREATE TABLE IF NOT EXISTS stu (
  ID INTEGER PRIMARY KEY,
  NAME TEXT,
  CLASS_ENROLED TEXT,
  AREA TEXT,
  JOINING_DATE TEXT
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO stu (NAME, CLASS_ENROLED, AREA, JOINING_DATE) VALUES (?, ?,?,?)
''', [
    ('Alice Smith', 'Math 101', 'North', '2023-09-01'),
    ('Bob Johnson', 'Physics 201', 'South', '2023-09-05'),
    ('Charlie Brown', 'English 101', 'East', '2023-09-10'),
    ('David Lee', 'Chemistry 101', 'West', '2023-09-15'),
    ('Emily Wilson', 'Biology 101', 'North', '2023-09-20'),
    ('Frank Davis', 'History 201', 'South', '2023-09-25'),
    ('Grace Garcia', 'Computer Science 101', 'East', '2023-10-01'),
    ('Henry Rodriguez', 'Art 101', 'West', '2023-10-05'),
    ('Isabella Martinez', 'Music 101', 'North', '2023-10-10'),
    ('Jack Anderson', 'Foreign Language 201', 'South', '2023-10-15'),
    ('Katherine Taylor', 'Psychology 101', 'East', '2023-10-20'),
    ('Liam Thomas', 'Sociology 101', 'West', '2023-10-25'),
    ('Mia Moore', 'Economics 101', 'North', '2023-11-01'),
    ('Noah Martin', 'Political Science 201', 'South', '2023-11-05'),
    ('Olivia Jackson', 'Communications 101', 'East', '2023-11-10'),
    ('Peter White', 'Business 101', 'West', '2023-11-15')
])

# Commit changes and close connection
conn.commit()
conn.close()
