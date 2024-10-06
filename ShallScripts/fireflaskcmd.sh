#!/bin/bash

# Define paths and variables
DB_PATH="/e/Pavan/dev/python/projects/FLASK_APPS/class.db"
LOG_DIR="/e/Pavan/dev/python/projects/FLASK_APPS/logs"
FLASK_APP_DIR="/e/Pavan/dev/python/projects/FLASK_APPS"
VENV_ACTIVATE="E:/Pavan/dev/python/projects/FLASK_APPS/venv/Scripts/activate"
CURRENT_DATE=$(date +'%Y-%m-%d')  # Define current date
LOG_TIMESTAMP=$(date +'%Y%m%d %H:%M:%S')  # Define log timestamp
ERROR_CODE=0

# Log creation function
log_message() {
    echo "$LOG_TIMESTAMP - $1" >> "$LOG_DIR/$stuJDT/report_$(date +'%y%m%d').log"
}

# Error handling function
handle_error() {
    log_message "ERROR: Failed - $1"
    echo "ERROR: $1"
    exit 1
}

# Function to execute commands with logging
execute_command() {
    # Print and log the command being executed
    echo "Executing:"
    echo "    '$*'"  # Print the full command with arguments
    log_message "Executing:"
    log_message "    '$*'"  # Log the full command with arguments

    # Execute the command directly
    "$@" || handle_error "Failed to execute '$*'"
    
    log_message "Executed '$*' successfully"
}

# Step 1: Get ID and JOINING_DATE from the database
# stuID=$( /c/sqlite/sqlite3 "$DB_PATH" "SELECT rowid FROM stu WHERE JOINING_DATE <= '$CURRENT_DATE' ORDER BY JOINING_DATE DESC LIMIT 1;" ) || handle_error "Failed to get student ID"
# stuJDT=$( /c/sqlite/sqlite3 "$DB_PATH" "SELECT JOINING_DATE FROM stu WHERE rowid=$stuID;" ) || handle_error "Failed to get student JOINING_DATE"
# # Step 1: Get ID and JOINING_DATE from the database
# read stuID stuJDT < <( /c/sqlite/sqlite3 "$DB_PATH" "SELECT rowid, JOINING_DATE FROM stu WHERE JOINING_DATE <= '$CURRENT_DATE' ORDER BY JOINING_DATE DESC LIMIT 1;" ) || handle_error "Failed to get student ID and JOINING_DATE"
# result=$( /c/sqlite/sqlite3 "$DB_PATH" "SELECT rowid, JOINING_DATE FROM stu WHERE JOINING_DATE <= '$CURRENT_DATE' ORDER BY JOINING_DATE DESC LIMIT 1;" ) || handle_error "Failed to get student ID and JOINING_DATE"

# Read stuID and stuJDT from the result
# read stuID stuJDT <<< "$result"

query="SELECT rowid, JOINING_DATE FROM stu WHERE JOINING_DATE <= '$CURRENT_DATE' ORDER BY JOINING_DATE DESC LIMIT 1;"
read stuID stuJDT < <(/c/sqlite/sqlite3 -separator ' ' "${DB_PATH}" "${query}")

echo "ID: $stuID" "JDT: $stuJDT" 

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR/$stuJDT" || handle_error "Failed to create log directory"

log_message "Log started for student with ID: $stuID and JOINING_DATE: $stuJDT"

# Step 3: Activate virtual environment
cd "$FLASK_APP_DIR" || handle_error "Failed to change directory to $FLASK_APP_DIR"
source "$VENV_ACTIVATE" || handle_error "Failed to activate virtual environment"

# Step 4: Execute Flask commands
log_message "Executing Flask commands"
execute_command flask list
# execute_command flask add "Nitin" "tenth" "Vashi" "2024-08-25"
execute_command flask delete $((stuID - 10))
execute_command flask list

# Step 5: Deactivate virtual environment
deactivate || handle_error "Failed to deactivate virtual environment"

# Step 6: Print log creation details
echo "Log created at: $LOG_DIR/$stuJDT/report_$(date +'%y%m%d').log"
log_message "Script completed successfully."
