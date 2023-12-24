import zipfile
import os

input_folder_path = 'C:/Users/ABC/Documents/unzip/stickers/'
output_folder_path = 'C:/Users/ABC/Documents/unzipped/'

for i in range(1, 200): 
    folder_name = f"folder_ ({i})"
    folder_to_unzip = os.path.join(input_folder_path, folder_name)
    zip_file_path = os.path.join(input_folder_path, f"{folder_name}.zip")

    print(folder_name)
    print(folder_to_unzip)
    print(zip_file_path)

    if os.path.exists(zip_file_path):
        output_path = os.path.join(output_folder_path, folder_name)
        os.makedirs(output_path, exist_ok=True)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)
            print(f"Extracted contents of {folder_name}.zip to {output_path}")
    else:
        print(f"Folder {folder_name} or its corresponding zip file not found.")
