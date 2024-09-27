# f0264: National Graph Insight Data

## Project Summary

This project focuses on exporting organization locations from a National Graph dataset. It reads configuration data from a config.ini file and connects to both Neo4j graph database and PostgreSQL using environment variables for credentials. The process involves fetching organization countries and cities, creating a DataFrame with relevant information, and inserting this data into a PostgreSQL table named 'cop_organisation_locations'. The script also handles duplicate records and sets a primary key on the inserted table.

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

## Inputs

1. **Augmentation Level** (`config['DEFAULT']['Augmentation-Level']`)
2. **Neo4j Link** (`config['DEFAULT']['Neo4j-Link']`)
3. **Graph Name** (`config['DEFAULT']['Graph-Name']`)
4. **Debug Mode** (`config['DEFAULT']['Debug']`)
5. **IP Address** (`config['DEFAULT']['IP']`)
6. **Port** (`config['DEFAULT']['Port']`)
7. **Postgres Database Name** (`config['DEFAULT']['PostgresDB']`)
8. **Neo4j Username** (Environment Variable: `neo4j_username`)
9. **Neo4j Password** (Environment Variable: `neo4j_password`)
10. **PostgreSQL Username** (Environment Variable: `pg_username`)
11. **PostgreSQL Password** (Environment Variable: `pg_password`)

## Outputs

1. `cop_organisation_locations` table created in PostgreSQL with the following columns:
   - "graph_name" (text)
   - "augmentation_level" (int)
   - "graph_version" (text)
   - "build_date" (date)
   - "country" (text)
   - "city" (text)
   - "organisations" (bigint)
   - "connected_researchers" (bigint)

2. `org_df` DataFrame appended to the `cop_organisation_locations` table in PostgreSQL, with a total of **{length_of>org_df}** new records inserted.

3. Duplicated records checked and removed from the `cop_organisation_locations` table in PostgreSQL. Total unique records after deduplication: **{len(df)}**.

4. Primary key (`(graph_name, augmentation_level, country, city)`) added to the `cop_organisation_locations` table in PostgreSQL.

5. Debug log file `{}/debug.log`.format(current_path) created with logging level set to INFO if debug mode is enabled.

## Usage Instructions

1. **Environment Setup**: Set the following environment variables for Neo4j and PostgreSQL credentials:
   - `neo4j_username`
   - `neo4j_password`
   - `pg_username` (PostgreSQL)
   - `pg_password` (PostgreSQL)

2. **Configure config.ini** with the following format:

```
[DEFAULT]
Augmentation-Level = <level>
Neo4j-Link = <neo4j_link>
Graph-Name = <graph_name>
Debug = True/False
IP = <ip>
Port = <port>
PostgresDB = <db_name>
```

3. **Run Script**:
   - Ensure `config.ini` is present in the same directory.
   - Run the script and follow the on-screen instructions.

4. **View Results**: After successful execution, check your PostgreSQL database for the updated 'cop_organisation_locations' table. If debug mode was enabled, check `{}/debug.log`.format(current_path) for detailed logs.
```