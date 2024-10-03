# This python file is to generate readme files for all pipeline files

import os
import sys # Pass the parameters from Javascript code to Python code
from pipeline_readme_generator import run_model_and_generate_readme, extract_feature_ids_from_groovy

def generate_readme_for_all_pipelines(groovy_directory_path, readme_directory_path):
    # Traverse the provided directory and search for all .groovy files
    groovy_files = [f for f in os.listdir(groovy_directory_path) if f.endswith('.groovy')]

    if not groovy_files:
        print(f"No Groovy pipeline files (.groovy) found in the directory: {groovy_directory_path}")
        return

    # Generate a README file for each pipeline
    for groovy_file in groovy_files:
        groovy_file_path = os.path.join(groovy_directory_path, groovy_file)
        try:
            print(f"Processing Groovy pipeline: {groovy_file}")

            # Extract feature IDs in the format (fXXXX)
            feature_ids = extract_feature_ids_from_groovy(groovy_file_path)
            
            # Check if all required feature README files exist
            missing_readmes = []
            for feature_id in feature_ids:
                readme_path = os.path.join(readme_directory_path, f"README_{feature_id}.md")
                if not os.path.exists(readme_path):
                    missing_readmes.append(readme_path)

            if missing_readmes:
                print(f"WARNING: Missing required README files for features: {', '.join(missing_readmes)}. Skipping this pipeline.")
                continue  # Skip the current Groovy file and proceed to the next one if missing readmes

            # Get the groovy file name without the extension
            groovy_name = os.path.splitext(os.path.basename(groovy_file_path))[0]

            # Set save paths for the initial and refined README files, with different naming conventions
            initial_readme_path = os.path.join(groovy_directory_path, f"README_{groovy_name}_a.md")
            refined_readme_path = os.path.join(groovy_directory_path, f"README_{groovy_name}.md")

            # Generate the README file for the pipeline
            run_model_and_generate_readme(groovy_file_path, readme_directory_path, initial_readme_path, refined_readme_path)

            print(f"Pipeline README generated for {groovy_file} and saved as: {refined_readme_path}")

        except Exception as e:
            print(f"Error processing {groovy_file}: {str(e)}")


# main function to be called when need
def main(groovy_directory_path, readme_directory_path):
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