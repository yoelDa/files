import os
import subprocess
# Path to the folder containing the files
folder_path = '/home/bruce/Desktop/suspicious-files'
# Path to the output file
output_file_path = '/home/bruce/Desktop/suspicious-files.txt'
# Open the output file for writing
with open(output_file_path, 'w') as output_file:
    # Loop through all files in the folder
    for filename in os.listdir(folder_path): file_path = os.path.join(folder_path, filename)
        # Check if the file is a regular file and not a directory
    if os.path.isfile(file_path):
            # Run the md5sum command on the file
            result = subprocess.run(['md5sum', file_path], stdout=subprocess.PIPE, text=True)
            # Extract the hash from the output of the command
            file_hash = result.stdout.split()[0]
            # Write the filename and its hash to the output file
            output_file.write(f"{filename}: {file_hash}")