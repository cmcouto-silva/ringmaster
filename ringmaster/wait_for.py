"""
Wait for a file to exist.
"""

import os
import sys
import time

from ringmaster import config


def main(filename, wait_time, max_waits):
    """Wait for a file to exist."""
    for attempt in range(max_waits):
        if os.path.exists(filename):
            break
        print(f"File {filename} doesn't exist on attempt {attempt}")
        sys.stdout.flush()  # Force output to log
        time.sleep(wait_time)


@config.from_env
def console_script(WAIT_TIME, MAX_WAITS):
    filename = sys.argv[1]
    wait_time, max_waits = map(int, [WAIT_TIME, MAX_WAITS])
    main(filename, wait_time, max_waits)


if __name__ == '__main__':
    console_script()
