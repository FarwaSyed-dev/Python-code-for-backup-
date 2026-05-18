import os
import shutil
import argparse
import logging
from datetime import datetime

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_backup(folder_path):

    try:
        if not os.path.exists(folder_path):
            print("Folder not found.")
            return

        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_folder = "backup_" + current_time

        shutil.copytree(folder_path, backup_folder)

        shutil.make_archive(backup_folder, 'zip', backup_folder)

        print("Backup created successfully.")

        logging.info("Backup created.")

    except Exception as error:
        print("Error:", error)
        logging.error(error)

parser = argparse.ArgumentParser(description="Backup Script")

parser.add_argument("folder", help="Enter folder path")

args = parser.parse_args()

create_backup(args.folder)