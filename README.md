# Mass Git Downloader

This Python script automates the process of downloading critical `.git` files from a list of specified domains. It supports flexible input and output options, making it a powerful tool for auditing purposes and testing exposed `.git` directories.

## Features
- **Customizable Input**: Provide a list of domains via a text file using the `-i` flag.
- **Organized Output**: Saves downloaded `.git` files in a structured directory hierarchy based on domain names.
- **Comprehensive File Targeting**: Includes important `.git` files like `.git/config`, `.git/HEAD`, `.gitignore`, and more.
- **Error Handling**: Skips invalid domains and handles connection errors gracefully.
- **Easy to Use**: Minimal configuration required; just run the script with input and output flags.

## Usage
1. Prepare a file containing target domains (one per line).
2. Run the script with:
   ```bash
   python3 git_downloader.py -i domains.txt -o output_directory
   ```
3. Review the downloaded `.git` files in the specified output directory.

## Important Note
This script is intended for ethical and educational purposes only. Ensure you have proper authorization before accessing any `.git` directories on a target domain.
