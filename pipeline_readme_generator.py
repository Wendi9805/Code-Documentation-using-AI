# This python file is to generate readme files for one pipeline files

import os # Provides functions to interact with the operating system, such as reading directories, file paths, and checking file existence.
import re # Allows pattern matching using regular expressions, here used to extract feature IDs from Groovy files.
import subprocess # Used to execute external commands or programs, in this case, it's used to run the 'ollama' model for generating and refining README files.
import time # Provides time-related functions, such as adding delays between steps with 'sleep', ensuring the external model has enough time to process.

# Extract feature IDs from the Groovy file
def extract_feature_ids_from_groovy(groovy_file_path):
    """
    Parse the Groovy file and extract the feature IDs in the format (fXXXX).
    Returns a list of feature IDs, such as ['f0284', 'f0173', 'f0255', 'f0263', 'f0264'].
    """
    feature_ids = []
    feature_pattern = re.compile(r'git@github\.com:data-community-of-practice/(f\d{4})\.git')

    with open(groovy_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = feature_pattern.search(line)
            if match:
                feature_ids.append(match.group(1))
                
    print(f"All detected feature IDs: {feature_ids}")  # Output all detected feature IDs
    return feature_ids

# Generate the readme file for a pipeline
def run_model_and_generate_readme(groovy_file_path, directory, initial_readme_path, refined_readme_path):
    # Step 0: Extract feature IDs from the Groovy file
    feature_ids = extract_feature_ids_from_groovy(groovy_file_path)
    print(f"Extracted feature IDs: {feature_ids}")

    # Generate the list of README file paths based on feature IDs
    readme_files = [os.path.join(directory, f"README_{feature_id}.md") for feature_id in feature_ids]
    print(f"Generated README file paths: {readme_files}")

    # Store titles and summaries from each README file
    titles_and_summaries = []

    # Step 1: Open terminal and run `ollama run mistral-nemo`
    process = subprocess.Popen(
        ['ollama', 'run', 'mistral-nemo'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )

    # Step 2: Wait for the model to start
    time.sleep(5)  # Adjust the sleep time as needed

    # Step 3: Send the contents of each README file to the model and extract titles and summaries
    for i, file_path in enumerate(readme_files):
        if not os.path.exists(file_path):
            print(f"WARNING: {file_path} does not exist, skipping this file.")
            continue

        with open(file_path, 'r', encoding='utf-8') as md_file:
            content = md_file.read()

            # Extract the # Title part of the README file
            title_line = content.split('\n')[0] if content.startswith('#') else "No Title Found"
            title = title_line.strip('#').strip()  # Remove the '#' and any leading/trailing spaces

            # Extract the ## Project Summary part of the README file
            summary_start = content.find('## Project Summary')
            project_summary = "No Summary Found"
            
            if summary_start != -1:
                # Extract content after '## Project Summary'
                summary_content = content[summary_start:].split('\n')
                # Find the first non-empty line after '## Project Summary'
                for line in summary_content[1:]:
                    if line.strip():  # Skip empty lines
                        project_summary = line.strip()
                        break

            # Combine title and summary in a formatted string
            formatted_title_and_summary = f"{title}\n  {project_summary}"
            titles_and_summaries.append(formatted_title_and_summary)

            # Provide a prompt to the model
            prompt = f"Below is the content of README file {i+1} describing a codebase. Please remember this information:\n\n{content}\n\n"
            process.stdin.write(prompt)
            process.stdin.flush()
            time.sleep(10)  # Wait for the model to process
            print(f"Sent the {i+1}th README file")

    # Combine titles and summaries into a formatted string with an extra blank line between each entry
    combined_titles_and_summaries = "## Code Repositories Included\n\n" + "\n\n".join([f"- {item}" for item in titles_and_summaries])

    # Step 4: Read and send the pipeline code from the Groovy file to the model
    try:
        with open(groovy_file_path, 'r', encoding='utf-8') as pipeline_file:
            pipeline_code = pipeline_file.read()
            # Prompt the model to generate the final README based on the combined information
            prompt = f"""Based on the contents of the provided README files, generate a comprehensive README for the following pipeline code:
            
                {pipeline_code}

                The README should include a Title, Summary, and Usage Instructions sections that reflect the combined information from all the previous README files. The format should be strictly like this:
                
                (do not use * in the title of each section, just use # + the title of each section)
                
                # Title

                ## Summary (only use one paragraph, less than 200 words)

                ## Usage Instruction
                1. Step 1
                2. Step 2
                .... 
                """
            process.stdin.write(prompt)
            process.stdin.flush()
            time.sleep(10)
    except FileNotFoundError:
        print(f"Error: The file '{groovy_file_path}' was not found. Please check the file path and try again.")
        return

    # Step 5: Capture the model's output (assuming the model generates the README in the output)
    model_output, _ = process.communicate()

    # Step 6: Insert the combined titles and summaries after the Summary section in the model's generated README
    summary_section_index = model_output.find('## Summary')
    usage_instruction_section_index = model_output.find('## Usage Instructions')

    if summary_section_index != -1 and usage_instruction_section_index != -1:
        # Inject titles and summaries between Summary and Usage Instructions sections
        updated_readme = (
            model_output[:usage_instruction_section_index].strip() +
            '\n\n' + combined_titles_and_summaries + '\n\n' +
            model_output[usage_instruction_section_index:].strip()
        )
    else:
        # If the output doesn't match the expected format, append titles and summaries at the end
        updated_readme = model_output + '\n\n' + combined_titles_and_summaries

    # Step 7: Save the initial generated README to a Markdown file
    with open(initial_readme_path, 'w', encoding='utf-8') as output_file:
        output_file.write(updated_readme)
    
    print(f"Initial README file has been saved to {initial_readme_path}")

    # Step 8: Read the generated README and send it to the model for format refinement
    with open(initial_readme_path, 'r', encoding='utf-8') as generated_readme_file:
        generated_readme_content = generated_readme_file.read()

    # Provide a new prompt to refine the README format
    refine_prompt = f"""
    The README content to be refined is as follows:

    {generated_readme_content}

    However, the format and the order of this readme file maybe different from the standard format, help me to edit the format based on the standard format below without losing information:

    # Your title

    ## Project Summary

    (here is the descrption of your project summary)

    ## Code Repositories Included

    - fXXX: title
    (description)

    - fXXX: title
    (description)

    - fXXX: title
    (description)

    - fXXX: title
    (description)

    - fXXX: title
    (description)
    ...

    ## Usage Instructions

    1. **Usage Instruction1:**
    - 
    - 
    ....

    2. **Usage Instruction2:**
    - 
    - 
    ....

    2. **Usage Instruction3:**
    - 
    - 
    ....
    """

    # Re-run the model to refine the README format
    process = subprocess.Popen(
        ['ollama', 'run', 'mistral-nemo'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )
    process.stdin.write(refine_prompt)
    process.stdin.flush()
    time.sleep(10)

    # Step 9: Capture the refined README from the model's output
    refined_readme_output, _ = process.communicate()

    # Remove content before the first `#` in the refined README output
    first_hash_index = refined_readme_output.find('#')
    if first_hash_index != -1:
        refined_readme_output = refined_readme_output[first_hash_index:]

    # Step 10: Save the refined README to a Markdown file
    with open(refined_readme_path, 'w', encoding='utf-8') as output_file:
        output_file.write(refined_readme_output)

    print(f"Refined README file has been saved to {refined_readme_path}")


# # Example Usage：
# groovy_file_path = r'D:\ANU - Master of Computing\Course work\8830 - Computing Internship\Primary Project\p0035.groovy'
# directory = r'D:\ANU - Master of Computing\Course work\8830 - Computing Internship\Primary Project'
# initial_readme_path = os.path.join(directory, 'initial_generated_readme.md')
# refined_readme_path = os.path.join(directory, 'refined_generated_readme.md')

# run_model_and_generate_readme(groovy_file_path, directory, initial_readme_path, refined_readme_path)
