#!/usr/bin/env python
"""
Get a piece of credentials configuration info.
"""

import sys

from db_driver.get import get

CREDENTIALS = '.creds'


def main(arg):
    """Get a piece of credentials configuration info."""
    return get(CREDENTIALS, arg)


def console_script():
    sys.stdout.write(main(sys.argv[1]))


if __name__ == '__main__':
    console_script()
