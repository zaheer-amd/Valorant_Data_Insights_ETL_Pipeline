import duckdb

# This is the magic of DuckDB. We can write standard SQL and use 
# the 'read_json_auto' function to treat a local file like a database table!

sql_query = """
    SELECT * FROM read_json_auto('zjson_files/single_match_data_fnatic_vs_ef.json')
"""

# Execute the query and display the results in the console
duckdb.sql(sql_query).show()