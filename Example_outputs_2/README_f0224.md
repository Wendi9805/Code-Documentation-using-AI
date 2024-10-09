# f0242: Inserting ABR Organisations into PostgreSQL Database

## Project Summary

This project involves inserting ABR organisations into a PostgreSQL database. The process begins by reading configuration settings and initiating logging. The notebook then uses a PostgreSQL driver to insert data into the `admin_organisations` table.

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
2. IP address for database connection (`config['DATABASE']['DB_IP_ADDRESS']`)
3. Port number for database connection (`config['DATABASE']['DB_PORT_NUMBER']`)
4. PostgreSQL username (`config['DATABASE']['DB_USERNAME']`)
5. PostgreSQL password (`config['DATABASE']['DB_PASSWORD']`)
6. Name of the PostgreSQL database (`config['DEFAULT']['DB_NAME']`)
7. Debug mode (True or False) (`config['DEFAULT']['DEBUG_MODE']`)

## Output

1. The configuration details are read from `config.ini` and used to connect to the PostgreSQL database.
2. A new database is created based on the value of `db_name`, unless it already exists.
3. Data from `input_rel` is loaded into a DataFrame and saved to the PostgreSQL table `relation_arc_to_abr`.
4. Data from `input_node` is loaded into a DataFrame and saved to the PostgreSQL table `node_abr_organisations`.

## Usage Instructions

1. **Set Up Configuration**: Ensure that a `config.ini` file exists in the same directory as your script, with relevant settings like database IP, port, username, password, and database name.

2. **Prepare Input Files**: Prepare two CSV files named according to the variables `input_rel` and `input_node` defined in your configuration file. These files should be separated by a pipe (`|`) character.

3. **Run the Script**: Execute the script. It will:
   - Connect to a PostgreSQL database using credentials from the config file.
   - Create a new database named as specified, unless it already exists.
   - Read and process CSV input files, dropping unnecessary columns.
   - Insert data into two tables (`relation_arc_to_abr` and `node_abr_organisations`) within the PostgreSQL database if certain conditions are met.

4. **Check Logs**: If debugging is enabled (configurable in `config.ini`), logs will be generated detailing actions taken during execution, including any errors that occur.