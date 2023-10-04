import os
import shutil

# Source directory where the JPG files are located
source_directory = './images'

# Destination directory where you want to move the JPG files
destination_directory = './test'

# Path to the text file containing the list of file names without extensions
file_list_path = 'test.txt'

# Ensure the destination directory exists, create it if necessary
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Read the list of file names from the text file
with open(file_list_path, 'r') as file:
    file_names_without_extension = file.read().splitlines()

# Loop through the file names and move the corresponding JPG files
for name_without_extension in file_names_without_extension:
    source_file_path = os.path.join(source_directory, name_without_extension + '.jpg')
    destination_file_path = os.path.join(destination_directory, name_without_extension + '.jpg')

    # Check if the source file exists
    if os.path.exists(source_file_path):
        # Move the file to the destination directory
        shutil.move(source_file_path, destination_file_path)
        print(f'Moved {name_without_extension}.jpg to {destination_directory}')
    else:
        print(f'Skipping {name_without_extension}.jpg (not found)')