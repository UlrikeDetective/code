import os

# Define the structure
directories = [
    'music-app',
    'music-app/public',
    'music-app/views',
    'music-app/routes'
]

files = [
    'music-app/public/styles.css',
    'music-app/public/index.js',
    'music-app/views/index.ejs',
    'music-app/views/music.ejs',
    'music-app/app.js',
    'music-app/database.js',
    'music-app/routes/api.js',
    'music-app/routes/music.js',
    'music-app/README.md'
]

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create empty files
for file in files:
    # Ensure parent directories exist (already handled above)
    with open(file, 'w') as f:
        pass

print("Directories and files created successfully.")
