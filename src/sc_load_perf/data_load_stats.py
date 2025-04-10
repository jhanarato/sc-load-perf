import polars as pl

def stats() -> pl.DataFrame:
    df = pl.read_csv(
        source='~/Code/suttacentral/server/load-data-run.csv',
        new_columns=['number', 'message', 'clock_time_s', 'cpu_time_s']
    )
    return df.filter(pl.col('message') != 'All done')