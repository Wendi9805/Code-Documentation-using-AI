# f0255: National Graph Insight Data

## Project Summary

This project exports and stores data on the most connected nodes in the National Graph Database. It connects to both Neo4j (for graph data retrieval) and PostgreSQL (for storing results), creating a table named `cop_most_connected_nodes`. The exported data includes graph name, augmentation level, graph version, build date, center node details, connected type/source, connection count, and additional node attributes.

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
7. **Postgres Database Name** (`config['DEFAULT']['PostgresDB']`)
8. **Neo4j Username** (Environment Variable: `neo4j_username`)
9. **Neo4j Password** (Environment Variable: `neo4j_password`)
10. **Postgres Username** (Environment Variable: `pg_username`)
11. **Postgres Password** (Environment Variable: `pg_password`)

## Output

1. **Table:** `cop_most_connected_nodes` created and populated in Postgres database.
   - Contains data on most connected nodes from different graphs/levels.
   - Primary Key: `(graph_name, augmentation_level, centre_node_key, connected_type, connected_source)`.

2. **Insertion Log:**
   - Append Successful (initial insertion)
   - Reinsert Successful (after dropping duplicates)

3. **Primary Key Addition:**
   - Successfully added PRIMARY KEY to table `cop_most_connected_nodes`.

## Usage Instructions

This script creates a table and inserts data into a PostgreSQL database using Python's `pandas` and `psycopg2` libraries.

**Steps:**

1. **Database Connection:**
   - Connect to the PostgreSQL database using credentials (db_name, ip, user_name, psword, port).
   - Set autocommit mode on (`conn.set_session(autocommit=True)`).

2. **Table Creation:**
   - Check if `additional_columns_definition` is provided.
   - Construct a SQL query to create the table `cop_most_connected_nodes` with specified columns and additional columns if defined.
   - Attempt to execute this query using a cursor (`with conn.cursor() as curs:`) and commit changes.

3. **Handle Table Creation Exception:**
   - If an error occurs during table creation, set `existing_db=True` and log the error message.

4. **Data Preparation:**
   - Convert `most_conneted` dataframe to SQL format using `to_sql()` function with `'append'` mode (`if_exists='append'`) for existing tables.
   - Handle any exceptions that occur during data insertion and log the error messages if they occur.

5. **Read and Check Duplicates:**
   - Fetch all records from `cop_most_connected_nodes` table ordered by specified columns.
   - Concatenate fetched records with `most_conneted` dataframe (`df = pd.concat([pd.DataFrame(current), most_conneted])`).
   - Check for duplicated records based on specific columns and print the count of duplicates.

6. **Data Cleaning:**
   - Drop duplicate rows based on specified columns (`keep='last'` to keep the latest record if duplicates exist).

7. **Reinsert Data:**
   - Convert data types of `augmentation_level` and `build_date` columns.
   - Re-insert cleaned dataframe into the PostgreSQL table using `'replace'` mode (`if_exists='replace'`) for existing tables.

8. **Handle Insertion Exception:**
   - Log any error messages that occur during insertion.

9. **Create Primary Key:**
   - Connect to the database engine and execute a SQL query to add a primary key to `cop_most_connected_nodes` table.
   - Commit changes if successful, else log the error message.

10. **Close Database Connection:**
    - Close the database connection using `conn.close()`.

**Note:** Make sure to have necessary credentials and appropriate data formats before running this script. Also, ensure that you have installed required libraries (`pandas`, `psycopg2`) and configured them correctly for your environment.
