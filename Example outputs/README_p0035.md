# Insights Database Versioning and Backup Pipeline

## Project Summary

This pipeline automates the versioning of databases, generates a dump file with the current version number, configures and runs Neo4j and PostgreSQL connections, executes Jupyter notebooks for data processing, and uploads the generated dump files to Nectar for backup. It also handles version updates by incrementing the minor version number and creating a new `version.txt` file if it doesn't exist.

## Code Repositories Included

- **f0284: Create Augmented Postgres from Neo4j**
  This project aims to create an augmented PostgreSQL database from an existing Neo4j graph database. It exports nodes and relations between them from Neo4j, processes the data using Pandas in Python, and inserts it into a PostgreSQL database with appropriate primary keys for both node and relation tables.

- **f0173: National Graph Insight Data**
  This script fetches publication data from a Neo4j graph database and stores it into a PostgreSQL table named `cop_stats_published_at`. It ensures data integrity by appending new records, replacing duplicates, and adding a primary key for efficient querying.

- **f0255: National Graph Insight Data - Exporting Most Connected Nodes**
  This project focuses on exporting the most connected nodes from a National Graph database. It connects to Neo4j and PostgreSQL databases, extracts information about the most connected nodes, ensures data integrity by dropping duplicates, and inserts processed data into a PostgreSQL table with appropriate column types and a composite primary key.

- **f0263: National Graph Insight Data - Exporting PID Coverage Per Node Type**
  This project exports PID coverage per node type from the National Graph Insight Data. It connects to Neo4j and PostgreSQL databases, retrieves data on nodes' connection counts and PID types, processes it into a dataframe, and inserts it into the PostgreSQL table `cop_pids_coverage_by_type`.

- **f0264: National Graph Insight Data**
  This project focuses on exporting organization locations from a National Graph dataset. It reads configuration data, connects to Neo4j graph database and PostgreSQL using environment variables for credentials, fetches organization countries and cities, creates a DataFrame with relevant information, and inserts this data into a PostgreSQL table named 'cop_organisation_locations'.

- **f0205: Insert Graph and PBI Collections Versions to MongoDB/Postgres**
  This project focuses on retrieving and storing versions of Graph DB (Neo4j) and report databases into MongoDB/Postgres. It involves setup configurations, logging, and insertion operations to manage the collections effectively.

## Usage Instructions

1. **Environment Setup:**
   - Install required Python packages listed in `requirements.txt`.
   - Set up environment variables for database credentials as mentioned in the project's configuration files.
   - Ensure necessary permissions are granted to run scripts and access databases.

2. **Pipeline Execution:**
   - Navigate to the pipeline root directory.
   - Run the main script, e.g., `python pipeline.py`, or follow specific instructions provided with each repository for their respective execution commands.
   - Monitor the output for any errors or warnings during the pipeline's execution.

3. **Version Management:**
   - The pipeline handles versioning automatically by incrementing minor versions and creating/updating the `version.txt` file as needed.
   - Ensure to commit and push changes to your version control system after each successful run to maintain a record of pipeline iterations.

4. **Backup and Recovery:**
   - Dump files generated during pipeline execution are uploaded to Nectar for backup purposes.
   - To recover data, follow the instructions provided in the project's documentation or contact the appropriate support team for assistance.

