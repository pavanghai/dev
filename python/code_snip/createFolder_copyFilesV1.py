import os
from datetime import datetime

# Get the current date in YYYY-MM-DD format
current_date = datetime.now().strftime('%Y-%m-%d')

# Define the base directory
base_dir = f"/hr/data/{current_date}"

# Define the subdirectories
subdirs = ["logs", "MUM/Reports"]

# Define the files to copy
files_to_copy = ["/hr/sample.txt", "/hr/sample1.txt", "/hr/sample2.txt", "/hr/sfdample.txt"]

# Check if all files exist
all_files_exist = all(os.path.exists(file) for file in files_to_copy)

if all_files_exist:
    # Create the directories
    for subdir in subdirs:
        os.makedirs(os.path.join(base_dir, subdir), exist_ok=True)

    # Set permissions to 775
    os.chmod(base_dir, 0o775)
    for subdir in subdirs:
        os.chmod(os.path.join(base_dir, subdir), 0o775)

    # Copy the files to the base directory
    for file in files_to_copy:
        os.system(f"cp {file} {base_dir}")

    print(f"Folders and files created and copied successfully in '{base_dir}' with permissions set to 775!")
else:
    print("Not all files are available. No actions were performed.")
