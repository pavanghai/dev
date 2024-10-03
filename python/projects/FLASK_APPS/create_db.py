import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('report.db')
cursor = conn.cursor()

# Create student table
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    area TEXT NOT NULL
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO student (name, area) VALUES (?, ?)
''', [
    ('Alice', 'Physics'),
    ('Bob', 'Chemistry'),
    ('Charlie', 'Mathematics')
])

# Commit changes and close connection
conn.commit()
conn.close()
