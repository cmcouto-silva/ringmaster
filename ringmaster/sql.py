"""
Use SQLAlchemy to interact with a PostgreSQL database.
"""

import csv
import sys

import psycopg2
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select, func

from ringmaster.config import from_json, from_env


CREDENTIALS = '.creds'


def postgres_engine(user, dbname, host, port, **kwargs):
    """Make a PostgreSQL database engine."""
    url = 'postgresql+psycopg2://{user}@{host}:{port}/{dbname}'.format(
        user=user, host=host, port=port, dbname=dbname
    )
    return create_engine(url, echo=False)


def postgres_connection(user, dbname, host, port, **kwargs):
    """Make a PostgreSQL database connection."""
    dsn = 'dbname={dbname} user={user} host={host} port={port}'.format(
        dbname=dbname, user=user, host=host, port=port
    )
    return psycopg2.connect(dsn)


def preconfigured_engine(load_method='from_json'):
    """Get a preconfigured PostgreSQL database engine."""
    return {
        'from_json': (lambda: from_json(postgres_engine)(CREDENTIALS)),
        'from_env': (lambda: from_env(postgres_engine)())
    }[load_method]()


def preconfigured_connection(load_method='from_json'):
    """Get a preconfigured PostgreSQL database connection."""
    return {
        'from_json': (lambda: from_json(postgres_connection)(CREDENTIALS)),
        'from_env': (lambda: from_env(postgres_connection)())
    }[load_method]()


class DatabaseEnvironment(object):
    """Database setup and teardown."""
    
    def __init__(self, load_method='from_json'):
        self.engine = preconfigured_engine(load_method=load_method)
        self.meta = MetaData()
        self.conn = self.engine.connect()
    
    def __enter__(self):
        self.trans = self.conn.begin()
        return self
    
    def __exit__(self, type_, value, traceback):
        if type_:
            self.trans.rollback()
        else:
            self.trans.commit()

    def Table(self, table, **kwargs):
        return Table(table, self.meta, autoload=True, autoload_with=self.engine, **kwargs)


class DatabaseFunction(object):
    """A wrapper around a function in the database."""
    
    def __init__(self, name, load_method='from_json'):
        self.name = name
        self.engine = preconfigured_engine(load_method=load_method)
        self.conn = self.engine.connect()
    
    def __enter__(self):
        """Wrap the function in a transaction."""
        self.trans = self.conn.begin()
        return self
    
    def __call__(self, *args):
        """Run a function in the database with positional arguments."""
        res = self.conn.execute(
            select(getattr(func, self.name)(*args))
        )
        return res
    
    def __exit__(self, type_, value, traceback):
        """Rollback on error, else commit."""
        if type_:
            self.trans.rollback()
        else:
            self.trans.commit()

 
def to_csv(res, stream=sys.stdout):
    """Write a result set to a stream as a CSV."""
    writer = csv.writer(stream)
    for row in res:
        writer.writerow(row)
