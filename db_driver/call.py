"""
Call a database function, send its output to standard out as a CSV.
"""

import os
import sys

from db_driver.config import from_config
from db_driver import sql, decs


class DatabaseFunctionCall(object):
    """A database function call."""
    
    def __init__(self, name, signature):
        self.func = sql.DatabaseFunction(name)
        self.signature = signature
    
    def __enter__(self):
        """Wrap the database function call in a transaction."""
        begin_transaction = self.func.__enter__()
        return self
    
    def __exit__(self, type_, value, traceback):
        """Rollback on error, else commit."""
        commit_or_rollback = self.func.__exit__(type_, value, traceback)
    
    def get_arguments(self, kwargs):
        """Get a list of function arguments according to its signature."""
        return [kwargs[param] for param in self.signature]
    
    def execute(self, **kwargs):
        """Execute the database function call according to keyword arguments."""
        args = self.get_arguments(kwargs)
        return self.func(*args)


def main(dec_file, call_file):
    """Call a database function, send its output to standard out as a CSV."""
    
    # Instantiate a database function call with its declaration
    with from_config(DatabaseFunctionCall)(dec_file) as call:
    
        # Call it with the arguments described in the call file
        rows = from_config(call.execute)(call_file)
    
        # Write the output of the function to standard out
        sql.to_csv(rows, stream=sys.stdout)


def console_script():
    # Specify function name instead of declaration file
    script, func_name, call_file = sys.argv
    dec_file = os.path.join(decs.DECS, '{func}.json'.format(func=func_name))
    main(dec_file, call_file)


if __name__ == '__main__':
    console_script()

