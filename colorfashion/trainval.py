import os
import shutil
import random

# Source directory where the JPG and text files are located
source_directory_images = './images'
source_directory_labels = './labels'

# Destination directories where you want to move the files
destination_directory_80 = './train'
destination_directory_20 = './val'

# Path to the text file containing the list of file names without extensions
file_list_path = 'trainval.txt'

# Ensure the destination directories exist, create them if necessary
if not os.path.exists(destination_directory_80):
    os.makedirs(destination_directory_80)

if not os.path.exists(destination_directory_20):
    os.makedirs(destination_directory_20)

# Read the list of file names from the text file
with open(file_list_path, 'r') as file:
    file_names_without_extension = file.read().splitlines()

# Calculate the number of files to move to each directory
total_files = len(file_names_without_extension)
num_files_80 = int(0.8 * total_files)  # 80%
num_files_20 = total_files - num_files_80  # 20%

# Shuffle the list of file names
random.shuffle(file_names_without_extension)

# Move the first 80% of files (both JPG and text) to destination_directory_80
for name_without_extension in file_names_without_extension[:num_files_80]:
    # Move JPG file
    source_file_path_jpg = os.path.join(source_directory_images, name_without_extension + '.jpg')
    destination_file_path_jpg = os.path.join(destination_directory_80, name_without_extension + '.jpg')
    shutil.move(source_file_path_jpg, destination_file_path_jpg)

    # Move text file from the "labels" directory
    source_file_path_txt = os.path.join(source_directory_labels, name_without_extension + '.txt')
    destination_file_path_txt = os.path.join(destination_directory_80, name_without_extension + '.txt')
    shutil.move(source_file_path_txt, destination_file_path_txt)

    print(f'Moved {name_without_extension}.jpg and {name_without_extension}.txt to {destination_directory_80}')

# Move the remaining 20% of files (both JPG and text) to destination_directory_20
for name_without_extension in file_names_without_extension[num_files_80:]:
    # Move JPG file
    source_file_path_jpg = os.path.join(source_directory_images, name_without_extension + '.jpg')
    destination_file_path_jpg = os.path.join(destination_directory_20, name_without_extension + '.jpg')
    shutil.move(source_file_path_jpg, destination_file_path_jpg)

    # Move text file from the "labels" directory
    source_file_path_txt = os.path.join(source_directory_labels, name_without_extension + '.txt')
    destination_file_path_txt = os.path.join(destination_directory_20, name_without_extension + '.txt')
    shutil.move(source_file_path_txt, destination_file_path_txt)

    print(f'Moved {name_without_extension}.jpg and {name_without_extension}.txt to {destination_directory_20}')