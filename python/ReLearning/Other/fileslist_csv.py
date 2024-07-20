import os
import csv
import datetime
from collections import defaultdict
from tqdm import tqdm
import sys

def get_file_metadata(file_path):
    """
    Returns file metadata including creation date and last modified date.
    """
    creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
    last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    return creation_date, last_modified

def create_csv_file(start_dir, output_file):
    """
    Creates a CSV file with columns: filename, path, file extension, number of duplicate files,
    creation date, and last modified date.
    """
    file_dict = defaultdict(list)  # Store files grouped by filename

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = file
            file_extension = os.path.splitext(file)[1]
            file_dict[file_name].append((file_path, file_extension))

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Filename', 'Path', 'File Extension', 'No. of Duplicate Files', 'Creation Date', 'Last Modified']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        total_files = sum(1 for file_paths in file_dict.values() if len(file_paths) > 1)
        progress_bar = tqdm(total=total_files, desc='Processing Files', unit='file')

        for file_name, file_paths in file_dict.items():
            if len(file_paths) > 1:
                creation_date, last_modified = get_file_metadata(file_paths[0][0])
                writer.writerow({
                    'Filename': file_name,
                    'Path': file_paths[0][0],
                    'File Extension': file_paths[0][1],
                    'No. of Duplicate Files': len(file_paths),
                    'Creation Date': creation_date,
                    'Last Modified': last_modified
                })
                progress_bar.update()

    progress_bar.close()
    print(f"CSV file '{output_file}' created successfully.")

# Specify the directory to start searching for files
start_directory = r'E:\\SharedFolder'  # Use the 'r' prefix to treat the string as a raw string

# Specify the output CSV file path
output_csv_file = 'file_metadata.csv'

# Set the encoding for the console to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

create_csv_file(start_directory, output_csv_file)