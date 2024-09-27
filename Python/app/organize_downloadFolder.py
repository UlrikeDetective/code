import os
import shutil

def organize_downloads(download_folder):
    file_types = {
        'Images': ['.jpg', '.png', '.gif', '.jpeg'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Audio': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mov'],
        'Excel': ['.xlsx', '.csv'],
        'html': ['.html'],
        
    }

    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        _, file_ext = os.path.splitext(file_path)

        for folder, extensions in file_types.items():
            if file_ext.lower() in extensions:
                folder_path = os.path.join(download_folder, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, filename))

organize_downloads('/Users/ulrike_imac_air/Downloads')  # Using double backslashes