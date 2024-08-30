import nbformat
import subprocess
import os

def extract_notebook_content(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = nbformat.read(file, as_version=4)

    content = []

    for cell in notebook.cells:
        content.append(cell.source)

    return '\n\n'.join(content)

def extract_notebook_content_as_string(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as file:
        notebook = nbformat.read(file, as_version=4)

    markdown_cells = []
    code_cells = []

    for cell in notebook.cells:
        if cell.cell_type == 'markdown':
            markdown_cells.append(cell.source)
        elif cell.cell_type == 'code':
            code_cells.append(cell.source)

    return markdown_cells, code_cells

def save_notebook_content_to_txt(markdown_content, code_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write("# Markdown Content\n\n")
        file.write("\n\n".join(markdown_content))
        file.write("\n\n# Code Content\n\n")
        file.write("\n\n".join(code_content))
    print(f"Notebook content saved to {output_path}")

def generate_readme_section_with_mistral(prompt):
    response = subprocess.run(
        ["ollama", "run", "mistral-nemo", prompt],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )

    if response.returncode == 0 and response.stdout:
        output = response.stdout
        filtered_output = "\n".join(line for line in output.splitlines() if "failed to get console mode" not in line)
        return filtered_output
    else:
        raise Exception(f"Failed to generate README section: {response.stderr}")

def save_readme_to_markdown(readme_content, vault_path, filename='README.md'):
    if not os.path.exists(vault_path):
        os.makedirs(vault_path)
    
    file_path = os.path.join(vault_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(readme_content)

    print(f"README.md saved to {file_path}")

try:
    notebook_path = r'D:\ANU - Master of Computing\Course work\8830 - Computing Internship\Primary Project\f0264.ipynb'

    print("Reading notebook...")
    content = extract_notebook_content(notebook_path)
    markdown_content, code_content = extract_notebook_content_as_string(notebook_path)

    print("Notebook read successfully.")
    
    # Save entire notebook content to a text file for reference
    save_notebook_content_to_txt(markdown_content, code_content, r'D:\ANU - Master of Computing\Course work\8830 - Computing Internship\Primary Project\notebook_content.txt')

    # Extract and generate the various parts of README

    #Title
    print("generate the title...\n")

    title_prompt = f"""
    Create a title section for a README.md file based on the following notebook title:

    {markdown_content[0]}

    Here's an example of Title section:

    # Title (just copy and paste the title I give you, that's it, do not add anything more)
    """
    title_content = generate_readme_section_with_mistral(title_prompt)

    print("Title is generated!\n")

    ##Dependencies
    print("generate the dependencies...\n")

    dependencies_prompt = f"""
    Create a Dependencies section for a EADME.md file based on the following code, do not add version numbers to the Dependencies:

    {code_content[0]}

    Here's an example of Dependencies section, please follow this format:

    ## Dependencies (Just list all the imported libraries and packages, that's it, do not add more stuff).

    - 
    - 
    - 
    """
    dependencies_content = generate_readme_section_with_mistral(dependencies_prompt)

    print("dependencies are generated!\n")

    ##Input
    print("generate the inputs...\n")

    input_prompt = f"""
    Create Input section for a README.md file based on the following input section:

    {code_content[2]}

    Here's an example of Input section, you should follow this format:

    ## Input (jsut list the inputs, do not add more stuff)

    1.
    2.
    3.
    """
    input_content = generate_readme_section_with_mistral(input_prompt)

    print("Inputs are generated!\n")

    ##Project summary
    print("generate the Project summary...\n")
    
    project_summary_prompt = f"""
    Based on the notebook content provided below, only generate the Project Summary section for the README.md file:

    Here's the notebook content:

    {content}

    Just use one paragraph to indroduce, do not add more stuff, the format for Project Summary should be like this:

    ## Project Summary

    """
    project_summary_content = generate_readme_section_with_mistral(project_summary_prompt)

    print("Project summary is generated!\n")

    ##Output
    print("generate the Output...\n")

    output_prompt = f"""
    Only Generate the Output section for the README.md file based on the code below:

    {content}

    The format should be like this strictly, jsut List all the outputs,output can be saved to database or save as some files, do not add other stuff:

    ## Output

    1. Output1
    2. Output2
    3. Output3
    ...
    """
    output_content = generate_readme_section_with_mistral(output_prompt)

    print("Output is generated!\n")

    ##Usage
    print("generate the usage..\n.")

    usage_instructions_prompt = f"""

    you only need to generate the Usage section for the README.md file based on the code below:

    {code_content}

    The format should be like this strictly, list how it works step by step, try to be concise (less than 300 words):

    ## Usage Instructions

    1. Step1
    2. Step2
    3. Step3
    ...
    """
    usage_instructions_content = generate_readme_section_with_mistral(usage_instructions_prompt)
    print("Usage is generated!\n")

    # Merge all parts
    complete_readme = (
        f"{title_content}\n"
        f"{project_summary_content}\n"
        f"{dependencies_content}\n"
        f"{input_content}\n"
        f"{output_content}\n"
        f"{usage_instructions_content}"
    )

    # Save the generated README file
    save_readme_to_markdown(complete_readme, r'D:\ANU - Master of Computing\Course work\8830 - Computing Internship\Primary Project')

    print("README.md generated and saved successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
