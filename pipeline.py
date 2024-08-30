import subprocess
import time
import os

def run_model_and_generate_readme(readme_files, pipeline_path, output_readme_path):
    # Print debugging information
    print(f"Trying to open the pipeline file at: {pipeline_path}")
    
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
        with open(pipeline_path, 'r', encoding='utf-8') as pipeline_file:
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
        print(f"Error: The file '{pipeline_path}' was not found. Please check the file path and try again.")
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

    # Step 7: Save the updated README to a Markdown file
    with open(output_readme_path, 'w', encoding='utf-8') as output_file:
        output_file.write(updated_readme)

    print(f"README file has been saved to {output_readme_path}")

# Usage example:
directory = r'D:\ANU - Master of Computing\Course work\8830 - Computing Internship\Primary Project'  # File directory
readme_files = [
    os.path.join(directory, 'README_f0284.md'),  # README file 1
    os.path.join(directory, 'README_f0173.md'),  # README file 2
    os.path.join(directory, 'README_f0255.md'),  # README file 3
    os.path.join(directory, 'README_f0263.md'),  # README file 4
    os.path.join(directory, 'README_f0264.md')   # README file 5
]
pipeline_path = os.path.join(directory, 'p0035.groovy')  # Update to your Groovy-format pipeline file path
output_readme_path = os.path.join(directory, 'generated_readme.md')

run_model_and_generate_readme(readme_files, pipeline_path, output_readme_path)
