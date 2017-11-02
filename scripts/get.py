#!/usr/bin/env python
"""
Get an argument from a JSON configuration file.
"""

import json
import sys


def get(filename, arg):
    with open(filename, 'r') as file_in:
        return json.load(file_in)[arg]


if __name__ == '__main__':
    script, filename, arg = sys.argv
    sys.stdout.write(get(filename, arg))
