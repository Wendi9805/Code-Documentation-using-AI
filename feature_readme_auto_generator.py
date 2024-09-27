# This python file is to generate readme files for all feature files

import os
from feature_readme_generator import generate_readme_from_notebook, edit_readme_format, save_readme_to_markdown

def generate_readme_for_all_notebooks(directory_path):
    # Traverse the provided directory and find all .ipynb files
    notebook_files = [f for f in os.listdir(directory_path) if f.endswith('.ipynb')]

    if not notebook_files:
        print(f"No Jupyter notebook files (.ipynb) found in the directory: {directory_path}")
        return

    # Generate a README file for each notebook file
    for notebook_file in notebook_files:
        notebook_path = os.path.join(directory_path, notebook_file)
        try:
            print(f"Processing notebook: {notebook_file}")

            # Generate README content
            readme_content = generate_readme_from_notebook(notebook_path)

            # Edit the format of the README
            final_readme_content = edit_readme_format(readme_content)

            # Set the path to save the README file
            readme_filename = f"README_{os.path.splitext(notebook_file)[0]}.md"
            save_readme_to_markdown(final_readme_content, directory_path, readme_filename)

            print(f"README file generated and saved as: {readme_filename}")

        except Exception as e:
            print(f"Error processing {notebook_file}: {str(e)}")

# if __name__ == "__main__":
#     # Provide the directory path
#     directory_path = r'D:\ANU - Master of Computing\Course work\8830 - Computing Internship\Primary Project\test'

#     if os.path.isdir(directory_path):
#         generate_readme_for_all_notebooks(directory_path)
#     else:
#         print(f"The provided path is not a valid directory: {directory_path}")
