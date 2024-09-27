# README: Code-Documentation-using-AI

## Introduction

First, introduce the main functionalities of each Python file in this project:

- **`gui.py`**: Responsible for generating the UI of the project.

- **`testDownload.py`**: Downloads feature files named in the format `fXXX` and pipeline files named `pXXX` from a specified GitHub repository.

- **`feature_readme_generator.py`**: Generates README files for individual Jupyter Notebooks corresponding to a feature.

- **`feature_readme_auto_generator.py`**: Generates README files for all Jupyter Notebooks in a specified folder containing multiple features.

- **`pipeline_readme_generator.py`**: Allows the selection of a pipeline's Groovy file, and checks if the README files for all related features exist. If they do, it generates a README file for the selected Groovy pipeline.

- **`pipeline_readme_auto_generator.py`**: Processes all pipeline Groovy files in a specified folder, checks if the README files for all related features exist. If they do, it generates README files for all Groovy pipeline.

## Prerequisites

- **Python**: The version used in this project is 3.12.3, but earlier versions of Python should work as well.

- **Dependencies**: Make sure to install the following dependencies: `os`, `re`, `subprocess`, `time`, `tkinter`, `nbformat`, `github`, and `requests`.

- **Ollama**: Visit the Ollama website to download the appropriate version for your system. Once installed, run the following command to install Mistral NeMo:

```
 ollama run mistral-nemo
```

- **Vscode**: Install the vscode for manage the code

## Usage Instructions

### Step 1: Configure GitHub API Token and Repository Settings

- Go to **`gui.py`**, and on lines 57 and 73, replace `token = "Your Github API token"` with the GitHub API token for the account that can access our **data-community-of-practice** repository.

- On lines 58 and 74, `org = "data-community-of-practice"` already points to our GitHub repository, so no changes are needed there.

- On lines 59 and 75, you can modify `max_downloads = 5` to adjust the number of feature and pipeline files to be downloaded from GitHub when the code runs. The default is set to 5.

### Step 2: Run the Project

- Run the following command to start the project:

```
python gui.py
```

After running the command, you will see a UI like this:

![](https://raw.githubusercontent.com/Wendi9805/Code-Documentation-using-AI/refs/heads/main/Images%20for%20README/1.png)

### Step 3: Introduce How to Use This Application

#### Task 0: Download All Files from the Repo

- The **`Select Your Jupyter Notebook`** button allows you to choose the directory where the downloaded files will be saved.

- The **`Download All the Feature Files`** button will download all the feature Jupyter Notebooks named `fXXXX` from our repository.

- The **`Download All the Pipeline Files`** button will download all the pipeline Groovy files named `pXXXX` from our repository.

![](https://raw.githubusercontent.com/Wendi9805/Code-Documentation-using-AI/refs/heads/main/Images%20for%20README/2.jpg)

#### Task 1: Generate README File for a one Jupyter Notebook

- The **`Select Your Jupyter Notebook`** button allows you to choose a feature Jupyter Notebook for which you want to generate a README file.

- The **`Generate README Files for This Feature`** button generates the README file for the selected Jupyter Notebook and saves it in the same directory as the feature Jupyter Notebook.

![](https://raw.githubusercontent.com/Wendi9805/Code-Documentation-using-AI/refs/heads/main/Images%20for%20README/3.jpg)


#### Task 2: Generate README Files for All Jupyter Notebooks

- The **`Select Directory for All Jupyter Notebooks`** button allows you to choose the folder where all the feature Jupyter Notebooks are saved.

- The **`Generate README Files for All the Features`** button generates README files for all the selected Jupyter Notebooks in the specified folder, one by one.

![](https://raw.githubusercontent.com/Wendi9805/Code-Documentation-using-AI/refs/heads/main/Images%20for%20README/4.jpg)

#### Task 3: Generate README File for One Groovy Notebook

- The **`Select Your Groovy File`** button allows you to choose the pipeline Groovy file for which you want to generate a README file.

- The **`Select Directory for Feature README Files`** button lets you select the folder where all the README files for the features are saved.

- The **`Generate README for This Pipeline`** button will first check if all the README files related to the selected pipeline Groovy file exist in the folder you just chose. If they do, it will generate the README file for the pipeline.

Note: The reason for checking if all the README files related to the selected pipeline Groovy file exist in the folder you just chose is primarily because generating a README file solely based on the pipeline's content wouldn't be accurate enough. It also requires the information from the features themselves. The pre-generated README files for the features provide more reliable information.

![](https://raw.githubusercontent.com/Wendi9805/Code-Documentation-using-AI/refs/heads/main/Images%20for%20README/5.jpg)

#### Task 4: Generate README Files for All Groovy Notebooks

- The **`Select Directory for All Groovy Files`** button allows you to choose the folder where all pipeline Groovy files are saved.

- The **`Select Directory for Feature README Files`** button lets you select the folder where all the README files for the features are saved.

- The **`Generate README File for All Pipelines`** button will sequentially check if the README files for the features related to each pipeline Groovy file exist. If they do, it will generate the README file for that pipeline. If not, it will skip to the next pipeline file and continue the same process.

![](https://raw.githubusercontent.com/Wendi9805/Code-Documentation-using-AI/refs/heads/main/Images%20for%20README/6.jpg)

## Additional Notes

- I put some example output of feature and pipeline Readme files in ths repo as well.

- The pipeline's README file generation will result in two README files. The one without "-a" in the filename is the one we need, while the one with "-a" is the pre-formatted README that I haven't had a chance to delete yet. I will remove it later.

- Please do not rename the generated README files; keep the default names. In the future, we plan to add functionality for customizing the file naming format.

- This project's code is tailored specifically for our company's repository, as our code structure and naming conventions follow consistent standards. If applied to other repositories where code format and naming conventions differ significantly from ours, the results may not be as effective.