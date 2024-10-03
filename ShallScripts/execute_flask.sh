#!/bin/bash

# Exit immediately if a command exits with a non-zero status and capture the error
set -e

# Initialize variables
currentDate=$(date +'%Y-%m-%d')
logDate=$(date +'%y%m%d')
cmdCounter=1 # Initialize command counter

# Log function with timestamp and dynamic command number
log() {
    echo "$(date +'%Y%m%d %H:%M:%S') info cmd${cmdCounter} executed: $1" >> /repo/data/${REPORTDT}/logs/script_log_$logDate.log
    ((cmdCounter++)) # Increment the command counter after every log
}

# Error logging function
log_error() {
    local last_command="$1"
    local exit_code="$2"
    echo "$(date +'%Y%m%d %H:%M:%S') error cmd${cmdCounter} failed: Command '$last_command' exited with status $exit_code" >> /repo/data/${REPORTDT}/logs/script_log_$logDate.log
}

# Step 2: Extract database path from DATABASE variable
DATABASE="/app/tech/data/report.db"

# Step 3: Fetch ID and REPORTDT from SQLite3 database
trap 'log_error "sqlite3 fetch" $?' ERR
read ID REPORTDT <<< $(sqlite3 "$DATABASE" "SELECT ID, REPORTDT FROM student WHERE REPORTDT = '$currentDate' ORDER BY ID DESC LIMIT 1;")
log "Fetched ID: $ID and REPORTDT: $REPORTDT from SQLite database."

# Step 4: Create the required folders only if they do not exist
trap 'log_error "mkdir reports folder" $?' ERR
if [ ! -d "/repo/data/${REPORTDT}/zone/reports" ]; then
    mkdir -p /repo/data/${REPORTDT}/zone/reports
    log "Created folder /repo/data/${REPORTDT}/zone/reports."
fi

trap 'log_error "mkdir logs folder" $?' ERR
if [ ! -d "/repo/data/${REPORTDT}/logs" ]; then
    mkdir -p /repo/data/${REPORTDT}/logs
    log "Created folder /repo/data/${REPORTDT}/logs."
fi

# Step 5: Copy support files
trap 'log_error "copy support.ini" $?' ERR
cp /app/tech/misc/support.ini /repo/data/${REPORTDT}/zone/reports/
log "Copied support.ini to /repo/data/${REPORTDT}/zone/reports/."

trap 'log_error "copy report.ini" $?' ERR
cp /app/tech/misc/report.ini /repo/data/${REPORTDT}/zone/reports/
log "Copied report.ini to /repo/data/${REPORTDT}/zone/reports/."

# Step 6: Activate Flask virtual environment
trap 'log_error "Flask environment activation" $?' ERR
cd /app/tech/hrreport/ && source ./activate.sh
log "Activated Flask virtual environment."

# Step 7: Execute Flask commands
trap 'log_error "flask repo --help" $?' ERR
flask repo --help
log "flask repo --help"

trap 'log_error "flask repo $ID -date $REPORTDT" $?' ERR
flask repo "$ID" -date "$REPORTDT" -log "/repo/data/${REPORTDT}/repo_$logDate.log"
log "flask repo $ID -date $REPORTDT -log /repo/data/${REPORTDT}/repo_$logDate.log"

trap 'log_error "flask scan -helper True" $?' ERR
flask scan -helper True -date "$REPORTDT" -log "/repo/data/${REPORTDT}/helper_$logDate.log"
log "flask scan -helper True -date $REPORTDT -log /repo/data/${REPORTDT}/helper_$logDate.log"

# Add more Flask commands here as needed (7-4 to 7-8)

# Step 7-9: Deactivate virtual environment
trap 'log_error "Flask environment deactivation" $?' ERR
deactivate
log "Deactivated Flask virtual environment."
