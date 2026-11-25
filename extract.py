import duckdb
#

duckdb.sql("""
    COPY (
        SELECT *
        FROM read_csv_auto('website.csv')
    )
    TO 'output.parquet'
    (FORMAT PARQUET);
""")

