# Backup code

A Python script that creates a timestamped backup of any folder and saves it as a ZIP file.

# What It Does
 Copies the entire folder you specify
 Names the backup with the current date and time: `backup_20260518_143022`
 Zips the backup folder automatically
 Logs all actions to `app.log`

# Requirements
 Python 3.14
 No external libraries. Uses: `os`, `shutil`, `argparse`, `logging`, `datetime`

# How to Run
Open a terminal in the project folder and run:

python backup.py folder_path
This creates a ZIP file like backup_20260518_143022.zip containing a full copy of sample_files

# OUTPUT
Folder: backup_20260518_143022.zip 
temporary folder created during backupZIP file: backup_20260518_143022.zip 
the final backup you keep app.log: Log file with timestamps of successful and failed backups
