# This python file is to generate readme files for one feature files

import os # Provides functions for interacting with the operating system, such as working with file paths.
import nbformat # Used to read and manipulate Jupyter Notebook (.ipynb) files in their native format.
import subprocess # Allows the script to run external commands or programs. Here, it's used to run Mistral NeMo for generating README content.

# Send a prompt to the Mistral model to generate the content
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

# Break down the notebook into different cells
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

# Main function to generate readme files
def generate_readme_from_notebook(notebook_path):
    notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
    markdown_content, code_content = extract_notebook_content_as_string(notebook_path)

    # Generate readme file for each section

    # Title
    print("generate the title...\n")

    title_prompt = f"""
    Create a title section for a README.md file based on the following notebook title:

    {markdown_content[0]}

    Here's an example of Title section:

    Title (do not add "#" before title, just copy and paste the title I give you, that's it, do not add anything more)
    """
    title_content = generate_readme_section_with_mistral(title_prompt)
    title_content = f"# {notebook_name}: {title_content.splitlines()[0]}\n"

    print("Title is generated!\n")

    # Dependencies
    print("generate the dependencies...\n")

    dependencies_prompt = f"""
    Create a Dependencies section for a README.md file based on the following code, do not add version numbers to the Dependencies:

    {code_content[0]}

    Here's an example of Dependencies section, please follow this format:

    ## Dependencies (Just list all the imported libraries and packages, that's it, do not add more stuff).

    - 
    - 
    - 
    """
    dependencies_content = generate_readme_section_with_mistral(dependencies_prompt)

    print("dependencies are generated!\n")

    # Input
    print("generate the inputs...\n")

    input_prompt = f"""
    Create Input section for a README.md file based on the following input section:

    {code_content[2]}

    Here's an example of Input section, you should follow this format:

    ## Input (just list the inputs, do not add more stuff)

    1.
    2.
    3.
    """
    input_content = generate_readme_section_with_mistral(input_prompt)

    print("Inputs are generated!\n")

    # Project Summary
    print("generate the Project summary...\n")

    project_summary_prompt = f"""
    Based on the notebook content provided below, only generate the Project Summary section for the README.md file:

    Here's the notebook content:

    {' '.join(markdown_content)}

    Just use one paragraph to introduce, do not add more stuff, the format for Project Summary should be like this:

    ## Project Summary

    """
    project_summary_content = generate_readme_section_with_mistral(project_summary_prompt)

    print("Project summary is generated!\n")

    # Output
    print("generate the Output...\n")

    output_prompt = f"""
    Only Generate the Output section for the README.md file based on the code below:

    {' '.join(code_content)}

    The format should be like this strictly, just List all the outputs, output can be saved to database or saved as some files, do not add other stuff:

    ## Output

    1. Output1
    2. Output2
    3. Output3
    ...
    """
    output_content = generate_readme_section_with_mistral(output_prompt)

    print("Output is generated!\n")

    # Usage
    
    print("generate the usage..\n.")

    usage_instructions_prompt = f"""
    you only need to generate the Usage section for the README.md file based on the code below:

    {' '.join(code_content)}

    The format should be like this strictly, list how it works step by step, try to be concise (less than 300 words):

    ## Usage Instructions

    1. Step1
    2. Step2
    3. Step3
    ...
    """
    usage_instructions_content = generate_readme_section_with_mistral(usage_instructions_prompt)

    print("Usage is generated!\n")

    # Combine all the sections
    complete_readme = (
        f"{title_content}\n"
        f"{project_summary_content}\n"
        f"{dependencies_content}\n"
        f"{input_content}\n"
        f"{output_content}\n"
        f"{usage_instructions_content}"
    )

    return complete_readme

# Edite the format for our Readme files
def edit_readme_format(complete_readme):
    print("Editing the format...\n")

    edit_format_prompt = f"""
    My readme file has been finished, here's my readme file content:

    {complete_readme}

    However, the format of this readme file may be different from the standard format, help me to edit the format based on the standard format below without losing information:

    # fXXX: Your title

    ## Project Summary

    (here is the description of your project summary)

    ## Dependencies

    - Dependency1
    - Dependency2
    - Dependency3
    ...

    ## Input

    1. **Input1** (`config['DEFAULT']['XXXXX']`)
    2. **Input2** (`config['DEFAULT']['XXXXX']`)
    3. **Input3** (`config['DEFAULT']['XXXXX']`)
    4. **Input4** (Environment Variable: `XXXXXXX`)
    .....

    ## Output

    1. Output1

    2. Output2

    3. Output3

    .....

    ## Usage Instructions

    1. **Usage Instruction1:**
    -
    -

    2. **Usage Instruction2:**
    -
    -

    3. **Usage Instruction3:**
    -
    -
    """
    final_version = generate_readme_section_with_mistral(edit_format_prompt)

    # Clean unnecessary parts of the AI generated content 
    def clean_generated_content(content):
        if '#' in content:
            cleaned_content = content.split('#', 1)[1]
            cleaned_content = f"# {cleaned_content.strip()}"
        else:
            cleaned_content = content
        return cleaned_content
    # Clean content before the first '#' in final_version
    cleaned_final_version = clean_generated_content(final_version)
    return cleaned_final_version

# Save the final content as Markdown file
def save_readme_to_markdown(readme_content, vault_path, filename):
    if not os.path.exists(vault_path):
        os.makedirs(vault_path)
    
    file_path = os.path.join(vault_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(readme_content)

    print(f"README.md saved to {file_path}")
