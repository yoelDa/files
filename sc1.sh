#!/bin/bash

# File containing the hash values
hash_file="/path/to/hash/file.txt"

# Malicious hash value to search for
malicious_hash=""

# Loop through all hash values in the file
while read -r line; do
    # Extract the hash value from the line
    hash=$(echo "$line" | awk '{print $1}')
    
    # Check if the hash value matches the malicious hash value
    if [[ "$hash" == "$malicious_hash" ]]; then
        # Extract the filename from the line and print it
        filename=$(echo "$line" | awk '{print $2}')
        echo "Malicious hash found in file: $filename"
    fi
done < "$hash_file"