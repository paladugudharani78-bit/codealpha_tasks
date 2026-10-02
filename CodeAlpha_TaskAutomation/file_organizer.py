import os
import shutil

# Folder containing the files
source_folder = "MyFiles"

# Folder where JPG files will be moved
destination_folder = os.path.join(source_folder, "JPG_Files")

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Check all files in the source folder
for filename in os.listdir(source_folder):

    # Check if the file is a JPG file
    if filename.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Move the JPG file
        shutil.move(source_path, destination_path)

        print(filename, "moved successfully.")

print("\nAll JPG files have been organized.")