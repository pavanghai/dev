#!/bin/bash

# Variables
curDate=$(date +"%Y-%m-%d")
logDate=$(date +"%y%m%d")
DATABASE="/e/Pavan/dev/python/projects/FLASK_APPS/class.db"

LOG_DIR="/e/Pavan/dev/python/projects/FLASK_APPS/logs/$curDate"
LOG_FILE="$LOG_DIR/script_$logDate.log"

# Create log directory and file
mkdir -p "$LOG_DIR"

# Log function to include timestamp
log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" | tee -a "$LOG_FILE"
}

# Command execution function with error handling (capturing both stdout and stderr)
run_cmd() {
    log "Executing: $1"
    eval $1 >> "$LOG_FILE" 2>&1
    if [ $? -ne 0 ]; then
        log "Error executing: $1"
    fi
}

# Flask command execution with error handling, stop script on error
run_flask_cmd() {
    log "Executing Flask command: $1"
    flask_output=$(eval $1 2>&1)
    exit_code=$?  # Capture the exit code
    if [ $exit_code -ne 0 ]; then
        log "Flask command error: $flask_output"
        log "Exit code: $exit_code"  # Log the exit code
        exit $exit_code  # Stop the script and return the exit code
    else
        log "Flask command output: $flask_output"
    fi
}

# Activate virtual environment
run_cmd "cd /e/Pavan/dev/python/projects/FLASK_APPS && source venv/Scripts/activate"

# Extract ID and name from student table using Python
student_info=$(python - << END
import sqlite3
try:
    conn = sqlite3.connect("$DATABASE")
    cur = conn.cursor()
    cur.execute("SELECT ID, name FROM stu WHERE area='North' LIMIT 1;")
    row = cur.fetchone()
    if row:
        print(f"{row[0]} {row[1]}")
    else:
        print("")
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
END
)

# Check if student_info contains an error
if [[ $student_info == *"Error"* ]]; then
    log "Error in Python execution: $student_info"
    exit 1
fi

var_ID=$(echo $student_info | awk '{print $1}')
var_name=$(echo $student_info | awk '{print $2}')

# Log extracted data
log "Extracted ID: $var_ID, Name: $var_name"

# Run flask commands and stop script if any command fails
#run_flask_cmd "flask add 'raj' 'sharma'"
#run_flask_cmd "flask delete $var_ID"
run_flask_cmd "flask list"
# run_flask_cmd "flask search-student $var_name"

# Deactivate virtual environment
run_cmd "deactivate"

log "Script execution completed."
