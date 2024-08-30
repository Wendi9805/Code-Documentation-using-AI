# f0263: National Graph Insight Data

## Project Summary

This project exports PID coverage per node type from a National Graph Insight data source. It connects to both Neo4j and PostgreSQL databases, retrieves node counts by type, and tracks PID (Persistent Identifier) data for different node types. The processed data is then inserted into a PostgreSQL table named 'cop_pids_coverage_by_type'.

## Dependencies

- pandas
- csv
- datetime
- time
- logging
- os
- neo4j
- psycopg2
- sqlalchemy

## Input

1. **Augmentation Level** (`config['DEFAULT']['Augmentation-Level']`)
2. **Graph Name** (`config['DEFAULT']['Graph-Name']`)
3. **Neo4j Link** (`config['DEFAULT']['Neo4j-Link']`)
4. **Debug Mode** (`config['DEFAULT']['Debug']`)
5. **IP Address** (`config['DEFAULT']['IP']`)
6. **Port Number** (`config['DEFAULT']['Port']`)
7. **PostgresDB Name** (`config['DEFAULT']['PostgresDB']`)
8. **Neo4j Username** (`neo4j_username`, from environment variables)
9. **Neo4j Password** (`neo4j_password`, from environment variables)
10. **Postgres Username** (`pg_username`, from environment variables)
11. **Postgres Password** (`pg_password`, from environment variables)

## Output

1. `cop_pids_coverage_by_type` table created and populated in PostgreSQL database with the following columns:
   - "graph_name" (text)
   - "augmentation_level" (int)
   - "graph_version" (text)
   - "build_date" (date)
   - "type" (text)
   - "total_count_by_type" (bigint)
   - "pid" (text)
   - "source" (text)
   - "count" (bigint)

2. Dataframe `pids_df` saved as CSV file: `pids_coverage.csv`

3. Log file created at `{}/debug.log`. The log contains information about the script's execution, including any errors that occurred during database operations.

4. Primary key added to `cop_pids_coverage_by_type` table on successful completion of the script:
   - Primary Key: (graph_name, augmentation_level, type, pid, source)

## Usage Instructions

1. **Set Up Environment Variables**
   Set the following environment variables:
   - `neo4j_username`: Neo4j username.
   - `neo4j_password`: Neo4j password.
   - `pg_username`: PostgreSQL username.
   - `pg_password`: PostgreSQL password.

2. **Configure config.ini File**
   Ensure a `config.ini` file is present in the same directory as the script, containing the following sections:
   - `[DEFAULT]` with keys: `augmentation_level`, `graph_version`, `build_date`.

3. **Run the Script**
   Execute the Python script. It performs the following steps:

   - Connects to Neo4j and PostgreSQL databases.
   - Retrieves data from Neo4j based on the configured augmentation level.
   - Processes and aggregates data, dropping duplicates if any.
   - Creates a table `cop_pids_coverage_by_type` in PostgreSQL (if it doesn't exist).
   - Inserts processed data into the created table.
   - Sets a primary key for the table.

4. **Monitor Progress**
   The script prints status messages and logs errors to monitor its progress.
