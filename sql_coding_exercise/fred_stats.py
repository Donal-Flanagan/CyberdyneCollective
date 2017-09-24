# -*- coding: utf-8 -*-

"""
Retrieve statistics from the FRED api

Usage:
    fred_stats.py --user=USER --password=PASSWORD [--start=START] [--end=END] [--host=HOST] [--api_key=API_KEY] [--database=DATABASE] [--port=PORT]
    fred_stats.py (-h | --help)
    fred_stats.py (-v | --version)

Options:
    -u --user=USER              Your Postgres username.
    -p --password=PASSWORD      Your Postgres password.
    -h --help                   Show this screen.
    -v --version                Show version.

Additional options:
    -s --start=START            yyyy-mm-dd. Start date for average unemployment rate aggregation.
                                Default = 1980-01-01
    -e --end=END                yyyy-mm-dd. End date for average unemployment rate aggregation.
                                Default = 2015-12-31
    --host=HOST                 Database hostname.
                                Default = 'localhost'.
    -a --api_key=API_KEY        Your FRED api key.
                                Default = Fred API key of Dónal Flanagan.
    -d --database=DATABASE      The name of the database in which you wish to store the Fred data.
                                If the database does not exist it will be created.
                                Default = 'fred_db'.
    --port=PORT                 The Postgres port.
                                Default = 5432
"""

# fixme: Is it best practice to separate the imports into
import sys
import logging
import requests
import pandas as pd
from fredapi import Fred
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
from docopt import docopt


logger = logging.getLogger('fred_stats')
__version__ = '0.0.1'


def get_db_engine(db_name, user, password, host, port=5432):

    db_connection = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        database=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )

    engine = create_engine(db_connection)
    if not database_exists(engine.url):
        try:
            create_database(engine.url)

        except Exception as exc:
            logger.exception('Could not create database. \nException: %r', exc)
            return exc
    return engine


def main():
    args = docopt(__doc__, version='fki-missing-answers %s' % __version__)

    user = args.get('--user')
    password = args.get('--password')
    host = args.get('--host') if args.get('--host') else 'localhost'
    api_key = args.get('--api_key') if args.get('--api_key') else '01af77900eb060649a7c504ee0705b4d'
    db_name = args.get('--database') if args.get('--database') else 'fred_db'
    port = int(args.get('--port')) if args.get('--port') else 5432
    start_date = args.get('--start') if args.get('--start') else '1980-01-01'
    end_date = args.get('--end') if args.get('--end') else '2015-12-31'

    # Instantiate the sqlalchemy database interface #fixme: is 'interface' the correct word?
    engine = get_db_engine(db_name, user, password, host, port)

    try:
        logging.basicConfig(level=logging.DEBUG)
        logger.info('starting fred_stats')

        # Retrieve the data from the FRED api
        fred = Fred(api_key=api_key)
        gdp = fred.get_series('GDPC1').rename('gdp')
        um_cust_sent_index = fred.get_series('UMCSENT').rename('umcsent')
        us_civ_unemploy_rate = fred.get_series('UNRATE').rename('unrate')

        frames = [gdp, um_cust_sent_index, us_civ_unemploy_rate]
        fred_data = pd.concat(frames, axis=1)

        # Insert the data into an SQL table
        # fixme: add option to replace or append here depending on intitial or incremental load type
        fred_data.to_sql(name='fred_data', con=engine, if_exists='replace', index=True, index_label='timestamp')

        # '1980-01-01'
        # '2015-12-31'
        print('start_date:',start_date)
        print('type:', type(start_date))

        # Aggregate the average unemployment rate per year
        unemployment_query = """
            SELECT EXTRACT(YEAR from timestamp)::INT as year, avg(unrate)
            FROM fred_data
            where timestamp >= :start_date and timestamp <= :end_date
            GROUP BY year
            ORDER BY year
        """.format(start_date=start_date, end_date=end_date)

        result = engine.execute(unemployment_query, {'mv': start_date, 'ml': end_date})

        df = pd.DataFrame(result.fetchall())
        df.columns = result.keys()
        df.set_index('year', inplace=True)

        print('The average rate of unemployment in the USA for each year between 1980 and 2015 is as follows:')
        print(df)

    except KeyboardInterrupt:
        logger.info('Stopping fred_stats')
    except Exception as exc:
        logger.exception('Got exception %r', exc)
        return exc

if __name__ == '__main__':
    sys.exit(main())
