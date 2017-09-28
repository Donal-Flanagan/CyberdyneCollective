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
