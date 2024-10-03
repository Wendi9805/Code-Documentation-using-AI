# README: Code-Documentation-using-AI

## Introduction

First, introduce the main functionalities of each Python file in this project:

- **`download.py`**: Downloads feature files named in the format `fXXX` and pipeline files named `pXXX` from a specified GitHub repository.

- **`feature_readme_generator.py`**: Generates README files for individual Jupyter Notebooks corresponding to a feature.

- **`feature_readme_auto_generator.py`**: Generates README files for all Jupyter Notebooks in a specified folder containing multiple features.

- **`pipeline_readme_generator.py`**: Allows the selection of a pipeline's Groovy file, and checks if the README files for all related features exist. If they do, it generates a README file for the selected Groovy pipeline.

- **`pipeline_readme_auto_generator.py`**: Processes all pipeline Groovy files in a specified folder, checks if the README files for all related features exist. If they do, it generates README files for all Groovy pipeline.

## Prerequisites

- **Python**: The version used in this project is v3.12.3, but earlier versions of Python should work as well.

- **Node.js**: The version used in this project is v20.17.0. [Link to install Node.js](https://nodejs.org/en).

- **Dependencies**: Make sure to install the following dependencies: `os`, `re`, `sys`, `subprocess`, `time`, `tkinter`, `nbformat`, `github`, and `requests`.

- **Ollama**: Visit the Ollama website to download the appropriate version for your system. Once installed, run the following command to install Mistral NeMo:

```
 ollama run mistral-nemo
```

- **Vscode**: Install the vscode for manage the code and extention

## Usage Instructions

### Step 1: Install the Extension

- Open Visual Studio Code.

- Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by using the shortcut `Ctrl+Shift+X`.

- Click on the three-dot menu in the Extensions view and select `Install from VSIX....`

- Select the `.vsix` file you downloaded from Github and follow the prompts to install the extension.

### Step 2: How to Use This Extension

The extension provides five tasks (Task 0 to Task 4) that you can run using the Command Palette.

#### Task 0: Download Feature and Pipeline Files from GitHub

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Download Feature Notebooks from GitHub` or `Readme Generator: Download Pipeline Groovy Files from GitHub` depending on what you want to download.

- Enter your GitHub token when prompted. This token should have access to the **data-community-of-practice** repository.

- Enter the name of the GitHub organization (I.e. data-community-of-practice).

- Select the folder where you want to save the downloaded files.

- Enter the maximum number of files to download.

#### Task 1: Generate README File for one Jupyter Notebook

- Open the Jupyter Notebook file in the editor that you want to generate a README for (it should be a `.ipynb` file).

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for current Jupyter Notebook`.

- The extension will automatically detect the currently active Jupyter Notebook and generate a README file for it.

- The generated README file will be saved in the same directory as the notebook.


#### Task 2: Generate README Files for All Jupyter Notebooks

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for All Feature Notebooks in Selected Folder`.

- Select the folder that contains all the Jupyter Notebooks you want to generate README files for.

- The extension will generate README files for each notebook in the selected folder.

- The README files will be saved in the same folder as the notebooks.

#### Task 3: Generate README File for One Groovy Notebook

- Open the Groovy pipeline file that you want to generate a README for (it should be a `.groovy` file).

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for current Groovy Pipeline`.

- Select the folder where the feature README files are saved (these should be pre-generated).

- The extension will check if all the necessary feature README files exist. If they do, it will generate the README file for the pipeline.

- The generated README file will be saved in the same folder as the Groovy pipeline file.

Note: The reason for checking if all the README files related to the selected pipeline Groovy file exist in the folder you just chose is primarily because generating a README file solely based on the pipeline's content wouldn't be accurate enough. It also requires the information from the features themselves. The pre-generated README files for the features provide more reliable information.

#### Task 4: Generate README Files for All Groovy Notebooks

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for All Groovy Pipelines in Selected Folder`.

- Select the folder that contains all the Groovy pipeline files you want to generate README files for.

- Select the folder where the feature README files are saved (these should be pre-generated).

- The extension will check each pipeline file to ensure all the required feature README files exist. If they do, a README file will be generated for the pipeline. If any feature README files are missing, the pipeline will be skipped.

- The README files will be saved in the same folder as the Groovy files.

## Additional Notes

- I put some example output of feature and pipeline Readme files in ths repo as well.

- The pipeline's README file generation will result in two README files. The one without "-a" in the filename is the one we need, while the one with "-a" is the pre-formatted README that I haven't had a chance to delete yet. I will remove it later.

- Please do not rename the generated README files; keep the default names. In the future, we plan to add functionality for customizing the file naming format.

- This project's code is tailored specifically for our company's repository, as our code structure and naming conventions follow consistent standards. If applied to other repositories where code format and naming conventions differ significantly from ours, the results may not be as effective.