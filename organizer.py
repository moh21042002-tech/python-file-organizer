import os
import shutil

def organize_directory(target_path):
    extensions_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp']
    }

    if not os.path.exists(target_path):
        print(f"Error: The path {target_path} does not exist.")
        return

    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, exts in extensions_map.items():
            if file_ext in exts:
                folder_path = os.path.join(target_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break
        
        if not moved:
            other_folder = os.path.join(target_path, 'Others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others/")

    print("✨ Organization completed successfully!")

if __name__ == "__main__":
    path_to_organize = input("Enter the path of the directory to organize: ")
    organize_directory(path_to_organizer)
