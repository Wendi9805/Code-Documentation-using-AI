# f0220: Exporting Data from Neo4j into Postgresql Database

## Project Summary

This project involves exporting data from a Neo4j database into a PostgreSQL database. The process includes reading configuration settings, starting logging, and using a MongoDB driver to insert ARC organizations and relationships, as well as ARC grants and their corresponding funding objectives. Additional CSV files such as `partners_orgs_without_admin_org.csv`, `grant_for.csv`, `grant_for_after_2013.csv`, and `socio_economic_objective.csv` are also inserted, followed by a summary in the `grant_summary.csv` file.

## Dependencies

- pandas
- os
- logging
- csv
- json
- collections
- nltk
- re
- pymongo
- gensim
- psycopg2
- sqlalchemy

## Input

1. **Input1** (`ip` - PostgreSQL Server IP Address)
2. **Input2** (`port` - PostgreSQL Server Port)
3. **Input3** (`user_name` - PostgreSQL Username)
4. **Input4** (`psword` - PostgreSQL Password)
5. **Input5** (`db_name` - PostgreSQL Database Name)
6. **Input6** (`input_path` - Path to Input Files)
7. **Input7** (`ip_in` - MongoDB Server IP Address (Input))
8. **Input8** (`port_in` - MongoDB Server Port (Input))
9. **Input9** (`user_name_in` - MongoDB Username (Input))
10. **Input10** (`psword_in` - MongoDB Password (Input))
11. **Input11** (`db_name_in` - MongoDB Database Name (Input))
12. **Input12** (`collection_in` - MongoDB Collection Name (Input))
13. **Input13** (`debug` - Debug Mode (True/False))

## Output

1. `grant_for_seo_df.to_sql("grant_seo", engine, if_exists='replace', index=False)`
2. `counter_obj = count_frequency(tmp_df)`
3. `tmp_df['cleaned_summary'] = tmp_df['grant-summary'].apply(lambda x: cleaning_text(x, counter_obj.most_common(n=100)))`
4. `tmp_df['keywords_by_gensim'] = tmp_df['cleaned_summary'].apply(lambda x: keywords(x))`
5. `tmp_df['keywords_by_gensim'] = tmp_df['keywords_by_gensim'].apply(lambda x: x.replace('\n', ' '))`
6. `summary_df = pd.DataFrame()`
7. For each row in `tmp_df`:
   - `keywords = str(r['keywords_by_gensim'])`
   - For each keyword `k` in `keywords.split(' ')`, append {"arc_grant_key": r['arc_grant_key'], "keywords_by_gensim": k} to `summary_df`
8. `summary_df.loc[:,'_id'] = summary_df['arc_grant_key'] + summary_df['keywords_by_gensim']`
9. `summary_df.to_sql("grant_summary", engine, if_exists='replace', index=False)`

## Usage Instructions

1. **Usage Instruction1: Check Database Name**
   - The script first checks if the `db_name` is 'nl0000'.
   
2. **Usage Instruction2: Extract Socio-Economic Objectives**
   - If true, it iterates through each row in `grants_for_seo_df`.
   - For each row, extract socio-economic objectives from the input CSV files.

3. **Usage Instruction3: Insert Data into MongoDB**
   - Use pymongo to insert ARC organizations and relationships into the specified MongoDB collection.
   
4. **Usage Instruction4: Handle Debug Mode**
   - If `debug` is True, enable detailed logging and error handling for easier debugging.
```

This version maintains all the necessary information from your original README while adhering to the standard format you provided. Adjustments were made to align with the structure expected in a typical README file.