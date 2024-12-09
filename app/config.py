import os

# Define the path to the Downloads folder on the C: drive
USER_DOWNLOADS_DIR = os.path.join(os.environ['USERPROFILE'], 'Downloads')

UPLOAD_DIRECTORY = os.path.join(USER_DOWNLOADS_DIR, 'uploaded_files')
REPORT_DIRECTORY = os.path.join(USER_DOWNLOADS_DIR, 'reports')

# Ensure directories exist
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
os.makedirs(REPORT_DIRECTORY, exist_ok=True)
