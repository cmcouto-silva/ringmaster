"""
Use SQLAlchemy to interact with a PostgreSQL database.
"""

import csv
import sys

import psycopg2
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, func


from config import from_config


CREDENTIALS = '.creds'


def postgres_engine(user, dbname, host, port, echo=False):
    """Make a PostgreSQL database engine."""
    url = f'postgresql+psycopg2://{user}@{host}:{port}/{dbname}'
    return create_engine(url, echo=echo)


def postgres_connection(user, dbname, host, port, echo=False):
    """Make a PostgreSQL database connection."""
    dsn = f'dbname={dbname} user={user} host={host} port={port}'
    return psycopg2.connect(dsn)


def preconfigured_engine():
    """Get a preconfigured PostgreSQL database engine."""
    return from_config(postgres_engine)(CREDENTIALS)


def preconfigured_connection():
    """Get a preconfigured PostgreSQL database connection."""
    return from_config(postgres_connection)(CREDENTIALS)


class DatabaseFunction(object):
    """A wrapper around a function in the database."""
    
    def __init__(self, name):
        self.name = name
        self.engine = preconfigured_engine()
        self.conn = self.engine.connect()
    
    def __call__(self, *args):
        """Run a function in the database with positional arguments."""
        res = self.conn.execute(
            select([
                getattr(func, self.name)(*args)
            ])
        )
        return res

 
def to_csv(res, stream=sys.stdout):
    """Write a result set to a stream as a CSV."""
    writer = csv.writer(stream)
    for row in res:
        writer.writerow(row)
