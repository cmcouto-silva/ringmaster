"""
Call a database function from the command line.
"""

import sys

import sql


def main(function_name, args):
    """Call a database function from the command line."""
    func = sql.DatabaseFunction(function_name)
    rows = func(*args)
    sql.to_csv(rows, stream=sys.stdout)


if __name__ == '__main__':
    function_name, args = sys.argv[1], sys.argv[2:]
    main(function_name, args)
