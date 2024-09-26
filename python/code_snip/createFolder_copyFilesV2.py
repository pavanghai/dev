import os
import sys
import argparse
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='script.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_folders(base_path):
    try:
        os.makedirs(os.path.join(base_path, 'logs'), exist_ok=True)
        os.makedirs(os.path.join(base_path, 'MUM/Reports'), exist_ok=True)
        os.chmod(base_path, 0o775)
        logging.info(f"Created folders and set permissions for {base_path}")
    except Exception as e:
        logging.error(f"Error creating folders: {e}")
        sys.exit(1)

def copy_files(base_path, files):
    try:
        for file in files:
            os.system(f'cp {file} {base_path}')
        logging.info(f"Copied files to {base_path}")
    except Exception as e:
        logging.error(f"Error copying files: {e}")
        sys.exit(1)

def main(copy_files_flag):
    date_str = datetime.now().strftime('%Y-%m-%d')
    base_path = f'/hr/data/{date_str}'
    
    create_folders(base_path)
    
    files = ['/hr/sample.txt', '/hr/sample1.txt', '/hr/sample2.txt', '/hr/sfdample.txt']
    
    if copy_files_flag:
        for file in files:
            if not os.path.exists(file):
                logging.error(f"File not found: {file}")
                sys.exit(1)
        copy_files(base_path, files)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create folders and optionally copy files.')
    parser.add_argument('-f', '--copy_files', type=bool, default=True, help='Flag to copy files (default: True)')
    args = parser.parse_args()
    
    main(args.copy_files)
