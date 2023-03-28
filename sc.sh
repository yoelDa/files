#!/bin/bash

# Directory containing the files to hash
dir="/path/to/directory"

# Output file to save the hash values
output_file="/path/to/output/file.txt"

# Loop through all files in the directory
for file in "$dir"/*; do
    # Check if the file is a regular file and not a directory
    if [[ -f "$file" ]]; then
        # Compute the MD5 hash of the file and save the result to the output file
        md5sum "$file" >> "$output_file"
    fi
done