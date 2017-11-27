#!/bin/bash

# Toy example to test the control flow of the test process.

# Exit on nonzero error code
set -e

# Trigger response to an error
./scripts/error.sh > tests/test.out 2>&1
./scripts/checkpoint.py

# Pass through a passed test
./scripts/passed.sh > tests/test.out 2>&1
./scripts/checkpoint.py

# Trigger response to a failed test
./scripts/failed.sh > tests/test.out 2>&1
./scripts/checkpoint.py

# Pass through another passed test
./scripts/passed.sh > tests/test.out 2>&1
./scripts/checkpoint.py
