import os
import shutil

DIRECTORY_TO_ORGANIZE = os.getcwd()

# File types and corresponding folder names
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Programs': ['.exe', '.msi', '.bat', '.cmd'],
    'Others': []
}

def organize_files(directory):
    script_name = os.path.basename(__file__)
    
    for folder in FILE_TYPES:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(directory):
        if filename == script_name:
            continue  # Skip the script file itself
        
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            
            if not moved:
                shutil.move(file_path, os.path.join(directory, 'Others', filename))

if __name__ == "__main__":
    organize_files(DIRECTORY_TO_ORGANIZE)
