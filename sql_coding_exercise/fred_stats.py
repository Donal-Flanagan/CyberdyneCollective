# -*- coding: utf-8 -*-

#fixme removed redundant args
"""
Retrieve statistics from the FRED api

Usage:
    fred_stats.py [--host=HOST] --user=USER --password=PASSWORD --api_key=API_KEY [-n -f -c -s]
    fred_stats.py (-h | --help)
    fred_stats.py (-v | --version)

Options:
  --host=HOST                   Database hostname.
  -u --user=USER                Your Postgres username
  -p --password=PASSWORD        Your Postgres password.
  -a --api_key=API_KEY          Your FRED api key
  -h --help                     Show this screen.
  -v --version                  Show version.

Additional options:
  -n, --remove-non-fredsters        Remove users which do not have an @fredknows.it email
                                    address from the fred.ava_projects collection.
  -f, --deactivate-feedbackforms    Deactivate email notifications and remove notifications
                                    email address from feedback forms.
  -c, --remove-customer-feedback    Set feedback fields to null in all games.
  -s, --remove-statistics           Remove all documents from statistics collection.
"""

#fixme: remove redundant imports
import sys
import logging
import re
import psycopg2
import requests

from docopt import docopt

from pprint import pprint as pp


logger = logging.getLogger('fred_stats')
__version__ = '0.0.1'


def main():
    args = docopt(__doc__, version='fki-missing-answers %s' % __version__)

    host_name = args.get('--host')
    user = args.get('--user')
    password = args.get('--password')
    api_key = args.get('--api_key')
    db_name = 'testpython'

    fred_url = 'https://api.stlouisfed.org/fred/series/search?api_key={}&search_text=canada'

    if host_name:
        host = host_name
    else:
        host = 'localhost'

    if api_key:
        key = api_key
    else:
        key = '01af77900eb060649a7c504ee0705b4d'

    try:

        print('host:', host)
        print('user:', user)
        print('password:', password)
        print('db_name:', db_name)

        print(fred_url)
        print(key)
        print('.................................')
        print(fred_url.format(key))

        logging.basicConfig(level=logging.DEBUG)
        logger.info('starting fred_stats')




        '''
        req = requests.post(fred_url % key)
        req.raise_for_status()
        data = req.json()


        connect_str = "dbname={db_name} user={user} host={host} password={password}".format(
            db_name=db_name, user=user, host=host, password=password
        )

        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # create a new table with a single column called "name"
        cursor.execute("""CREATE TABLE tutorials (name char(40));""")
        # run a SELECT statement - no data in there, but we can try it
        cursor.execute("""SELECT * from tutorials""")
        rows = cursor.fetchall()
        print(rows)
        '''



    except KeyboardInterrupt:
        logger.info('stopping fred_stats')
    except Exception as exc:
        logger.exception('got exception %r', exc)
        return exc


if __name__ == '__main__':
    sys.exit(main())
