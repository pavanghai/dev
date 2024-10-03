#!/bin/bash

# Variables
curDate=$(date +"%Y-%m-%d")
logDate=$(date +"%y%m%d")
DATABASE="/e/Pavan/dev/python/projects/FLASK_APPS/report.db"
LOG_DIR="/e/Pavan/dev/python/projects/FLASK_APPS/logs/$curDate"
LOG_FILE="$LOG_DIR/script_$logDate.log"

# Create log directory and file
mkdir -p "$LOG_DIR"

# Log function to include timestamp
log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" | tee -a "$LOG_FILE"
}

# Command execution function with error handling
run_cmd() {
    log "Executing: $1"
    eval $1 2>>"$LOG_FILE"
    if [ $? -ne 0 ]; then
        log "Error executing: $1"
    fi
}

# Activate virtual environment using source for Git Bash
run_cmd "cd /e/Pavan/dev/python/projects/FLASK_APPS && source venv/Scripts/activate"

# Check if SQLite3 is installed
if ! command -v sqlite3 &> /dev/null
then
    log "Error: sqlite3 is not installed or not found in PATH"
    exit 1
fi

# Extract ID and name from student table based on 'Chemistry'
student_info=$(sqlite3 "$DATABASE" "SELECT ID, name FROM student WHERE area='Chemistry' LIMIT 1;")
var_ID=$(echo $student_info | awk '{print $1}')
var_name=$(echo $student_info | awk '{print $2}')

# Log extracted data
log "Extracted ID: $var_ID, Name: $var_name"

# Run flask commands
run_cmd "flask add_student 'raj' 'sharma'"
run_cmd "flask delete-student $var_ID"
run_cmd "flask list-students"
run_cmd "flask search-student $var_name"

# Deactivate virtual environment
run_cmd "deactivate"

log "Script execution completed."
