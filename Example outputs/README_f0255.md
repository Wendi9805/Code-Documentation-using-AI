# f0255: National Graph Insight Data: Exporting Most Connected Nodes

## Project Summary

This project focuses on exporting the most connected nodes from a National Graph database. It reads configuration parameters from an environment file and connects to both Neo4j (graph database) and PostgreSQL databases. The script extracts key information about the most connected nodes, ensures data integrity by dropping duplicates, and inserts the processed data into a table named `cop_most_connected_nodes` in the PostgreSQL database with appropriate column types and a composite primary key.

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

1. **Augmentation-Level** (`config['DEFAULT']['Augmentation-Level']`)
2. **Graph-Name** (`config['DEFAULT']['Graph-Name']`)
3. **Neo4j-Link** (`config['DEFAULT']['Neo4j-Link']`)
4. **Debug** (`config['DEFAULT']['Debug']`)
5. **IP** (`config['DEFAULT']['IP']`)
6. **Port** (`config['DEFAULT']['Port']`)
7. **PostgresDB** (`config['DEFAULT']['PostgresDB']`)

8. **neo4j_username** (Environment Variable)
9. **neo4j_password** (Environment Variable)

10. **pg_username** (Environment Variable)
11. **pg_password** (Environment Variable)

## Output

1. `cop_most_connected_nodes` table created in Postgres with columns:
   - "graph_name" (text)
   - "augmentation_level" (int)
   - "graph_version" (text)
   - "build_date" (date)
   - "centre_node_type" (text)
   - "centre_node_key" (text)
   - "connected_type" (text)
   - "connected_source" (text)
   - "conneted_count" (bigint)
   - Additional columns based on data present in the dataset

2. Data inserted into `cop_most_connected_nodes` table:
   - Initial append of records from most_conneted dataframe
   - Reinsertion of cleaned and deduplicated data

3. Primary key added to `cop_most_connected_nodes` table:
   - (graph_name, augmentation_level, centre_node_key, connected_type, connected_source)

## Usage Instructions

1. **Setup:**
   - Install required libraries: `psycopg2`, `pandas`, `sqlalchemy`.
   - Import necessary modules and define variables:
     ```python
     import psycopg2, pandas as pd, logging, sqlalchemy
     from sqlalchemy import create_engine, text

     db_name = "your_database"
     ip = "your_ip"
     user_name = "your_username"
     psword = "your_password"
     port = "your_port"

     additional_columns = [...]  # List of additional columns
     ```

2. **Connect to PostgreSQL:**
   - Create a connection using `psycopg2.connect()`.
   - Set the session to autocommit (`conn.set_session(autocommit=True)`).

3. **Create Table Schema:**
   - Define `additional_columns_definition` based on provided list.
   - Generate SQL CREATE TABLE statement with or without additional columns.
   - Execute the create table query.

4. **Fetch and Process Data:**
   - Fetch data from Neo4j database using Cypher queries.
   - Process the fetched data as per requirements.
   - Store the processed data in a Pandas dataframe named `most_conneted`.

5. **Insert Data into PostgreSQL:**
   - Convert the `most_conneted` dataframe to an SQL insert query.
   - Execute the insert query using the created connection.

6. **Ensure Data Integrity:**
   - Fetch existing records from `cop_most_connected_nodes`.
   - Merge and deduplicate the fetched records with the processed data in `most_conneted`.
   - Insert the final dataset back into `cop_most_connected_nodes`.

7. **Add Primary Key:**
   - Generate an ALTER TABLE query to add a composite primary key.
   - Execute the alter table query using the created connection.

8. **Close Connection:**
   - Close the database connection (`conn.close()`).

---