import os
import requests
from urllib.parse import urlparse
import argparse

def download_git_files(domain_list_file, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the domain list from the input file
    with open(domain_list_file, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]

    # Define common .git paths to download
    git_paths = [
        ".git/config",
        ".git/HEAD",
        ".git/index",
        ".git/objects/info/packs",
        ".git/logs/HEAD",
        ".git/logs/refs/heads/master",
        ".git/refs/heads/master",
        ".git/refs/remotes/origin/HEAD",
        ".git/refs/remotes/origin/master",
        ".git/packed-refs",
        ".git/description",
        ".git/hooks/pre-commit.sample",
        ".git/hooks/pre-push.sample",
        ".gitignore"
    ]

    for domain in domains:
        parsed_url = urlparse(domain)
        if not parsed_url.scheme or not parsed_url.netloc:
            print(f"Invalid domain format: {domain}")
            continue

        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        # Create a directory for the domain
        domain_dir = os.path.join(output_dir, parsed_url.netloc.replace(':', '_'))
        os.makedirs(domain_dir, exist_ok=True)

        print(f"Processing domain: {base_url}")

        for path in git_paths:
            file_url = f"{base_url}/{path}"
            local_file_path = os.path.join(domain_dir, path.replace('/', '_'))

            try:
                print(f"Downloading: {file_url}")
                response = requests.get(file_url, timeout=10)

                if response.status_code == 200:
                    with open(local_file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"Saved: {local_file_path}")
                else:
                    print(f"Failed to download {file_url} (Status code: {response.status_code})")

            except requests.RequestException as e:
                print(f"Error downloading {file_url}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download .git files from a list of domains.")
    parser.add_argument('-i', '--input', required=True, help="Path to the input file containing domains.")
    parser.add_argument('-o', '--output', default="downloaded_git_files", help="Directory to store downloaded files.")

    args = parser.parse_args()

    download_git_files(args.input, args.output)
