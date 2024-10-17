# This python file is to generate readme files for all feature files

import os
import sys # Pass the parameters from Javascript code to Python code
from feature_readme_generator import generate_readme_from_notebook, edit_readme_format, save_readme_to_markdown
import time # Provides time-related functions, such as measuring execution time and creating delays.
import threading # Allows for creating and managing threads, enabling parallel task execution.

# Get the current time
elapsed_time = 0

file_number = 0

def timer():
    global elapsed_time
    while True:
        time.sleep(1)
        elapsed_time += 1

def start_timer():
    timer_thread = threading.Thread(target=timer)
    timer_thread.daemon = True
    timer_thread.start()

def disable_print():
    sys.stdout = open(os.devnull, 'w')

def enable_print():
    sys.stdout = sys.__stdout__

def generate_readme_for_all_notebooks(directory_path):

    # Traverse the provided directory and find all .ipynb files
    notebook_files = [f for f in os.listdir(directory_path) if f.endswith('.ipynb')]

    if not notebook_files:
        print(f"No Jupyter notebook files (.ipynb) found in the directory: {directory_path}")
        return

    time1 = elapsed_time
    # Generate a README file for each notebook file
    for notebook_file in notebook_files:
        notebook_path = os.path.join(directory_path, notebook_file)
        try:
            global file_number
            
            time3 = elapsed_time
            print(f"\033[92mProcessing notebook: {notebook_file}\033[0m\n")
            print(f"\033[92mGenerating README file for current feature notebook (may take around 30 seconds averagely)...\033[0m\n")
            disable_print()

            # Generate README content
            readme_content = generate_readme_from_notebook(notebook_path)

            # Edit the format of the README
            final_readme_content = edit_readme_format(readme_content)

            # Set the path to save the README file
            readme_filename = f"README_{os.path.splitext(notebook_file)[0]}.md"
            enable_print()
            
            save_readme_to_markdown(final_readme_content, directory_path, readme_filename)

            enable_print()
            time4 = elapsed_time - time3
            print(f"\033[94m{readme_filename} has been generated and saved in {directory_path}, took {time4} seconds!\033[0m\n")
            file_number = file_number + 1 

        except Exception as e:
            print(f"Error processing {notebook_file}: {str(e)}")

    time2 = elapsed_time -time1
    print(f"\033[94m{file_number} README files have been generated, took {time2} seconds in total!\033[0m\n")

# main function to be called when need
def main(directory_path):
    start_timer()
    if os.path.isdir(directory_path):
        generate_readme_for_all_notebooks(directory_path)
    else:
        print(f"The provided path is not a valid directory: {directory_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        main(directory_path)
    else:
        print("Please provide a directory path.")
