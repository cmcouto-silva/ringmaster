"""
Call a database function from the command line.
"""

import sys

from db_driver import sql


def main(function_name, args):
    """Call a database function from the command line."""
    with sql.DatabaseFunction(function_name) as func:
        rows = func(*args)
        sql.to_csv(rows, stream=sys.stdout)


def console_script():
    function_name, args = sys.argv[1], sys.argv[2:]
    main(function_name, args)


if __name__ == '__main__':
    console_script()
