# Code Documentation using AI

This repository contains two Python scripts that utilize Mistral NeMo to automatically generate `README` files for different types of files, such as Jupyter notebooks and Groovy pipeline scripts.

1. `feature.py` is used to generate `README` files for feature Jupyter notebooks.
2. `pipeline.py` is used to generate `README` files for pipeline Groovy files.

# Performance of the Code

To evaluate the performance of this prototype, I chose 5 feature Jupyter notebooks and 1 pipeline Groovy file for testing. These 5 feature Jupyter notebooks are run together in this pipeline. The current code and AI model can ensure a 90-95% accuracy of the README files.

## Readme file for features

### f0284.ipynb

Link to the repository of this Jupyter notebook:
https://github.com/data-community-of-practice/f0284/blob/main/f0284.ipynb

Here's the generated `README` file:

Link to the repository:
https://github.com/Wendi9805/Code-Documentation-using-AI/blob/main/README_f0284.md

### f0173.ipynb

Link to the repository of this Jupyter notebook:
https://github.com/data-community-of-practice/f0173/blob/main/f0173.ipynb

Here's the generated `README` file:

Link to the repository: 
https://github.com/Wendi9805/Code-Documentation-using-AI/blob/main/README_f0173.md

### f0255.ipynb

Link to the repository of this Jupyter notebook:
https://github.com/data-community-of-practice/f0255/blob/main/f0255.ipynb

Here's the generated `README` file:

Link to the repository: 
https://github.com/Wendi9805/Code-Documentation-using-AI/blob/main/README_f0255.md

### f0263.ipynb

Link to the repository of this Jupyter notebook:
https://github.com/data-community-of-practice/f0263/blob/main/f0263.ipynb

Here's the generated `README` file:

Link to the repository: 
https://github.com/Wendi9805/Code-Documentation-using-AI/blob/main/README_f0263.md

### f0264.ipynb

Link to the repository of this Jupyter notebook:
https://github.com/data-community-of-practice/f0264/blob/main/f0264.ipynb

Here's the generated `README` file:

Link to the repository: 
https://github.com/Wendi9805/Code-Documentation-using-AI/blob/main/README_f0264.md

## Readme file for pipeline

### p0035.groovy

Link to the repository of this Groovy file:
https://github.com/data-community-of-practice/p0035/blob/main/p0035.groovy

Here's the generated `README` file:

Link to the repository: 
https://github.com/Wendi9805/Code-Documentation-using-AI/blob/main/README_p0035.md

# Current Issues and Potential Solutions

1. **Manual File Addition**: Although the basic functionality is implemented and the accuracy is reasonably high, the current process requires manually adding files to run the scripts. In the future, we plan to enhance the user experience by adding a user interface (UI) and scripts that allow the process to run automatically, generating README files without manual intervention.

2. **Accuracy Limitations**: While most of the information in the generated README files is accurate (90% - 95%), achieving 100% accuracy remains a challenge. Occasionally, the model may misinterpret certain aspects, leading to minor information loss. For instance, a file name might not be correctly read. A possible solution to this problem is to use High-Performance Computing (HPC) to run larger models. The current 12B model seems to minimize errors to the greatest extent possible, but it cannot guarantee 100% accuracy every time. Running more powerful models on HPC could potentially reduce these inaccuracies further.

3. **Inconsistent Formatting**: The generated README files generally follow a consistent format; however, occasionally, there are minor formatting issues, such as an extra blank line or an additional asterisk (e.g., in the title generated for p0035). I have observed that these issues are more likely to occur with smaller models when the input size increases—for example, when the content of the current Jupyter notebook is lengthy. The longer the input, the more likely such problems are to occur. This could be due to the limited training of smaller models, where, when faced with large inputs, they may automatically ignore certain pieces of information. A possible solution could be to use larger models or fine-tune existing models to better handle longer inputs.
