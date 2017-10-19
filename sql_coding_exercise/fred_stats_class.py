# -*- coding: utf-8 -*-

"""
Retrieve statistics from the FRED api

Usage:
    fred_stats.py --user=USER --password=PASSWORD [--start=START]
                  [--end=END] [--database=DATABASE] [--table=TABLE]
                  [--host=HOST] [--api_key=API_KEY] [--port=PORT]
    fred_stats.py (-h | --help)
    fred_stats.py (-v | --version)

Options:
    -u --user=USER              Your Postgres username.
    -p --password=PASSWORD      Your Postgres password.
    -h --help                   Show this screen.
    -v --version                Show version.

Additional options:
    -s --start=START            yyyy. Start year for average unemployment rate aggregation.
                                Default = 1980
    -e --end=END                yyyy. End year for average unemployment rate aggregation.
                                Default = 2015
    -d --database=DATABASE      The name of the database in which you wish to store the Fred data.
                                If the database does not exist it will be created.
                                Default = 'fred_db'.
    -t --table=TABLE            The name of the table in which you wish to insert/update the data.
                                Default = 'fred_data
    -a --api_key=API_KEY        Your FRED api key.
                                Default = Fred API key of Dónal Flanagan.
    --host=HOST                 Database hostname.
                                Default = 'localhost'.
    --port=PORT                 The Postgres port.
                                Default = 5432
"""

import sys
import logging
import pandas as pd
from fredapi import Fred
from sqlalchemy import create_engine, text, Table, Column, DateTime, Numeric, MetaData
from sqlalchemy_utils import database_exists, create_database
from docopt import docopt


logger = logging.getLogger('fred_stats')
__version__ = '0.0.1'


class FredStats:
    def __init__(self, api_key):
        self.fred = Fred(api_key=api_key)

    def retrieve_stats(self, series_names):
        # Retrieve the data from the FRED api
        frames = []
        for series_name in series_names:
            data_series = self.fred.get_series(series_name).rename(series_name)
            frames.append(data_series)

        data = pd.concat(frames, axis=1)
        data.index.name = 'timestamp'
        return data


class DatabaseInterface:
    def __init__(self,
                 db_name,
                 user,
                 password,
                 host='localhost',
                 port=5432):

        self.portgres_url = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.db_name = db_name
        self._engine = create_engine(self.portgres_url)
        self._connection = self._engine.connect()
        self.metadata = MetaData(self._engine)
        self._check_db_exists()

    def _check_db_exists(self):
        if not database_exists(self._engine.url):
            try:
                create_database(self._engine.url)
                logger.info('Database created: %s', self.db_name)

            except Exception as exc:
                logger.exception('Could not create database. \nException: %r', exc)
                return exc

    def _get_table(self, table_name, data):

        table = Table(table_name,
                      self.metadata,
                      Column(data.index.name, DateTime),
                      Column((col_name, Numeric) for col_name in data.columns.values))

        # If the table does not already exist, create it.
        if not self._engine.dialect.has_table(self._engine, table_name):
            try:
                self.metadata.create_all()
                logger.info('Table created: %s', self.db_name)

            except Exception as exc:
                logger.exception('Could not create table. \nException: %r', exc)
                return exc

        return table

    def insert_data(self, data, table_name):

        table = self._get_table(table_name, data)

        data.reset_index(level=0, inplace=True)
        data = data.to_dict('records')

        # Bulk insert the data
        self._connection.execute(table.insert(), data)

    def retrieve_avg_unemployment_rate(self, table_name, start_date, end_date, ):

        # Query the SQL table for the average unemployment rate.
        unemployment_query = """SELECT Extract(YEAR from timestamp)::INT as year, avg(unrate)
                                FROM {t_name}
                                WHERE timestamp >= :start_date and timestamp <= :end_date
                                GROUP BY year
                                ORDER BY year;""".format(t_name=table_name)

        result = self._engine.execute(text(unemployment_query), start_date=start_date, end_date=end_date)

        # Insert the data into a dataframe
        df = pd.DataFrame(result.fetchall())
        # Set the column names in the dataframe
        df.columns = result.keys()
        # Set the year column as the index
        df.set_index('year', inplace=True)


def main():

    args = docopt(__doc__, version='fred_stats %s' % __version__)

    api_key = args.get('--api_key') if args.get('--api_key') else '01af77900eb060649a7c504ee0705b4d'

    db_name = args.get('--database') if args.get('--database') else 'fred_db'
    user = args.get('--user')
    password = args.get('--password')
    host = args.get('--host') if args.get('--host') else 'localhost'
    port = int(args.get('--port')) if args.get('--port') else 5432

    table_name = args.get('--table') if args.get('--table') else 'fred_data'
    start_year = args.get('--start') if args.get('--start') else '1980'
    end_year = args.get('--end') if args.get('--end') else '2015'

    start_date = '{start_year}-01-01'.format(start_year=start_year)
    end_date = '{end_year}-12-31'.format(end_year=end_year)

    series_names = ['GDPC1', 'UMCSENT', 'UNRATE']

    try:
        logging.basicConfig(level=logging.DEBUG)
        logger.info('starting fred_stats')

        fred_stats = FredStats(api_key=api_key)
        fred_data_df = fred_stats.retrieve_stats(series_names=series_names)

        dbi = DatabaseInterface(db_name, user, password, host, port)
        dbi.insert_data(fred_data_df, table_name)

        avg_unemployment = db

        print('The average rate of unemployment in the USA for each year between %s and %s is as follows:' %
              (start_date, end_date))
        print(df)

    except KeyboardInterrupt:
        logger.info('Stopping fred_stats')
    except Exception as exc:
        logger.exception('Got exception %r', exc)
        return exc

if __name__ == '__main__':
    sys.exit(main())
