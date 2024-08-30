# f0284: Create Augmented Postgres from Neo4j

## Project Summary
This project aims to create augmented Postgres tables from Neo4j data. It exports nodes and relations from a Neo4j graph database, processes them into DataFrames using pandas, and inserts them into Postgres tables with appropriate primary keys. The script handles duplicates and null key records during insertion.

## Dependencies

- pandas
- os
- logging
- csv
- json
- re
- neo4j
- psycopg2
- sqlalchemy

## Input

1. **IP** (from `config.ini`)
2. **Port** (from `config.ini`)
3. **PostgresDB** (from `config.ini`)
4. **Neo4j-Link** (from `config.ini`)
5. **Debug** (from `config.ini`)
6. **pg_username** (from environment variables)
7. **pg_password** (from environment variables)
8. **neo4j_username** (from environment variables)
9. **neo4j_password** (from environment variables)

## Output

1. **Nodes Exported and Inserted:**
   - `grant`: Exported and inserted into `augmented_grant` table.
   - `researcher`: Exported and inserted into `augmented_researcher` table.
   - `dataset`: Exported and inserted into `augmented_dataset` table.
   - `organisation`: Exported and inserted into `augmented_organisation` table.
   - `publication`: Exported and inserted into `augmented_publication` table.

2. **Relations Exported and Inserted:**
   - Relations between `grant` and other nodes (e.g., `grant_researcher`, `grant_dataset`, etc.) exported and inserted into respective `augmented_relation_{n_from}_{n_to}` tables.
   - Similarly, relations for other node pairs like `researcher_publication`, `dataset_publication`, `organisation_grant`, etc.

3. **Logs:**
   - Logs generated during the execution, including information about duplicated records, null key records, and any exceptions encountered while inserting data into PostgreSQL tables.
   - Log files saved as `output_log_{timestamp}.txt`.

Here's a step-by-step guide on how to run the given script, adhering strictly to the requested format and conciseness:

## Usage Instructions

1. **Setup**
   - Install necessary packages: `neo4j` for Neo4j interaction, `pandas`, `psycopg2`, and `logging`.
   - Set up a Neo4j driver with an active session.
   - Initialize a Postgres engine using `create_engine()` from `psycopg2`.

2. **Define Node Labels and Relationships**
   - Set `n_from` and `n_to` as the labels for the start and end nodes respectively.

3. **Query Neo4j**
   - Define Cypher query to fetch relationships between nodes with non-null keys.
   - Run the query using `driver.session().run(cypher)` and store results in `result`.

4. **Update Relationships**
   - Update relationship properties (`r.update(r['props'])`) for each result in `result`.
   - Remove 'props' key from each result (`r.pop('props')`).

5. **Data Frame Preparation**
   - Convert `result` into a pandas DataFrame, `df`.

6. **Data Cleaning**
   - Check and log duplicated records by `{n_from}_key,{n_to}_key`.
   - Check and log null key records.
   - Drop duplicates by `{n_from}_key,{n_to}_key`, keeping the last occurrence (`df.drop_duplicates(subset=[f'{n_from}_key',f'{n_to}_key'],keep='last')`).
   - Drop rows with any null keys.

7. **Insert to Postgres**
   - Insert cleaned data into a table named `augmented_relation_{n_from}_{n_to}` in Postgres.
   - Handle exceptions during insertion and log errors if any.

8. **Append Data to Existing Table**
   - Retrieve existing records from the Postgres table using `conn.cursor()`.
   - Concatenate new data with existing records and re-insert into the Postgres table.
   - Add a primary key constraint on `{n_from}_key,{n_to}_key`.

9. **Close Database Connection**
   - Close the database connection with `conn.close()`.

If no relations are found (`len(result) == 0`), the script will simply pass without performing any operations or errors.
