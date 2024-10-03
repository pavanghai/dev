from flask import Flask
import sqlite3
import click

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('report.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.cli.command('add-student')
@click.argument('name')
@click.argument('area')
def add_student(name, area):
    """Add a new student to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO student (name, area) VALUES (?, ?)', (name, area))
    conn.commit()
    conn.close()
    click.echo(f'Student {name} added successfully.')

@app.cli.command('search-student')
@click.argument('name')
def search_student(name):
    """Search for a student by name."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student WHERE name LIKE ?', ('%' + name + '%',))
    students = cursor.fetchall()
    conn.close()
    for student in students:
        click.echo(f'ID: {student["id"]}, Name: {student["name"]}, Area: {student["area"]}')

@app.cli.command('list-students')
def list_students():
    """List all students in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student')
    students = cursor.fetchall()
    conn.close()
    for student in students:
        click.echo(f'ID: {student["id"]}, Name: {student["name"]}, Area: {student["area"]}')

@app.cli.command('delete-student')
@click.argument('student_id')
def delete_student(student_id):
    """Delete a student by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM student WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    click.echo(f'Student with ID {student_id} deleted successfully.')

if __name__ == '__main__':
    app.run(debug=True)
