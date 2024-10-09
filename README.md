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

- **Dependencies**: Make sure to install the following dependencies: `os`, `re`, `sys`, `subprocess`, `time`, `threading`, `tkinter`, `nbformat`, `github`, and `requests`.

- **Ollama**: Visit the Ollama website to download the appropriate version for your system. Once installed, run the following command to install Qwen2.5:

```
 ollama run qwen2.5:7b
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

- Enter the name of the GitHub organization (i.e. data-community-of-practice).

- Select the folder where you want to save the downloaded files.

- Enter the maximum number of files to download.

#### Task 1: Generate README File for one Jupyter Notebook

- Open the Jupyter Notebook file in the editor that you want to generate a README for (it should be a `.ipynb` file).

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for current Jupyter Notebook`.

- The extension will automatically detect the currently active Jupyter Notebook and generate a README file for it.

- If the README file for the Jupyter Notebook already exists, you will be prompted to confirm whether you want to overwrite it. If you choose `y`, the generated README file will be saved in the same directory as the notebook.


#### Task 2: Generate README Files for All Jupyter Notebooks

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for All Feature Notebooks in Selected Folder`.

- Select the folder that contains all the Jupyter Notebooks you want to generate README files for.

- The extension will generate README files for each notebook in the selected folder.

- If the README files for the Jupyter Notebooks already exist, you will be prompted to confirm whether you want to overwrite them. If you choose `y`, the generated README files will be saved in the same folder as the notebooks.

#### Task 3: Generate README File for One Groovy Notebook

- Open the Groovy pipeline file that you want to generate a README for (it should be a `.groovy` file).

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for current Groovy Pipeline`.

- Select the folder where the feature README files are saved (these should be pre-generated).

- The extension will check if all the necessary feature README files exist. If they do, it will generate the README file for the pipeline.

- If the README file for the Groovy pipeline file already exists, you will be prompted to confirm whether you want to overwrite it. If you choose `y`, the generated README file will be saved in the same directory as the Groovy pipeline file.

Note: The reason for checking if all the README files related to the selected pipeline Groovy file exist in the folder you just chose is primarily because generating a README file solely based on the pipeline's content wouldn't be accurate enough. It also requires the information from the features themselves. The pre-generated README files for the features provide more reliable information.

#### Task 4: Generate README Files for All Groovy Notebooks

- Open the **Command Palette** using `Ctrl+Shift+P`.

- Type `Readme Generator: Generate README for All Groovy Pipelines in Selected Folder`.

- Select the folder that contains all the Groovy pipeline files you want to generate README files for.

- Select the folder where the feature README files are saved (these should be pre-generated).

- The extension will check each pipeline file to ensure all the required feature README files exist. If they do, a README file will be generated for the pipeline. If any feature README files are missing, the pipeline will be skipped.

- If the README file for the Groovy pipeline files already exist, you will be prompted to confirm whether you want to overwrite them. If you choose `y`, the generated README files will be saved in the same directory as the Groovy pipeline files.

## Additional Notes

- I put some example output of feature and pipeline Readme files in ths repo as well.

- Previously, I noticed that generating a single README file took a significant amount of time, roughly 5 minutes per file. Initially, I suspected it was either a code issue or a problem with running Ollama in multithreaded mode, but later, I discovered it was due to the Mistral NeMo model itself. Large models like this one generate text at a rate of about five words per minute on my computer. Although the process appears fast in the terminal, generating a draft README file of around 600 words takes approximately 2 minutes, and even longer when formatting corrections are applied. I found that switching to smaller models, such as Mistral 7B or Llama3 8B, greatly improved speed. After several tests, I settled on Qwen2.5 7B, which, while slightly less accurate than Mistral NeMo, offers acceptable results with much faster performance. The time to generate a single README file was reduced to about 30 seconds, significantly improving the efficiency of our model.

- If we want to switch back to using the **Mistral NeMo** model, we simply need to modify a few lines in the code: change `qwen2.5:7b` to `mistral-nemo` in **line 27** of `feature_readme_generator.py`, **line 59**, and **line 228** of `pipeline_readme_generator.py`. After saving these changes, go to the VS Code extension interface and uninstall the previous plugin. Then, in the terminal, run `ollama run mistral-nemo` to install Mistral NeMo and `vsce package` to package this plugin again. Once this process is complete, a `.vsix` file will be generated. Install this file again to update the plugin, and the switch will be applied successfully.

- **Please do not rename the generated README files**; keep the default names,as the pipeline README file generation requires checking whether the corresponding feature README files exist. Any renaming could result in mismatches or missing references during this process, causing interruptions in the pipeline's execution.

- This project's code is tailored specifically for our company's repository, as our code structure and naming conventions follow consistent standards. If applied to other repositories where code format and naming conventions differ significantly from ours, the results may not be as effective.