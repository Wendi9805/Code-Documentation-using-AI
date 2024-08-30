# f0173: National Graph Insight Data

## Project Summary

This script fetches publication statistics from a Neo4j graph database and stores them into a PostgreSQL table named `cop_stats_published_at`. The data includes graph name, augmentation level, build date, source of publications, publication year, publication month, and the count of distinct publications. It first creates this table if it doesn't exist, then appends new records to it. After appending, it drops any duplicated records based on the combination of graph_name, augmentation_level, source, publication_year, and publication_month. Finally, it adds a primary key for these columns to ensure data consistency.

## Dependencies

- pandas
- csv
- datetime
- time
- logging
- os
- psycopg2.extras
- neo4j
- GraphDatabase
- ServiceUnavailable (neo4j.exceptions)
- psycopg2
- sqlalchemy

## Input

1. **Graph Name** (`graph_name`)
   - Default: `config['DEFAULT']['Graph-Name']`
   - Environment Variable: `NEO4J_GRAPH_NAME`

2. **Augmentation Level** (`aug_lvl`)
   - Default: `config['DEFAULT']['Augmentation-Level']`
   - Environment Variable: `AUG_LEVEL`

3. **Neo4j Link** (`neo4j_link`)
   - Default: `config['DEFAULT']['Neo4j-Link']`
   - Environment Variable: `NEO4J_LINK`

4. **Debug Mode** (`debug`)
   - Default: `config['DEFAULT']['Debug']`
   - Environment Variable: `DEBUG_MODE`

5. **IP Address** (`ip`)
   - Default: `config['DEFAULT']['IP']`
   - Environment Variable: `IP_ADDRESS`

6. **Port Number** (`port`)
   - Default: `config['DEFAULT']['Port']`
   - Environment Variable: `PORT_NUMBER`

7. **Database Name** (`db_name`)
   - Default: `config['DEFAULT']['PostgresDB']`
   - Environment Variable: `POSTGRES_DB_NAME`

8. **Neo4j Username**
   - Default: Environment variable `neo4j_username`
   - Example: `NEO4J_USERNAME`

9. **Neo4j Password**
   - Default: Environment variable `neo4j_password`
   - Example: `NEO4J_PASSWORD`

10. **Postgres Username**
    - Default: Environment variable `pg_username`
    - Example: `PG_USERNAME`

11. **Postgres Password**
    - Default: Environment variable `pg_password`
    - Example: `PG_PASSWORD`

## Output

1. Successfully created `cop_stats_published_at` table.
   - Table schema: CREATE TABLE cop_stats_published_at (
       "graph_name" text,
       "augmentation_level" int,
       "graph_version" text,
       "build_date" date,
       "source" text,
       "publication_year" integer,
       "publication_month" integer,
       "publication_count" bigint
     );

2. Inserted `published_at_df` data to PostgreSQL.
   - New records inserted: 107 rows

3. Append Successful for table `cop_stats_published_at`
   - Records appended successfully

4. After dropping duplicates, there are now 58 unique records.

5. Successfully added PRIMARY KEY (graph_name, augmentation_level, source, publication_year, publication_month) to the cop_stats_published_at table.
   - Primary Key Successful

**Usage Instructions**

1. **Prepare Dataframe:**
   - If `published_at_df` is not empty, fill NaN values in 'publication_year' and 'publication_month' columns with 0.
   - Select relevant columns and drop duplicates based on ['graph_name', 'augmentation_level', 'source', 'publication_year', 'publication_month'].
   - Convert 'publication_year' and 'publication_month' to integer data type.

2. **Create Table (if not exists):**
   - Define SQL query `create_stats_published_at` for creating table `cop_stats_published_at`.
   - Attempt to execute the query using `conn.cursor()`. If successful, commit changes and log creation. If an exception occurs, set `existing_db=True` and log the error.

3. **Insert Data into MongoDB:**
   - Log and print a message indicating insertion of `publishedat_result` into MongoDB.

4. **Append Data to PostgreSQL:**
   - Attempt to append `published_at_df` to the `cop_stats_published_at` table in PostgreSQL using `pd.DataFrame.to_sql()`. If successful, log success.
   - If an exception occurs, log the error.

5. **Update Table with New Records:**
   - Fetch all records from `cop_stats_published_at`, concatenate them with `published_at_df`, convert data types as necessary, remove duplicates, and replace the table's contents using `pd.DataFrame.to_sql()`.
   - If successful, log the number of records after removing duplicates. If an exception occurs, print "Update Failed, Check Log" and log the error.

6. **Add Primary Key:**
   - Attempt to add a primary key (`graph_name`, `augmentation_level`, `source`, `publication_year`, `publication_month`) to `cop_stats_published_at` using `con.execute()`. If successful, commit changes and print success.
   - If an exception occurs, log the error.

7. **Close Connection:**
   - Close the database connection with `conn.close()`.

**Note:** This script assumes that you have already established a connection (`conn`) and created an engine (`engine`) for PostgreSQL. Also, it's recommended to handle exceptions within try-except blocks to prevent unexpected failures.
