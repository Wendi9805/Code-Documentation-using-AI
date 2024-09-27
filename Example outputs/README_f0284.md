# f0284: Create Augmented Postgres from Neo4j

## Project Summary

This project aims to create an augmented PostgreSQL database from an existing Neo4j graph database. It exports nodes (including 'grant', 'researcher', 'dataset', 'organisation', and 'publication') and relations between them from Neo4j, processes the data using Pandas in Python, and inserts it into a PostgreSQL database with appropriate primary keys for both node and relation tables. The script handles duplicated records and null key records during processing.

## Dependencies

- pandas
- os
- logging
- csv
- json
- re
- neo4j
- psycopg2
- psycopg2.extras
- sqlalchemy

## Input

1. **IP Address** (`config.ini` under `[DEFAULT]`, default value from config file)
2. **Port Number** (`config.ini` under `[DEFAULT]`, default value from config file)
3. **PostgreSQL Database Name** (`config.ini` under `[DEFAULT]`, default value from config file)
4. **Neo4j Link** (`config.ini` under `[DEFAULT]`, default value from config file)
5. **Debug Mode** (`config.ini` under `[DEFAULT]`, default value from config file)
6. **PostgreSQL Username** (Environment Variable: `pg_username`)
7. **PostgreSQL Password** (Environment Variable: `pg_password`)
8. **Neo4j Username** (Environment Variable: `neo4j_username`)
9. **Neo4j Password** (Environment Variable: `neo4j_password`)

## Output

1. **Nodes Exported and Inserted into Postgres**
   - grant: Exported and inserted nodes: `<exported_nodes_count>`
   - researcher: Exported and inserted nodes: `<exported_nodes_count>`
   - dataset: Exported and inserted nodes: `<exported_nodes_count>`
   - organisation: Exported and inserted nodes: `<exported_nodes_count>`
   - publication: Exported and inserted nodes: `<exported_nodes_count>`

2. **Relationships Exported and Inserted into Postgres**
   - `<relation_name>` (`<from_node>_<to_node>` format): Exported and inserted relations: `<exported_relations_count>`
     - Example: grant_researcher relationship exported and inserted: `<exported_relations_count>`

3. **Log Files**
   - log_file_1: Contains detailed logs of node exports, relation exports, inserts into Postgres, duplicates dropped, etc.
   - log_file_2: Contains error messages encountered during the process.

4. **Database Tables Created/Updated**
   - augmented_<node_name>: Updated or created tables for nodes in Postgres
     - Example: augmented_grant table updated/created

   - augmented_relation_<from_node>_<to_node>: Updated or created tables for relationships in Postgres
     - Example: augmented_relation_grant_researcher table updated/created

## Usage Instructions

1. **Cypher Query & Data Extraction**
   - Define Cypher query to fetch relations between `n_from` and `n_to` nodes.
   - Execute the query using Neo4j driver.
   - Process the results to extract relevant data.

2. **Data Processing**
   - Remove duplicate records.
   - Handle null key records according to your requirements (e.g., fill with default values or exclude).

3. **Database Insertion**
   - Connect to PostgreSQL database using psycopg2.
   - Create tables if they don't exist, following the schema defined in the script.
   - Insert processed data into respective tables.

2. **Error Handling & Logging**
   - Implement error handling for database connectivity issues and other exceptions.
   - Log successful executions, errors, warnings, and debug messages using Python's built-in logging module.
```

This formatted README retains all the information from your original README while adhering to the standard format you provided.