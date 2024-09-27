# GUI interface for generating README files for Jupyter Notebooks and Pipelines

# Tkinter and OS modules are used for creating a GUI to interact with files and directories.
# filedialog: Used to open file/directory dialogs.
# scrolledtext: Provides a scrollable text widget.
# messagebox: For displaying popup messages.
# os: Provides functions for interacting with the operating system, such as file path operations.
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os

# These imports handle specific functions for generating README files for Jupyter Notebooks and Groovy Pipelines.
# They also include functions for downloading repositories from GitHub
from feature_readme_generator import generate_readme_from_notebook, edit_readme_format, save_readme_to_markdown
from pipeline_readme_generator import run_model_and_generate_readme
from feature_readme_auto_generator import generate_readme_for_all_notebooks
from pipeline_readme_auto_generator import generate_readme_for_all_pipelines
from testDownload import download_notebooks_from_repos
from testDownload import download_pipeline_from_repos

# Display the UI for users
def create_gui():

    # Creating the Main UI Window
    root = tk.Tk()
    root.title("Jupyter Notebook README Generator")
    root.geometry("1000x800")

    # Save all the directories or paths users choose

    download_directory_path_var = tk.StringVar() # Directory to download files
    notebook_file_path_var = tk.StringVar() # Path to the Jupyter Notebook users choose
    groovy_file_path_var = tk.StringVar() # Path to the Groovy Notebook users choose
    feature_directory_path_var = tk.StringVar()
    all_feature_directory_path_var = tk.StringVar()
    all_pipeline_directory_path_var = tk.StringVar()
    feature_directory2_path_var = tk.StringVar()

    # All the functions related to the Buttons in UI:

    # Task 0. Download all the files from repo:

    ## Select the directory to save the downloaded files
    def select_download_directory():
        directory_path = filedialog.askdirectory(
            title="Select Directory to Save README Files"
        )
        download_directory_path_var.set(directory_path)
    
    ## Download all the feature files
    def download_feature_files():
        download_path = download_directory_path_var.get()
        if not download_path:
            messagebox.showwarning("Warning", "Please select a directory.")
            return
        try:
            token = "Your Github API token"
            org = "data-community-of-practice"
            max_downloads = 5
            download_notebooks_from_repos(token,org,download_path,max_downloads)
            messagebox.showinfo("Success", f"All the files are saved to {download_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ## Download all the pipeline files
    def download_pipeline_files():
        download_path = download_directory_path_var.get()
        if not download_path:
            messagebox.showwarning("Warning", "Please select a directory.")
            return
        try:
            token = "Your Github API token"
            org = "data-community-of-practice"
            max_downloads = 5
            download_pipeline_from_repos(token,org,download_path,max_downloads)
            messagebox.showinfo("Success", f"All the files are saved to {download_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Task 1. Generate Readme File for One Jupyter Notebook:

    ## Select the directory to the Jupyter Notebook
    def select_notebook_file():
        file_path = filedialog.askopenfilename(
            filetypes=[("Jupyter Notebooks", "*.ipynb")],
            title="Select a Jupyter Notebook File"
        )
        notebook_file_path_var.set(file_path)

    ## Generate the readme file for one Jupyter Notebook
    def generate_readme():
        notebook_path = notebook_file_path_var.get()
        if not notebook_path:
            messagebox.showwarning("Warning", "Please select a Jupyter Notebook file.")
            return
        
        try:
            # Generate README content
            readme_content = generate_readme_from_notebook(notebook_path)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, readme_content)

           # Edit and save the final README
            final_readme_content = edit_readme_format(readme_content)
            notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
            readme_filename = f"README_{notebook_name}.md"
            output_path = os.path.join(os.path.dirname(notebook_path), readme_filename)
            save_readme_to_markdown(final_readme_content, os.path.dirname(notebook_path), readme_filename)
            
            messagebox.showinfo("Success", f"README_final.md generated and saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Task 2. Generate Readme File for All Jupyter Notebook:

    ## Select the directory to the all Jupyter Notebooks
    def select_directory_all_features():
        all_feature_directory_path = filedialog.askdirectory(
            title="Select Directory to Save README Files"
        )
        all_feature_directory_path_var.set(all_feature_directory_path)

    ## Generate readme file for all Jupyter Notebooks
    def generate_all_feature_readme():
        all_feature_directory_path = all_feature_directory_path_var.get()
        if not all_feature_directory_path:
           messagebox.showwarning("Warning", "Please select a Jupyter Notebook file.")
           return
        
        try: 
            generate_readme_for_all_notebooks(all_feature_directory_path)
            messagebox.showinfo("Success", f"README_final.md generated and saved to {all_feature_directory_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    # Task 3. Generate Readme File for One Groovy Notebook:

    ## Select the directory to one Groovy Notebook
    def select_groovy_file():
        groovy_file_path = filedialog.askopenfilename(
            filetypes=[("Groovy Files", "*.groovy")],
            title="Select a Groovy Pipeline File"
        )
        groovy_file_path_var.set(groovy_file_path)

    ## Select the directory to the Jupyter Notebooks Readme files related to this Groovy Notebook
    def select_directory():
        directory_path = filedialog.askdirectory(
            title="Select Directory to Feature README Files"
        )
        feature_directory_path_var.set(directory_path)
        
    ## Generate Readme File for One Groovy Notebook
    def generate_pipeline_readme():
        groovy_file_path = groovy_file_path_var.get()
        directory_path = feature_directory_path_var.get()

        if not groovy_file_path:
            messagebox.showwarning("Warning", "Please select a Groovy pipeline file.")
            return
        if not directory_path:
            messagebox.showwarning("Warning", "Please select a directory.")
            return

        try:
            groovy_name = os.path.splitext(os.path.basename(groovy_file_path))[0]
            initial_readme_path = os.path.join(directory_path, f"README_{groovy_name}_a.md")
            refined_readme_path = os.path.join(directory_path, f"README_{groovy_name}.md")
            run_model_and_generate_readme(groovy_file_path, directory_path, initial_readme_path, refined_readme_path)
            
            messagebox.showinfo("Success", f"Pipeline README generated and saved to {directory_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Task 4. Generate Readme File for all Groovy Notebooks:

    ## Select the directory to All Groovy Notebooks
    def select_directory_all_pipelines():
        all_pipeline_directory_path = filedialog.askdirectory(
            title="Select Directory to all Groovy Notebooks"
        )
        all_pipeline_directory_path_var.set(all_pipeline_directory_path)
    
    ## Select the directory to the Jupyter Notebooks Readme files related to this Groovy Notebooks
    def select_directory2():
        directory2_path = filedialog.askdirectory(
            title="Select Directory to Feature README Files"
        )
        feature_directory2_path_var.set(directory2_path)

    ## enerate Readme File for all Groovy Notebooks
    def generate_all_pipeline_readme():
        all_pipeline_directory_path = all_pipeline_directory_path_var.get()
        directory_path2 = feature_directory2_path_var.get()

        if not all_pipeline_directory_path:
            messagebox.showwarning("Warning", "Please select a Groovy pipeline file.")
            return
        if not directory_path2:
            messagebox.showwarning("Warning", "Please select a directory.")
            return
        
        try:
            generate_readme_for_all_pipelines(all_pipeline_directory_path, directory_path2)
            messagebox.showinfo("Success", f"Pipeline README generated and saved to {all_pipeline_directory_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # All the buttons in UI:

    # Task 0. Download all the files from repo
    instruction_label0 = tk.Label(root, text="Task 0: Download All the Files from Repo", anchor='w')
    instruction_label0.pack(fill='x', padx=30, pady=10)

    button_frame0 = tk.Frame(root)
    button_frame0.pack(anchor='w', padx=30, pady=5)

    select_button0 = tk.Button(button_frame0, text="Select Directory to Save Files", command=select_download_directory)
    select_button0.pack(side='left', padx=10)

    generate_button0 = tk.Button(button_frame0, text="Download All the Feature files", command=download_feature_files)
    generate_button0.pack(side='left', padx=10)

    generate_button00 = tk.Button(button_frame0, text="Download All the Pipeline files", command=download_pipeline_files)
    generate_button00.pack(side='left', padx=10)

    file_label = tk.Label(root, textvariable=download_directory_path_var, anchor='w')
    file_label.pack(fill='x', padx=30, pady=5) 

    # Task 1. Generate Readme File for One Jupyter Notebook
    instruction_label1 = tk.Label(root, text="Task 1: Generate Readme File for one Jupyter Notebook", anchor='w')
    instruction_label1.pack(fill='x', padx=30, pady=10)

    button_frame1 = tk.Frame(root)
    button_frame1.pack(anchor='w', padx=30, pady=5)

    select_button1 = tk.Button(button_frame1, text="Select Your Jupyter Notebook", command=select_notebook_file)
    select_button1.pack(side='left', padx=10)

    generate_button1 = tk.Button(button_frame1, text="Generate README File for This Feature", command=generate_readme)
    generate_button1.pack(side='right', padx=10)

    file_label = tk.Label(root, textvariable=notebook_file_path_var, anchor='w')
    file_label.pack(fill='x', padx=30, pady=5)

    # Task 2. Generate Readme File for All Jupyter Notebook
    instruction_label2 = tk.Label(root, text="Task 2: Generate Readme File for All Jupyter Notebook", anchor='w')
    instruction_label2.pack(fill='x', padx=30, pady=10)

    button_frame2 = tk.Frame(root)
    button_frame2.pack(anchor='w', padx=30, pady=5)

    select_button2 = tk.Button(button_frame2, text="Select Directory for All Jupyter Notebooks", command=select_directory_all_features)
    select_button2.pack(side='left', padx=10)

    generate_button2 = tk.Button(button_frame2, text="Generate README Files for All the Features", command=generate_all_feature_readme)
    generate_button2.pack(side='right', padx=10)

    file_labe2 = tk.Label(root, textvariable=all_feature_directory_path_var, anchor='w')
    file_labe2.pack(fill='x', padx=30, pady=5)

    # Task 3. Generate Readme File for One Groovy Notebook
    instruction_label3 = tk.Label(root, text="Task 3: Generate Readme File for One Groovy Notebook", anchor='w')
    instruction_label3.pack(fill='x', padx=30, pady=10)
    
    button_frame3 = tk.Frame(root)
    button_frame3.pack(anchor='w', padx=30, pady=5)

    select_groovy_button = tk.Button(button_frame3, text="Select Your Groovy File", command=select_groovy_file)
    select_groovy_button.pack(side='left', padx=10)

    select_directory_button = tk.Button(button_frame3, text="Select Directory for Feature README Files", command=select_directory)
    select_directory_button.pack(side='left', padx=10)

    generate_pipeline_button = tk.Button(button_frame3, text="Generate README for This Pipeline", command=generate_pipeline_readme)
    generate_pipeline_button.pack(side='left', padx=10)

    groovy_file_label = tk.Label(root, textvariable=groovy_file_path_var,anchor='w')
    groovy_file_label.pack(fill='x', padx=30, pady=5)

    directory_label = tk.Label(root, textvariable=feature_directory_path_var,anchor='w')
    directory_label.pack(fill='x', padx=30, pady=5)

    # Task 4. Generate Readme File for all Groovy Notebook
    instruction_label4 = tk.Label(root, text="Task 4: Generate Readme File for All Groovy Notebooks", anchor='w')
    instruction_label4.pack(fill='x', padx=30, pady=10)

    button_frame4 = tk.Frame(root)
    button_frame4.pack(anchor='w', padx=30, pady=5)

    select_groovy_button2 = tk.Button(button_frame4, text="Select Directory for All Groovy Files", command=select_directory_all_pipelines)
    select_groovy_button2.pack(side='left', padx=10)
    
    select_directory_button2 = tk.Button(button_frame4, text="Select Directory for Feature README Files", command=select_directory2)
    select_directory_button2.pack(side='left', padx=10)

    generate_pipeline_button3 = tk.Button(button_frame4, text="Generate README File for All Pipelines", command=generate_all_pipeline_readme)
    generate_pipeline_button3.pack(side='left', padx=10)

    groovy_file_label2 = tk.Label(root, textvariable=all_pipeline_directory_path_var,anchor='w')
    groovy_file_label2.pack(fill='x', padx=30, pady=5)

    directory_label2 = tk.Label(root, textvariable=feature_directory2_path_var,anchor='w')
    directory_label2.pack(fill='x', padx=30, pady=5)

    # TODO: display the info in the terminal
    output_text = scrolledtext.ScrolledText(root, width=100, height=5)
    output_text.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
