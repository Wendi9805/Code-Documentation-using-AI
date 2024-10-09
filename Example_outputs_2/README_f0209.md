# f0209: NL0014 Database Result Summary

## Project Summary

This notebook aims to summarize database results from a specific feature set. It includes setups such as defining the current path, reading configuration files, and starting logging. The MongoDB driver is utilized to read input from `grants_all` and `grants_for_all` collections.

## Dependencies

- pandas
- logging
- os
- pymongo
- MongoClient

## Input

1. **Input1** (`config['DEFAULT']['CONFIG_FILE_PATH']`)
2. **Input2** (IP address for the database)
3. **Input3** (Port number for the database)
4. **Input4** (MongoDB username)
5. **Input5** (MongoDB password)
6. **Input6** (Database name)
7. **Input7** (`config['DEFAULT']['OUTPUT_PATH']`)
8. **Input8** (`Debug mode` - `True/False`)

## Output

1. `nl0014_grants_result.csv` saved to the specified output path defined in `config.ini`.

## Usage Instructions

1. Ensure you have Python installed on your system.
2. Install the required packages: `pandas`, `configparser`, and `pymongo`. You can install them using pip:
   ```bash
   pip install pandas pymongo configparser
   ```
3. Place the provided script in a `.py` file, for example, `process_grants.py`.
4. Create a `config.ini` file in the same directory as your script with the necessary configuration settings (IP, Port, Username, Password, DB, Output-Path).
5. Run the script using Python:
   ```bash
   python process_grants.py
   ```
6. The script will log any debug information to a `debug.log` file if the `Debug` setting in your config.ini is set to `True`.
7. After execution, the processed data will be saved as `nl0014_grants_result.csv` in the specified output path from your configuration.
```

This format should match the standard you provided while retaining all the necessary information.