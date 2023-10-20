from ultralytics import YOLO

# Create model from scratch
model = YOLO('yolov8m.pt')

# Train the model
model.train(data='/kaggle/input/config/config_kaggle.yaml', epochs=250)

import zipfile
import os

# Define the folder you want to zip and the name for the zip file
folder_to_zip = '/kaggle/working/runs'  # Change this to your folder's name
zip_file_name = 'runs.zip'  # Change this to your desired zip file name

# Create a zip file and open it in write mode
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_to_zip):
        for file in files:
            # Get the full path to the file
            file_path = os.path.join(root, file)
            
            # Define the relative path for the zip file
            zip_path = os.path.relpath(file_path, folder_to_zip)
            
            # Write the file to the zip file
            zipf.write(file_path, zip_path)

print(f'{zip_file_name} has been created.')


# Define the folder you want to zip and the name for the zip file
folder_to_zip = '/kaggle/working/wandb'  # Change this to your folder's name
zip_file_name = 'wandb.zip'  # Change this to your desired zip file name

# Create a zip file and open it in write mode
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_to_zip):
        for file in files:
            # Get the full path to the file
            file_path = os.path.join(root, file)
            
            # Define the relative path for the zip file
            zip_path = os.path.relpath(file_path, folder_to_zip)
            
            # Write the file to the zip file
            zipf.write(file_path, zip_path)

print(f'{zip_file_name} has been created.')