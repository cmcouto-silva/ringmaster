#!/usr/bin/env python
"""
Prompt for continued execution of a program.
"""

import sys

try:
    from builtins import input
except ImportError:
    if sys.version_info[0] < 3:
        input = raw_input


def ask_to_continue():
    """Ask the user if they'd like to continue execution."""
    
    response = input('Continue [y/n]? > ')
    answer = response[0].lower()
    
    while answer not in {'y', 'n'}:
        answer = input('> ')[0].lower()

    return {'y': 0, 'n': 1}[answer]


if __name__ == '__main__':
    sys.exit(ask_to_continue())
