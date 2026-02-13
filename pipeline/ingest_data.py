import pandas as pd
import click
from sqlalchemy import create_engine

url_1 = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
green_taxi_df = pd.read_parquet(url_1)

url_2 = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
taxi_zone_df = pd.read_csv(url_2)

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')

def run(pg_user, pg_pass, pg_port, pg_host, pg_db):
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    green_taxi_df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')
    green_taxi_df.to_sql(name='green_taxi_data', con=engine, if_exists='append')

    taxi_zone_df.head(n=0).to_sql(name='taxi_zone_data', con=engine, if_exists='replace')
    taxi_zone_df.to_sql(name='taxi_zone_data', con=engine, if_exists='append')

if __name__ == '__main__':
    run()



