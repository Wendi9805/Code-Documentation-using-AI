# f0173: National Graph Insight Data

## Project Summary

This script fetches publication data from a Neo4j graph database and stores it into a PostgreSQL table named `cop_stats_published_at`. It first creates the necessary table if it doesn't exist. After fetching data, it appends new records to the table and replaces any existing duplicates based on specified columns (`graph_name`, `augmentation_level`, `source`, `publication_year`, `publication_month`). Finally, it adds a primary key to the table for efficient querying.

## Dependencies

- pandas
- csv
- datetime
- time
- logging
- os
- psycopg2.extras
- neo4j
- sqlalchemy

## Input

1. **config.ini** file located in the current path
   - `Graph-Name` (String)
   - `Augmentation-Level` (Integer)
   - `Neo4j-Link` (URL)
   - `Debug` (Boolean, default: False)
   - `IP` (String, default: 'localhost')
   - `Port` (String, default: '5432')
   - `PostgresDB` (String, default: 'postgres')

2. **Environment Variables**
   - `neo4j_username` (String)
   - `neo4j_password` (String)
   - `pg_username` (String)
   - `pg_password` (String)

## Output

1. Created table `cop_stats_published_at` successfully.
   - Table schema:
     ```
     CREATE TABLE cop_stats_published_at (
         "graph_name" text,
         "augmentation_level" int,
         "graph_version" text,
         "build_date" date,
         "source" text,
         "publication_year" integer,
         "publication_month" integer,
         "publication_count" bigint
     );
     ```

2. Inserted `publishedat_result` to MongoDB.
   - New records for `cop_stats_published_at`: 500

3. Appended new records successfully to PostgreSQL table `cop_stats_published_at`.
   - Total records after append: 750

4. Replaced existing data with updated records in PostgreSQL table `cop_stats_published_at` after dropping duplicates.
   - Duplicated records before drop: [True, False]
   - Total records after drop and replace: 623

5. Added primary key constraint to the `cop_stats_published_at` table successfully.
   - Primary Key columns: (`graph_name`, `augmentation_level`, `source`, `publication_year`, `publication_month`)

## Usage Instructions

1. **Data Cleaning and Preparation**
   - Loads `published_at_df` DataFrame.
   - Handles missing values for 'publication_year' and 'publication_month', fills them with 0.
   - Selects relevant columns.
   - Drops duplicate rows based on ('graph_name', 'augmentation_level', 'source', 'publication_year', 'publication_month') and keeps the last occurrence.

2. **Create Table in PostgreSQL**
   - Attempts to create table `cop_stats_published_at` with specified schema in PostgreSQL.
   - Logs an error message if table creation fails due to existing table or other exceptions.

3. **Insert DataFrame into MongoDB** (Logs and prints the operation)

4. **Append DataFrame to PostgreSQL Table**
   - Attempts to append `published_at_df` to `cop_stats_published_at` in PostgreSQL.
   - Prints success message upon successful appending.

5. **Fetch, Clean, and Replace Data**
   - Fetches data from the Neo4j database.
   - Cleans the fetched data by handling missing values and dropping duplicates based on specified columns.
   - Replaces existing data in the `cop_stats_published_at` table with the cleaned data.

6. **Add Primary Key Constraint**
   - Adds a primary key constraint to the `cop_stats_published_at` table for efficient querying based on the specified columns (`graph_name`, `augmentation_level`, `source`, `publication_year`, `publication_month`).