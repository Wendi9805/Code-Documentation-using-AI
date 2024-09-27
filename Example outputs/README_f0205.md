# f0205: Insert Graph and PBI Collections Versions to MongoDB/Postgres

## Project Summary
This project focuses on retrieving and storing versions of Graph DB (Neo4j) and report databases into MongoDB/Postgres. It involves setup configurations, logging, and insertion operations to manage the collections effectively.

## Dependencies
- pandas
- datetime
- sys
- os
- string
- re
- logging
- numpy
- pymongo
- neo4j
- csv
- psycopg2
- sqlalchemy

## Input

1. **IP** (`str`): The IP address to connect to.
   - Default: `config['DEFAULT']['IP']`

2. **Port** (`int`): The port number to use for the connection.
   - Default: `config['DEFAULT']['Port']`

3. **DB Name** (`str`): The name of the database.
   - Default: `config['DEFAULT']['DB']`

4. **DB Type** (`str`): The type of the database (default is 'mongodb').
   - Default: `config.get('DEFAULT', 'DB-Type', fallback='mongodb')`

5. **Collection** (`str`): The collection name for MongoDB.
   - Default: `config['DEFAULT']['Collection']`

6. **Input Path** (`str`): The path to the input data file(s).
   - Default: `config['DEFAULT']['Input-Path']`

7. **Neo4j URI** (`str`): The connection URI for Neo4j.
   - Default: `config['DEFAULT']['Neo4j-Link']`

8. **Debug Mode** (`bool`): Whether to run the script in debug mode.
   - Default: `config.getboolean('DEFAULT', 'Debug')`

9. **Environment Variables**:
   - **neo4j_username**: Username for Neo4j connection (if not using URI).
     - Default: `os.environ.get("neo4j_username")`
   - **neo4j_password**: Password for Neo4j connection (if not using URI).
     - Default: `os.environ.get("neo4j_password")`
   - **pg_username**: Username for PostgreSQL connection.
     - Default: `os.environ.get("pg_username")`
   - **pg_password**: Password for PostgreSQL connection.
     - Default: `os.environ.get("pg_password")`

## Output

1. **Version Data Dictionary:**
   ```
   {'version': 'report_version', 'build_date': 'current_date'}
   ```

2. **MongoDB Operation:**
   - If `db_type` is 'mongodb':
     - Deletes existing documents in the collection.
     - Inserts the version data dictionary into the specified MongoDB collection.

3. **PostgreSQL Operation:**
   - If `db_type` is 'postgres':
     - Connects to the PostgreSQL database using provided credentials.
     - Creates a pandas DataFrame with the version data.
     - Writes the DataFrame to the "cop_meta" table in the specified PostgreSQL database (if_exists='replace').

4. **Log Files:**
   - If `debug` is set to True:
     - A debug log file named 'debug.log' will be created in the current_path directory with logs formatted as '%(asctime)s | %(levelname)s | %(message)s'.

## Usage Instructions

1. **Ensure Environment Variables are Set**: Make sure the following environment variables are set:
   - `neo4j_username` and `neo4j_password`: Usernames and passwords for Neo4j connection.
   - `pg_username` and `pg_password`: Usernames and passwords for PostgreSQL connection.

2. **Configure `config.ini`**: Update the necessary fields in the `config.ini` file to reflect your desired inputs, such as IP address, port number, database name, collection name, input path, Neo4j URI, etc.

3. **Run the Script**:
   - Navigate to the directory containing your script.
   - Execute the script with optional `-d` flag for debug mode:
     ```
     python script_name.py [-d]
     ```

4. **Monitor Logs**: If the `-d` flag is used, monitor the `debug.log` file in the current_path directory for relevant information about the script's execution.

---