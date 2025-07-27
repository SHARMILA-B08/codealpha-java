import os
import shutil

def move_jpg_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(src_folder):
        if filename.endswith(".jpg"):
            shutil.move(os.path.join(src_folder, filename), os.path.join(dest_folder, filename))
            print(f"Moved: {filename}")

# Change these to actual existing paths
source = r"C:\Users\santh\Pictures\source_folder"
destination = r"C:\Users\santh\Pictures\destination_folder"

move_jpg_files(source, destination)
