# This python file is to download all the feature and pipeline files

from github import Github # Imports the GitHub library to interact with the GitHub API, allowing you to access repositories, files, and more.
import os # Provides functions to interact with the operating system, such as file and directory management.
import re # The 're' module is used for regular expression operations, allowing pattern matching for repository names.
import requests # A library to send HTTP requests, used here to download files from URLs (like Jupyter Notebooks or Groovy files).
import sys # Pass the parameters from Javascript code to Python code

def download_notebooks_from_repos(token, org_name, download_path, max_downloads):
    """
    Download Jupyter Notebook (.ipynb) files from repositories in the specified GitHub organization
    that match the naming pattern (fXXXX).
    
    :param token: GitHub personal access token
    :param org_name: Name of the GitHub organization
    :param download_path: Directory path to save downloaded files
    :param max_downloads: Maximum number of repositories to download
    """
    # Create a GitHub client using the provided token
    g = Github(token)

    # Check GitHub API rate limit
    rate_limit = g.get_rate_limit()
    core_limit = rate_limit.core
    print(f"Rate limit remaining: {core_limit.remaining}/{core_limit.limit}")

    # Match repositories with the fXXXX naming pattern
    repo_pattern = re.compile(r'^f\d{4}$')

    # Get all repositories in the organization
    org = g.get_organization(org_name)
    repos = org.get_repos()

    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Helper function to download notebook files
    def download_notebook_files(repo, path):
        contents = repo.get_contents("")  # Retrieve all files and folders in the repository root directory.
        print(f"Checking contents in repository: {repo.name}")
        
        while contents:  # Continue until the contents list is empty
            file_content = contents.pop(0)
            print(f"Found {file_content.path} (type: {file_content.type})")

            if file_content.type == "dir":
                # Recursively enter subdirectories
                print(f"Entering directory: {file_content.path}")
                contents.extend(repo.get_contents(file_content.path))  # Add the contents of the subdirectory to the list to be processed
            elif file_content.path.endswith(".ipynb"):  # Check if it's a .ipynb file
                download_url = file_content.download_url
                response = requests.get(download_url)
                file_path = os.path.join(path, file_content.name)

                # Check if the download was successful and save the file
                if response.status_code == 200 and len(response.content) > 0:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"Downloaded {file_content.name} from {repo.name} to {file_path}")
                else:
                    print(f"Failed to download {file_content.name} from {repo.name}.")

    # Counter to track the number of downloads
    downloaded_count = 0

     # Iterate over all repositories, filter based on the naming pattern, and download Jupyter Notebook files
    for repo in repos:
        if repo_pattern.match(repo.name):  # Match repositories with fXXXX pattern
            print(f"Matched repository: {repo.name}")
            if downloaded_count >= max_downloads:
                print(f"Reached the maximum download limit of {max_downloads}.")
                break  # Stop downloading when the limit is reached
            print(f"Processing repository: {repo.name}")
            download_notebook_files(repo, download_path)  # Download directly to the specified path
            downloaded_count += 1   # Update the counter

    print("Download completed.")


def download_pipeline_from_repos(token, org_name, download_path, max_downloads):
    """
     Download Groovy (.groovy) files from repositories in the specified GitHub organization
    that match the naming pattern (pXXXX).
    
    :param token: GitHub personal access token
    :param org_name: Name of the GitHub organization
    :param download_path: Directory path to save downloaded files
    :param max_downloads: Maximum number of repositories to download
    """

    g = Github(token)

    rate_limit = g.get_rate_limit()
    core_limit = rate_limit.core
    print(f"Rate limit remaining: {core_limit.remaining}/{core_limit.limit}")

    repo_pattern = re.compile(r'^p\d{4}$')

    org = g.get_organization(org_name)
    repos = org.get_repos()

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    def download_groovy_files(repo, path):
        contents = repo.get_contents("")
        print(f"Checking contents in repository: {repo.name}")
        
        while contents:
            file_content = contents.pop(0)
            print(f"Found {file_content.path} (type: {file_content.type})")

            if file_content.type == "dir":

                print(f"Entering directory: {file_content.path}")
                contents.extend(repo.get_contents(file_content.path))
            elif file_content.path.endswith(".groovy"):
                download_url = file_content.download_url
                response = requests.get(download_url)
                file_path = os.path.join(path, file_content.name)


                if response.status_code == 200 and len(response.content) > 0:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"Downloaded {file_content.name} from {repo.name} to {file_path}")
                else:
                    print(f"Failed to download {file_content.name} from {repo.name}.")


    downloaded_count = 0


    for repo in repos:
        if repo_pattern.match(repo.name):
            print(f"Matched repository: {repo.name}")
            if downloaded_count >= max_downloads:
                print(f"Reached the maximum download limit of {max_downloads}.")
                break
            print(f"Processing repository: {repo.name}")
            download_groovy_files(repo, download_path)
            downloaded_count += 1

    print("Download completed.")

# main function to be called when need
def main(task_type, token, org_name, download_path, max_downloads):
    if task_type == 'notebook':
        download_notebooks_from_repos(token, org_name, download_path, max_downloads)
    elif task_type == 'pipeline':
        download_pipeline_from_repos(token, org_name, download_path, max_downloads)
    else:
        print("Invalid task type. Please use 'notebook' or 'pipeline'.")

if __name__ == "__main__":
    if len(sys.argv) == 6:
        task_type = sys.argv[1]
        token = sys.argv[2]
        org_name = sys.argv[3]
        download_path = sys.argv[4]
        max_downloads = int(sys.argv[5])
        main(task_type, token, org_name, download_path, max_downloads)
    else:
        print("Usage: python script.py <task_type> <token> <org_name> <download_path> <max_downloads>")
