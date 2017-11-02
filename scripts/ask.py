#!/usr/bin/env python
"""
Ask the user if they'd like to continue execution of the build process.
"""

import sys


def main():
    """Ask the user if they'd like to continue execution. Run as a child process."""
    
    response = input('Continue [y/n]? > ')
    answer = response[0].lower()
    
    while answer not in {'y', 'n'}:
        answer = input('> ')[0].lower()

    # Communicate with parent process through error codes

    if answer == 'y':
        sys.exit(0)
    
    sys.exit(1)


if __name__ == '__main__':
    main()
