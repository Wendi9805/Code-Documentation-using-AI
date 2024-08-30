# Database Dump and Backup Pipeline**

## **Summary**
This Jenkins pipeline automates the process of incrementing the database version, dumping the PostgreSQL database, converting a Jupyter notebook to Python script for Neo4j processing, running the Neo4j process, and uploading the dumped data as a backup to Nectar using Swift. The pipeline also ensures that Neo4j is shut down properly after use.

## Code Repositories Included

- f0284: Create Augmented Postgres from Neo4j
  This project aims to create augmented Postgres tables from Neo4j data. It exports nodes and relations from a Neo4j graph database, processes them into DataFrames using pandas, and inserts them into Postgres tables with appropriate primary keys. The script handles duplicates and null key records during insertion.

- f0173: National Graph Insight Data
  This script fetches publication statistics from a Neo4j graph database and stores them into a PostgreSQL table named `cop_stats_published_at`. The data includes graph name, augmentation level, build date, source of publications, publication year, publication month, and the count of distinct publications. It first creates this table if it doesn't exist, then appends new records to it. After appending, it drops any duplicated records based on the combination of graph_name, augmentation_level, source, publication_year, and publication_month. Finally, it adds a primary key for these columns to ensure data consistency.

- f0255: National Graph Insight Data
  This project exports and stores data on the most connected nodes in the National Graph Database. It connects to both Neo4j (for graph data retrieval) and PostgreSQL (for storing results), creating a table named `cop_most_connected_nodes`. The exported data includes graph name, augmentation level, graph version, build date, center node details, connected type/source, connection count, and additional node attributes.

- f0263: National Graph Insight Data
  This project exports PID coverage per node type from a National Graph Insight data source. It connects to both Neo4j and PostgreSQL databases, retrieves node counts by type, and tracks PID (Persistent Identifier) data for different node types. The processed data is then inserted into a PostgreSQL table named 'cop_pids_coverage_by_type'.

- f0264: National Graph Insight Data
  This project aims to export organisation locations from a National Graph database and store them in a PostgreSQL database. It uses Neo4j for graph operations and pandas for data manipulation. The process involves retrieving organisation country and city information, filtering duplicates, and inserting the resulting DataFrame into the PostgreSQL table 'cop_organisation_locations'. The script also ensures that the table has a composite primary key consisting of ('graph_name', 'augmentation_level', 'country', 'city').

## **Usage Instructions**

1. **Set up Jenkins environment:**
   - Install and configure Jenkins on your server.
   - Ensure you have installed necessary plugins like 'Pipeline', 'Git', and 'Publish Plugins' (if not already installed).
   - Configure credentials for GitHub, Neo4j, and PostgreSQL in Jenkins' credentials manager.

2. **Configure the pipeline job:**
   - Create a new pipeline job in Jenkins.
   - Set the pipeline definition to 'Pipeline script from SCM'.
   - In 'SCM', choose 'Git' and enter your repository URL (e.g., `https://github.com/yourusername/database-dump-pipeline.git`).
   - In ' Branches to build', specify the branch you want to build (e.g., `main` or `develop`).
   - Set 'Additional Behaviours' to 'Checkout behaviour: Checkout submodule(s) as needed'.
   - Save and run your job.

3. **Configure pipeline parameters:**
   - In the pipeline configuration, define parameters for:
     - `db_name`: The name of the database.
     - `neo4j_username` & `neo4j_password`: Neo4j credentials.
     - `pg_username` & `pg_password`: PostgreSQL credentials.
     - `graph_name`: Name of the Neo4j graph.

4. **Monitor and manage jobs:**
   - Monitor the pipeline runs in Jenkins' dashboard.
   - Manage build triggers (e.g., periodic schedule, GitHub webhook) as needed.

5. **Verify backup on Nectar:**
   - After successful completion of the 'Upload to Nectar for Backup' stage, verify that the dumped database file (`${db_name}_version_$current_version.dump`) has been uploaded to the `powerbi-insights/${db_name}` container on Nectar.



