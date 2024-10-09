# This python file is to generate readme files for all pipeline files

import os
import sys # Pass the parameters from Javascript code to Python code
from pipeline_readme_generator import run_model_and_generate_readme, extract_feature_ids_from_groovy, save_readme_to_markdown
import time # Provides time-related functions, such as measuring execution time and creating delays.
import threading # Allows for creating and managing threads, enabling parallel task execution.

# Get the current time
elapsed_time = 0
# Global variable for counting the number of files processed
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

def generate_readme_for_all_pipelines(groovy_directory_path, readme_directory_path):
    
    global file_number
    
    # Traverse the provided directory and search for all .groovy files
    groovy_files = [f for f in os.listdir(groovy_directory_path) if f.endswith('.groovy')]

    if not groovy_files:
        print(f"No Groovy pipeline files (.groovy) found in the directory: {groovy_directory_path}")
        return
    time3 = elapsed_time

    # Generate a README file for each pipeline
    for groovy_file in groovy_files:
        groovy_file_path = os.path.join(groovy_directory_path, groovy_file)
        try:
            time1 = elapsed_time
            print(f"\033[92mProcessing Groovy pipeline: {groovy_file}\033[0m\n")

            # Extract feature IDs in the format (fXXXX)
            feature_ids = extract_feature_ids_from_groovy(groovy_file_path)
            
            # Check if all required feature README files exist
            missing_readmes = []
            for feature_id in feature_ids:
                readme_path = os.path.join(readme_directory_path, f"README_{feature_id}.md")
                if not os.path.exists(readme_path):
                    missing_readmes.append(readme_path)

            if missing_readmes:
                print(f"\033[31mWARNING: Missing required README files for features: {', '.join(missing_readmes)}. Skipping this pipeline.\033[0m\n")
                continue  # Skip the current Groovy file and proceed to the next one if missing readmes

            # Get the groovy file name without the extension
            groovy_name = os.path.splitext(os.path.basename(groovy_file_path))[0]

            refined_readme_path = os.path.join(groovy_directory_path, f"README_{groovy_name}.md")

            print(f"\033[92mGenerating README file for current groovy file (may take around 60 seconds averagely)...\033[0m\n")
            # Generate the README file for the pipeline
            disable_print()
            final_content = run_model_and_generate_readme(groovy_file_path, readme_directory_path)
            enable_print()

            save_readme_to_markdown(refined_readme_path, final_content)

            time2 = elapsed_time - time1
            file_number = file_number + 1

            print(f"Pipeline README generated for {groovy_file} and saved as: {refined_readme_path}, took {time2} seconds!\n")

        except Exception as e:
            print(f"Error processing {groovy_file}: {str(e)}")

    time4 = elapsed_time - time3
    print(f"\033[43m{file_number} README files have been generated and saved as: {refined_readme_path}, took {time4} seconds in total!\033[0m\n")


# main function to be called when need
def main(groovy_directory_path, readme_directory_path):

    start_timer()

    if os.path.isdir(groovy_directory_path) and os.path.isdir(readme_directory_path):
        generate_readme_for_all_pipelines(groovy_directory_path, readme_directory_path)
    else:
        print(f"Invalid directory paths provided.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        groovy_directory_path = sys.argv[1]
        readme_directory_path = sys.argv[2]
        main(groovy_directory_path, readme_directory_path)
    else:
        print("Usage: python script.py <groovy_directory_path> <readme_directory_path>")