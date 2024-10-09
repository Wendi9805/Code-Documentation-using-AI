# Jenkins Pipeline for Data Backup and Script Conversion

## Project Summary

This Jenkinsfile is designed to automate the following tasks:
1. Create a versioned backup of MongoDB data from the `nl0014` database.
2. Convert Jupyter Notebooks into Python scripts for execution.
3. Generate metadata CSV files using Neo4j connection details.
4. Process MongoDB data and create grant result CSV files.
5. Upload both the MongoDB dump and processed CSV files to a Swift storage service.

## Code Repositories Included

- **f0206: Machine Learning Model Development**
  - This project aims to develop a machine learning model for predicting customer churn in telecommunications, utilizing various customer attributes and usage patterns. The performance of the model is evaluated with metrics like accuracy, precision, recall, and F1-score.

- **f0220: Neo4j to PostgreSQL Data Migration**
  - This project focuses on exporting data from a Neo4j database into a PostgreSQL database. It involves reading configuration settings, starting logging, and using MongoDB drivers for inserting ARC organizations, relationships, grants, funding objectives, and additional CSV files.

- **f0223: Admin Organisations Insertion into PostgreSQL**
  - This notebook is dedicated to inserting admin organisations into a PostgreSQL database. It includes steps such as reading configuration settings, initiating logging, executing insertions for admin organisations, classifications, and FoR (Field of Research) data, including FoR 2020.

- **f0242: ABR Organisations Insertion into PostgreSQL**
  - This project involves inserting ABR organisations into a PostgreSQL database. The process starts by reading configuration settings and initiating logging. It uses a PostgreSQL driver to insert data into the `admin_organisations` table.

- **f0209: NL0014 Database Result Summary**
  - This notebook summarizes results from specific feature sets in the `nl0014` database using the MongoDB driver to read input from `grants_all` and `grants_for_all` collections.

## Usage Instructions

1. **Install Dependencies:**
   - Ensure that all necessary dependencies, such as `mongodump`, are installed on the Jenkins server.
2. **Configure Environment Variables:**
   - Set up database credentials, host details, and Swift storage service parameters in the respective scripts or configuration files.
3. **Update Version Numbers and File Paths:**
   - Update the version number and file paths as needed before running the pipeline.
4. **Run Jenkinsfile Stages:**
   1. **Stage `f0001: Preprocess`**:
      - Initializes configurations for Jupyter Notebooks and Python scripts.
      - Sets up necessary environment variables, such as PATH for Jupyter Notebook binaries.
      - Converts Jupyter Notebooks into executable Python scripts.

   2. **Stage `f0205: Make Metadata CSV`**:
      - Configures a metadata script with necessary parameters like Neo4j connection details and debug mode.
      - Executes the Python script to generate a metadata file.

   3. **Stage `Make Grant Result CSV` (f209)**:
      - Sets up configurations for generating grant result CSV files from MongoDB data.
      - Runs a Python script to process and create the CSV file.

   4. **Stage `Upload to Nectar for Backup`**:
      - Updates the version number in the CSV filename.
      - Moves and renames the generated CSV files.
      - Executes a shell script (`f0032.sh`) to upload both the MongoDB dump and CSV file to Swift storage.

By following these steps, you can automate the data backup process from MongoDB databases using Jenkins pipelines.

