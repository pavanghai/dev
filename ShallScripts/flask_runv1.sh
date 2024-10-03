#!/bin/bash

# Variables
curDate=$(date +"%Y-%m-%d")
logDate=$(date +"%y%m%d")
DATABASE="E:/Pavan/dev/python/projects/FLASK_APPS/report.db"
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

# Activate virtual environment
run_cmd "cd /e/Pavan/dev/python/projects/FLASK_APPS && source venv/Scripts/activate"

# Extract ID and name from student table using Python
student_info=$(python - << END
import sqlite3
conn = sqlite3.connect("$DATABASE")
cur = conn.cursor()
cur.execute("SELECT ID, name FROM student WHERE area='Chemistry' LIMIT 1;")
row = cur.fetchone()
if row:
    print(f"{row[0]} {row[1]}")
else:
    print("")
conn.close()
END
)

var_ID=$(echo $student_info | awk '{print $1}')
var_name=$(echo $student_info | awk '{print $2}')

# Log extracted data
log "Extracted ID: $var_ID, Name: $var_name"

# Run flask commands
run_cmd "flask add_student 'raj' 'Chemistry'"
run_cmd "flask delete-student $var_ID"
run_cmd "flask list-students"
run_cmd "flask search-student $var_name"

# Deactivate virtual environment
run_cmd "deactivate"

log "Script execution completed."
