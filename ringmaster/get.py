#!/usr/bin/env python
"""
Get an argument from a JSON configuration file.
"""

import json
import sys


def get(filename, arg):
    with open(filename, 'r', encoding='utf8') as file_in:
        return json.load(file_in)[arg]


def console_script():
    script, filename, arg = sys.argv
    sys.stdout.write(get(filename, arg))


if __name__ == '__main__':
    console_script()
