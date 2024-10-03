# Created Flask minimal project with
1. created virtual environment, activated, install packages
   python -m venv venv
   venv\Scripts\activate
   pip install Flask
2. create scripts create_db.py, app.py
   This will also create report.db
3. Start executing flask cli
   flask --help
      add-student     Add a new student to the database.
      delete-student  Delete a student by ID.
      list-students   List all students in the database.
      routes          Show the routes for the app.
      run             Run a development server.
      search-student  Search for a student by name.
      shell           Run a shell in the app context.

   flask add_student "name" "area" 
   flask delete-student <ID>  Delete a student by ID.
   flask list-students
   flask search-student <name>

   flask routes          Show the routes for the app.
   flask run             Run a development server.
   flask shell           Run a shell in the app context.
3. deactivate
4. move up 2 folders 
     E:\Pavan\dev\python>
5. Activate Virual environment
    E:\Pavan\dev\python>cd projects\FLASK_APPS && venv\Scripts\activate;
-------------------------------------
-------------  DOCUMENT -------------
-------------------------------------
Bash Script Documentation
Script Overview
This Bash script automates the interaction with a SQLite database and a Flask application, logging actions and handling errors gracefully. The script retrieves a student's ID and joining date, activates a virtual environment, executes Flask commands, and logs the process.

Script Code
bash
Copy code
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
function log_message {
    echo "$LOG_TIMESTAMP - $1" >> "$LOG_DIR/$stuJDT/report_$(date +'%y%m%d').log"
}

# Error handling function
function handle_error {
    log_message "ERROR: Failed - $1"
    echo "ERROR: $1"
    exit 1
}

# Function to execute commands with logging
function execute_command {
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
stuID=$( /c/sqlite/sqlite3 "$DB_PATH" "SELECT rowid FROM stu WHERE JOINING_DATE <= '$CURRENT_DATE' ORDER BY JOINING_DATE DESC LIMIT 1;" ) || handle_error "Failed to get student ID"
stuJDT=$( /c/sqlite/sqlite3 "$DB_PATH" "SELECT JOINING_DATE FROM stu WHERE rowid=$stuID;" ) || handle_error "Failed to get student JOINING_DATE"

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
Line-by-Line Explanation
Shebang
bash
Copy code
#!/bin/bash
Specifies that the script should be run using the Bash shell.
Variable Definitions
bash
Copy code
# Define paths and variables
DB_PATH="/e/Pavan/dev/python/projects/FLASK_APPS/class.db"
LOG_DIR="/e/Pavan/dev/python/projects/FLASK_APPS/logs"
FLASK_APP_DIR="/e/Pavan/dev/python/projects/FLASK_APPS"
VENV_ACTIVATE="E:/Pavan/dev/python/projects/FLASK_APPS/venv/Scripts/activate"
CURRENT_DATE=$(date +'%Y-%m-%d')  # Define current date
LOG_TIMESTAMP=$(date +'%Y%m%d %H:%M:%S')  # Define log timestamp
ERROR_CODE=0
Defines paths for the database, log directory, Flask app, and virtual environment.
Initializes CURRENT_DATE and LOG_TIMESTAMP for logging purposes.
Log Message Function
bash
Copy code
# Log creation function
function log_message {
    echo "$LOG_TIMESTAMP - $1" >> "$LOG_DIR/$stuJDT/report_$(date +'%y%m%d').log"
}
Logs messages with a timestamp into a log file.
Error Handling Function
bash
Copy code
# Error handling function
function handle_error {
    log_message "ERROR: Failed - $1"
    echo "ERROR: $1"
    exit 1
}
Logs and prints error messages and exits the script with an error status.
Execute Command Function
bash
Copy code
# Function to execute commands with logging
function execute_command {
    # Print and log the command being executed
    echo "Executing:"
    echo "    '$*'"  # Print the full command with arguments
    log_message "Executing:"
    log_message "    '$*'"  # Log the full command with arguments

    # Execute the command directly
    "$@" || handle_error "Failed to execute '$*'"
    
    log_message "Executed '$*' successfully"
}
Executes commands, logs the command being executed, and logs the success of the execution.
Database Queries
bash
Copy code
# Step 1: Get ID and JOINING_DATE from the database
stuID=$( /c/sqlite/sqlite3 "$DB_PATH" "SELECT rowid FROM stu WHERE JOINING_DATE <= '$CURRENT_DATE' ORDER BY JOINING_DATE DESC LIMIT 1;" ) || handle_error "Failed to get student ID"
stuJDT=$( /c/sqlite/sqlite3 "$DB_PATH" "SELECT JOINING_DATE FROM stu WHERE rowid=$stuID;" ) || handle_error "Failed to get student JOINING_DATE"
Retrieves the student ID and joining date from the SQLite database.
Create Log Directory
bash
Copy code
# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR/$stuJDT" || handle_error "Failed to create log directory"
Creates a log directory for the student if it doesn't already exist.
Log Start Message
bash
Copy code
log_message "Log started for student with ID: $stuID and JOINING_DATE: $stuJDT"
Logs the beginning of the log process for the student.
Activate Virtual Environment
bash
Copy code
# Step 3: Activate virtual environment
cd "$FLASK_APP_DIR" || handle_error "Failed to change directory to $FLASK_APP_DIR"
source "$VENV_ACTIVATE" || handle_error "Failed to activate virtual environment"
Changes to the Flask application directory and activates the virtual environment.
Execute Flask Commands
bash
Copy code
# Step 4: Execute Flask commands
log_message "Executing Flask commands"
execute_command flask list
# execute_command flask add "Nitin" "tenth" "Vashi" "2024-08-25"
execute_command flask delete $((stuID - 10))
execute_command flask list
Executes specified Flask commands, logging each action.
Deactivate Virtual Environment
bash
Copy code
# Step 5: Deactivate virtual environment
deactivate || handle_error "Failed to deactivate virtual environment"
Deactivates the virtual environment after executing commands.
Log Creation Details
bash
Copy code
# Step 6: Print log creation details
echo "Log created at: $LOG_DIR/$stuJDT/report_$(date +'%y%m%d').log"
log_message "Script completed successfully."
Outputs the location of the log file and logs a success message.
Conclusion
This script is designed to streamline the process of interacting with a SQLite database and a Flask application while maintaining comprehensive logs and error handling.