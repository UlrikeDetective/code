# static file | create_directory.py
import os

# Define the structure
directories = [
    'app'
]

files = [
    'app/__init__.py',
    'app/main.py',
    'app/models.py',
    'app/templates.py',
    'app/database.py'
]

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create empty files
for file in files:
    with open(file, 'w') as f:
        pass

print("Directories and files created successfully.")