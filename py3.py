import os
import subprocess

# Path to the folder containing the files
folder_path = '/path/to/folder'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a regular file and not a directory
    if os.path.isfile(file_path):
        # Run the md5sum command on the file
        result = subprocess.run(['md5sum', file_path], stdout=subprocess.PIPE, text=True)
        
        # Extract the MD5 hash from the output of the command
        md5_hash = result.stdout.split()[0]
        
        # Print the filename and its MD5 hash
        print(f"{filename}: {md5_hash}")