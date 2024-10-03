from flask import Flask
import sqlite3
import click

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('class.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.cli.command('add')
@click.argument('NAME')
@click.argument('CLASS_ENROLED')
@click.argument('AREA')
@click.argument('JOINING_DATE')
def add(NAME, CLASS_ENROLED, AREA, JOINING_DATE):
    """Add a new student to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO stu (NAME, CLASS_ENROLED, AREA, JOINING_DATE) VALUES (?, ?,?,?)', (NAME, CLASS_ENROLED, AREA, JOINING_DATE))
    conn.commit()
    conn.close()
    click.echo(f'Student {NAME} added successfully.')

@app.cli.command('search')
@click.argument('name')
def search(name):
    """Search for a student by name."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stu WHERE name LIKE ?', ('%' + name + '%',))
    students = cursor.fetchall()
    conn.close()
    for student in students:
        click.echo(f'ID: {student["id"]}, Name: {student["name"]}, Area: {student["area"]}, Joining_Date: {student["JOINING_DATE"]}')

@app.cli.command('list')
def list():
    """List all students in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stu')
    students = cursor.fetchall()
    conn.close()
    for student in students:
        click.echo(f'ID: {student["id"]}, Name: {student["name"]}, Area: {student["area"]},ClassEnroled: {student["CLASS_ENROLED"]}, JOINING_DATE: {student["JOINING_DATE"]}, ')

@app.cli.command('delete')
@click.argument('student_id')
def delete(student_id):
    """Delete a student by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stu WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    click.echo(f'Student with ID {student_id} deleted successfully.')

if __name__ == '__main__':
    app.run(debug=True)
