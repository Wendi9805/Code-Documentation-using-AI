# f0223: Inserting Admin Organisations into Postgresql Database

## Project Summary

This notebook focuses on inserting admin organisations into a PostgreSQL database. It includes steps for reading configuration settings, starting logging, and executing insertions for admin organisations, classifications, and FoR (Field of Research) data, with an additional step for inserting FoR 2020 data.

## Dependencies

- pandas
- os
- logging
- csv
- json
- psycopg2
- sqlalchemy

## Input

1. **Path to `config.ini` file** (`config['DEFAULT']['CONFIG_FILE_PATH']`)
2. IP address for database connection (`config['DATABASE']['DB_HOST']`)
3. Port number for database connection (`config['DATABASE']['DB_PORT']`)
4. PostgreSQL username (`config['DATABASE']['DB_USER']`)
5. PostgreSQL password (`config['DATABASE']['DB_PASSWORD']`)
6. Name of the PostgreSQL database (`config['DEFAULT']['DB_NAME']`)
7. Path for input files (`config['DEFAULT']['INPUT_FILES_PATH']`)
8. Debug mode (True or False) (`config['DEFAULT']['DEBUG']`)

## Output

1. `admin_organisations` table saved to Postgres database
2. `classification` table saved to Postgres database (if `db_name` is 'nl0004_7')
3. `for_2008` table saved to Postgres database (if `db_name` is 'abs')
4. `for_2020` table saved to Postgres database (if `db_name` is 'abs')
5. Combined `for_graph` table saved to Postgres database (if `db_name` is 'abs')

## Usage Instructions

1. **Set Up Configuration**: Ensure the `config.ini` file is properly configured with necessary details such as database credentials and input paths.
2. **Run Script**: Execute the script in a Python environment where Pandas, SQLAlchemy, psycopg2, and other required libraries are installed.
3. **Database Creation**: The script will connect to a PostgreSQL server using the provided credentials and create a new database named as specified in `config.ini`.
4. **Admin Organisations Import**: Read `admin_organisations.csv` and insert data into the PostgreSQL database under the table `admin_organisations`. This step is conditionally executed based on the database name.
5. **Classification Table Import**: If the database name matches certain conditions, read an Excel file named `Classification.xlsx`, process it, and import into a PostgreSQL table called `classification`.
6. **FOR 2008 Data Processing**: Read `FOR_graph.xlsx` for the year 2008, process column names and values, then insert this data into the PostgreSQL table `for_2008`.
7. **FOR 2020 Data Processing**: Similarly, read the same file but for the year 2020, process columns, and insert the data into the PostgreSQL table `for_2020`.
8. **Combine DataFrames**: Append the processed `for_2008` and `for_2020` DataFrames to create a combined DataFrame named `for_graph`, then import this combined table into PostgreSQL.
9. **Logging**: Throughout the process, detailed logs are generated for debugging purposes if the `debug` flag is set in `config.ini`. Logs will be stored in a file named `debug.log`.

Ensure all paths and configurations match your environment to avoid issues during execution.
```

This format maintains the essential information while adhering to the specified structure.