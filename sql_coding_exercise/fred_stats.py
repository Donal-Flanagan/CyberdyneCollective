# -*- coding: utf-8 -*-

#fixme removed redundant args
"""
Retrieve statistics from the FRED api

Usage:
    fred_stats.py [--host=HOST] --user=USER --password=PASSWORD [-n -f -c -s]
    fred_stats.py (-h | --help)
    fred_stats.py (-v | --version)

Options:
  --host=HOST                   Database hostname.
  -u --user=USER                Your Postgres username
  -p --password=PASSWORD        Your Postgres password.
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

from docopt import docopt

from pprint import pprint as pp


logger = logging.getLogger('fred_stats')
__version__= '0.0.1'


def main():
    args = docopt(__doc__, version='fki-missing-answers %s' % __version__)

    host_name = args.get('--host')
    user = args.get('--user')
    password = args.get('--password')
    db_name = 'testpython'

    if host_name:
        host = host_name
    else:
        host = 'localhost'

    try:

        print('host:', host)
        print('user:', user)
        print('password:', password)
        print('db_name:', db_name)

        logging.basicConfig(level=logging.DEBUG)
        logger.info('starting fred_stats')

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



    except KeyboardInterrupt:
        logger.info('stopping fred_stats')
    except Exception as exc:
        logger.exception('got exception %r', exc)
        return exc


if __name__ == '__main__':
    sys.exit(main())