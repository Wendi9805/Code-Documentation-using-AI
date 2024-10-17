# This python file is to generate readme files for one pipeline files

import os # Provides functions to interact with the operating system, such as reading directories, file paths, and checking file existence.
import re # Allows pattern matching using regular expressions, here used to extract feature IDs from Groovy files.
import subprocess # Used to execute external commands or programs, in this case, it's used to run the 'ollama' model for generating and refining README files.
import time # Provides time-related functions, such as adding delays between steps with 'sleep', ensuring the external model has enough time to process.
import sys # Pass the parameters from Javascript code to Python code
import threading # Allows for creating and managing threads, enabling parallel task execution.

# Get the current time
elapsed_time = 0

def timer():
    global elapsed_time
    while True:
        time.sleep(1)
        elapsed_time += 1

def start_timer():
    timer_thread = threading.Thread(target=timer)
    timer_thread.daemon = True
    timer_thread.start()

# Extract feature IDs from the Groovy file
def extract_feature_ids_from_groovy(groovy_file_path):
    """
    Parse the Groovy file and extract the feature IDs in the format (fXXXX or fXXX).
    Returns a list of feature IDs, ensuring all are in the format 'fXXXX' (four digits).
    """
    feature_ids = []
    feature_pattern = re.compile(r'stage\(\'(f\d{3,4}):')

    with open(groovy_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = feature_pattern.search(line)
            if match:
                feature_id = match.group(1)
                # If the feature ID is in the form fXXX, convert it to f0XXX
                if len(feature_id) == 4:  # Check if the ID is f followed by 3 digits
                    feature_id = feature_id[:1] + '0' + feature_id[1:]  # Add a leading zero
                feature_ids.append(feature_id)
                
    print(f"\033[92mAll detected feature IDs from this Groovy file: {feature_ids}\033[0m\n")  # Output all detected feature IDs
    return feature_ids

# Generate the readme file for a pipeline
def run_model_and_generate_readme(groovy_file_path, directory):
    # Step 0: Extract feature IDs from the Groovy file
    feature_ids = extract_feature_ids_from_groovy(groovy_file_path)

    # Generate the list of README file paths based on feature IDs
    readme_files = [os.path.join(directory, f"README_{feature_id}.md") for feature_id in feature_ids]

    # Store titles and summaries from each README file
    titles_and_summaries = []

    # Step 1: Open terminal and run `ollama run mistral-nemo`
    process = subprocess.Popen(
        ['ollama', 'run', 'qwen2.5:7b'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )

    # Step 2: Wait for the model to start
    time.sleep(3)  # Adjust the sleep time as needed

    time1 = elapsed_time

    # Step 3: Send the contents of each README file to the model and extract titles and summaries
    print(f"\033[92m1. Sending related feature README files to the model...\033[0m\n")
    for i, file_path in enumerate(readme_files):
        if not os.path.exists(file_path):
            print(f"\033[41mWARNING: {file_path} does not exist, skipping this file.\033[0m\n")
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
            time.sleep(5)  # Wait for the model to process
            print(f"Sent the {i+1}th README file")
        
    time2 = elapsed_time -time1
    print(f"All feature README files have been sent to the model, took {time2} seconds!\n")
    
    # Combine titles and summaries into a formatted string with an extra blank line between each entry
    combined_titles_and_summaries = "## Code Repositories Included\n\n" + "\n\n".join([f"- {item}" for item in titles_and_summaries])

    # Step 4: Read and send the pipeline code from the Groovy file to the model
    time3 = elapsed_time

    print(f"\033[92m2. Generating README files for this pipeline file...\033[0m\n")

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
            time.sleep(5)
    except FileNotFoundError:
        print(f"\033[31mError: The file '{groovy_file_path}' was not found. Please check the file path and try again.\033[0m\n")
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

    generated_readme_content = updated_readme
    time4 = elapsed_time - time3
    print(f"Finished the draft of README file, took {time4} seconds!\n")

    # Step 7: Edit the format and save the final version of readme file
    # Provide a new prompt to refine the README format
    print(f"\033[92m3. Editing the format of README files draft...\033[0m\n")
    time5 = elapsed_time

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
        ['ollama', 'run', 'qwen2.5:7b'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )
    process.stdin.write(refine_prompt)
    process.stdin.flush()
    time.sleep(5)

    # Step 8: Capture the refined README from the model's output
    refined_readme_output, _ = process.communicate()

    # Remove content before the first `#` in the refined README output
    first_hash_index = refined_readme_output.find('#')
    if first_hash_index != -1:
        refined_readme_output = refined_readme_output[first_hash_index:]

    time6 = elapsed_time - time5

    print(f"The format has been edited, took {time6} seconds!\n")

    return refined_readme_output

# Step 9: Save the refined README to a Markdown file
def save_readme_to_markdown(refined_readme_path, refined_readme_output):
    """
    Saves the refined README content to a Markdown file.
    Checks if the file already exists and prompts the user whether to overwrite it.
    """
    # Extract the pipeline's name from the refined_readme_path (assumes README_filename follows a standard like README_<pipeline_name>.md)
    pipeline_name = os.path.basename(refined_readme_path)

    # Check if the file already exists
    if os.path.exists(refined_readme_path):
        overwrite = input(f"The README file for the pipeline '{pipeline_name}' already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != 'y':
            print(f"Skipping save operation for '{pipeline_name}' README file.'\n")
            return  # Skip saving the file if user does not want to overwrite
    
    # Save the refined README content to a file
    with open(refined_readme_path, 'w', encoding='utf-8') as output_file:
        output_file.write(refined_readme_output)

# main function to be called when need
def main(groovy_file_path, directory):
    start_timer()
    groovy_name = os.path.splitext(os.path.basename(groovy_file_path))[0]
    refined_readme_path = os.path.join(directory, f"README_{groovy_name}.md")

    refined_readme_output = run_model_and_generate_readme(groovy_file_path, directory)

    # Save the generated README content
    save_readme_to_markdown(refined_readme_path, refined_readme_output)

    print(f"\033[43mREADME file has been saved to {refined_readme_path}, took {elapsed_time} seconds in total to generate this README file\033[0m\n")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        groovy_file_path = sys.argv[1]
        directory = sys.argv[2]
        main(groovy_file_path, directory)
    else:
        print("Usage: python script.py <groovy_file_path> <directory_for_readmes>")
