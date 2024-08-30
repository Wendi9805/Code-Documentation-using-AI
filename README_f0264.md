# f0264: National Graph Insight Data

## Exporting Organisation Locations

## Project Summary

This project aims to export organisation locations from a National Graph database and store them in a PostgreSQL database. It uses Neo4j for graph operations and pandas for data manipulation. The process involves retrieving organisation country and city information, filtering duplicates, and inserting the resulting DataFrame into the PostgreSQL table 'cop_organisation_locations'. The script also ensures that the table has a composite primary key consisting of ('graph_name', 'augmentation_level', 'country', 'city').

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

1. **config.ini** file located in the project root directory
   - `Augmentation-Level` (string)
   - `Neo4j-Link` (string)
   - `Graph-Name` (string)
   - `Debug` (boolean, default: False)
   - `IP` (string)
   - `Port` (integer)
   - `PostgresDB` (string)

2. **Environment Variables**
   - `neo4j_username` (string)
   - `neo4j_password` (string)
   - `pg_username` (string)
   - `pg_password` (string)

## Output

1. Table `cop_organisation_locations` created in PostgreSQL database.
   - Columns: `"graph_name" text`, `"augmentation_level" int`, `"graph_version" text`, `"build_date" date`, `"country" text`, `"city" text`, `"organisations" bigint`, `"connected_researchers" bigint`.
2. DataFrame `org_df` appended to table `cop_organisation_locations` in PostgreSQL database.
   - New records:  Length of `org_df`
3. Table `cop_organisation_locations` updated with deduplicated records based on keys `('graph_name', 'augmentation_level', 'country', 'city')`.
4. Primary key added to table `cop_organisation_locations`: `(graph_name, augmentation_level, country, city)`.

## Usage Instructions

1. **Environment Setup:**
   - Set up a PostgreSQL database.
   - Create and configure a Neo4j database.
   - Set the required environment variables: `neo4j_username`, `neo4j_password`, `pg_username`, `pg_password`.
   - Create a `config.ini` file in the same directory as the script with the following sections:
     ```
     [DEFAULT]
     Augmentation-Level = <aug_level>
     Neo4j-Link = <neo4j_link>
     Graph-Name = <graph_name>
     Debug = True/False
     IP = <ip_address>
     Port = <port_number>
     PostgresDB = <postgres_db_name>
     ```

2. **Running the Script:**
   - Install required packages: `pandas`, `pyneo4j`, `psycopg2`, `sqlalchemy`.
   - Run the script. It will:
     a. Read configuration files and environment variables.
     b. Connect to Neo4j and PostgreSQL databases.
     c. Create a new database (if not exists) in PostgreSQL for storing results.
     d. Fetch graph version and date from Neo4j.
     e. Query and process organization data from Neo4j.
     f. Convert the retrieved data into a pandas DataFrame.
     g. Fill NA values, drop duplicates, and convert column types as needed.
     h. Create table `cop_organisation_locations` in PostgreSQL (if not exists).
     i. Insert or replace data into the `cop_organisation_locations` table.

3. **Logging:**
   - If `Debug = True` in `config.ini`, it will log info messages to a `debug.log` file in the script's directory.
