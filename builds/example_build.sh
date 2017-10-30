#!/bin/bash

# Build an example database. Formal description of the build process.

alias run="python scripts/cmd.py"

run wipe_tables
# Put tests here; pipe them into a Python program that suspends if there are
# errors or failed tests.

run init_tables
# Put tests here

run pop_tables
# Put tests here
