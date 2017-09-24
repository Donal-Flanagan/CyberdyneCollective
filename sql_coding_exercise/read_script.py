# -*- coding: utf-8 -*-

#fixme removed redundant args
"""
Retrieve statistics from the FRED api

Usage:
    fred_stats.py --user=USER --password=PASSWORD [--host=HOST] [--api_key=API_KEY] [--database=DATABASE] [--port=PORT]
    fred_stats.py (-h | --help)
    fred_stats.py (-v | --version)

Options:
    -u --user=USER                Your Postgres username.
    -p --password=PASSWORD        Your Postgres password.
    --host=HOST                   Database hostname. Default = 'localhost'.
    -a --api_key=API_KEY          Your FRED api key.
                                  Default = Dónal Flanagan's Fred API key.
    -d --database=DATABASE        The name of the database in which you wish to store the Fred data.
                                  If the database does not exist it will be created. Default = 'fred_db'.
    --port=PORT                   The Postgres port. Default = 5432
    -h --help                     Show this screen.
    -v --version                  Show version.

"""

#fixme: remove redundant imports
import sys
import logging
import re
import psycopg2
import requests
import pandas as pd
from fredapi import Fred
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from docopt import docopt

from pprint import pprint as pp


logger = logging.getLogger('fred_stats')
__version__ = '0.0.1'


def main():
    args = docopt(__doc__, version='fki-missing-answers %s' % __version__)

    user = args.get('--user')
    password = args.get('--password')
    host = args.get('--host') if args.get('--host') else 'localhost'
    api_key = args.get('--api_key') if args.get('--api_key') else '01af77900eb060649a7c504ee0705b4d'
    db_name = args.get('--database') if args.get('--database') else 'fred_db'
    port = args.get('--port') if args.get('--port') else 5432

    db_connection = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        database=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )

    try:

        engine = create_engine(db_connection)

        print('\n---------------------------------------')
        print('data inserted')
        print('---------------------------------------\n')

        unemployment_query = """
            SELECT EXTRACT(YEAR from timestamp)::INT as year, avg(unrate)
            FROM fred_data
            where timestamp >= '1980-01-01' and timestamp <= '2015-12-31'
            GROUP BY year
            ORDER BY year
        """

        result = engine.execute(unemployment_query)

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
