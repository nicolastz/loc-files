import os

def copy_files(source_folder, new_extension):
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                # file_name_without_extension, old_extension = os.path.splitext(file_name)
                new_file_name = file_name + new_extension
                new_file_path = os.path.join(root, new_file_name)
                with open(new_file_path, 'w'):
                    pass

source_folder = "D:/Desktop/temp/prueba"
dest_folder = "D:/Desktop/temp/prueba"
new_extension = ".loc"
copy_files(source_folder, new_extension)