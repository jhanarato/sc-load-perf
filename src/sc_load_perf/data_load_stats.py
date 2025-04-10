import polars as pl

def stats() -> pl.DataFrame:
    return pl.read_csv('~/Code/suttacentral/server/load-data-run.csv')
