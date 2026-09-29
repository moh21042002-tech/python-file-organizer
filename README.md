# 📂 Python File Organizer Automation

A lightweight, efficient Python automation script designed to clean up messy folders (like Downloads) by automatically sorting files into organized categories (Images, Documents, Videos, Code, etc.) based on their extensions.

---

### 🚀 Features:
* **Automatic Categorization:** Sorts files into specific folders (`Images`, `Documents`, `Archives`, `Scripts`, etc.).
* **Time-saving:** Runs in seconds, eliminating manual file sorting.
* **Safe Handling:** Skips existing files to prevent accidental overwriting.

---

### 🛠️ Built With:
* **Python 3.x** (`os`, `shutil` built-in libraries)

---

### 💻 The Code:
```python
import os
import shutil

def organize_directory(target_path):
    # Define extension mappings
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

        # Skip directories
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
    # Specify the target folder path to organize
    path_to_organize = input("Enter the path of the directory to organize: ")
    organize_directory(path_to_organize)
git clone [https://github.com/moh21042002-tech/python-file-organizer.git](https://github.com/moh21042002-tech/python-file-organizer.git)
python organizer.py
