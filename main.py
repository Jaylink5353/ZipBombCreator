import os
import shutil
import sys

source_file = "./text.txt"
destination_folder = "./duplicates"

def copy_files(source_file, destination_folder,):
    """
    Copies a source file repeatedly into a destination folder

    Args:
        source_file: Path to the source file.
        destination_folder: Path to the destination folder.
    """

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    file_count = 0

    while True:  # Copies indefinitely, you might want to add a total file limit
        file_count += 1
        print(file_count)
        destination_path = os.path.join(destination_folder, f"{os.path.splitext(os.path.basename(source_file))[0]}_{file_count}{os.path.splitext(source_file)[1]}") #Preserves extension and adds a number
        shutil.copy2(source_file, destination_path)  # copy2 preserves metadata

# Example usage:
copy_files(source_file, destination_folder)
