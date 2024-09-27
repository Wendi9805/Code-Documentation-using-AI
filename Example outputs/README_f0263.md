# f0263: National Graph Insight Data: Exporting PID Coverage Per Node Type

## Project Summary

This project exports PID coverage per node type from the National Graph Insight Data. It connects to Neo4j and PostgreSQL databases, retrieves data on nodes' connection counts and PID types, processes it into a dataframe, and inserts it into the PostgreSQL table `cop_pids_coverage_by_type`. The script creates this table if it doesn't exist.

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

1. **Augmentation Level** (`augmentation_level`)
   - Type: String
   - Default: `config['DEFAULT']['Augmentation-Level']`

2. **Graph Name** (`graph_name`)
   - Type: String
   - Default: `config['DEFAULT']['Graph-Name']`

3. **Neo4j Link** (`neo4j_link`)
   - Type: String
   - Default: `config['DEFAULT']['Neo4j-Link']`

4. **Debug Mode** (`debug_mode`)
   - Type: Boolean (True/False)
   - Default: `config['DEFAULT']['Debug']`

5. **IP Address**
   - Type: String
   - Default: `config['DEFAULT']['IP']` or Environment Variable `neo4j_ip`

6. **Port Number**
   - Type: Integer
   - Default: `config['DEFAULT']['Port']` or Environment Variable `neo4j_port`

7. **PostgreSQL Database Name** (`postgres_db`)
   - Type: String
   - Default: `config['DEFAULT']['PostgresDB']`

8. **Neo4j Username**
   - Type: String
   - Default: Environment Variable `neo4j_username`

9. **Neo4j Password**
   - Type: String (sensitive)
   - Default: Environment Variable `neo4j_password`

10. **PostgreSQL Username**
    - Type: String
    - Default: Environment Variable `pg_username`

11. **PostgreSQL Password** (`psword`)
    - Type: String (sensitive)
    - Default: Environment Variable `pg_password`

## Output

- PostgreSQL Table: `cop_pids_coverage_by_type` created and updated with the following columns:
  - graph_name (text)
  - augmentation_level (int)
  - graph_version (text)
  - build_date (date)
  - type (text)
  - total_count_by_type (bigint)
  - pid (text)
  - source (text)
  - count (bigint)

- DataFrame `pids_df` saved to PostgreSQL table:
  - New records inserted: <Number of new records>
  - Duplicated records removed before reinsertion
  - Primary key added for columns: graph_name, augmentation_level, type, pid, source

## Usage Instructions

1. **Environment Setup:**
   Ensure the following environment variables are set:
   - `neo4j_username` & `neo4j_password`: Neo4j authentication credentials.
   - `pg_username` & `pg_password`: PostgreSQL authentication credentials.
   - `IP`, `Port`, `postgres_db`: PostgreSQL connection details.

2. **Configuration File:**
   Create a `config.ini` file in the same directory as this script with the following structure:
   ```
   [DEFAULT]
   augmentation_level = <your_augmentation_level>
   ```

3. **Run the Script:**
   Execute the Python script. It performs the following steps:
   - Reads configuration and environment variables.
   - Connects to Neo4j and PostgreSQL databases.
   - Retrieves data from Neo4j and processes it (drops duplicates, converts types).
   - Inserts data into the PostgreSQL table `cop_pids_coverage_by_type`.

4. **Monitoring:**
   Monitor the script's progress using logging statements and check the output table for successful insertions.

5. **Error Handling:**
   Ensure proper error handling is in place to manage any potential issues during database connections or data processing stages.