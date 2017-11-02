#!/bin/bash

# Build process POC. Build a toy example database.
# Constitutes a formal description of a specific build with tests.

# Stop if nonzero error code; this is how program flow is controlled.
set -e

# Get database credentials from configuration file
GET="./scripts/get.py .creds"

# Make psql pretty :) Do we need to worry about shell injection?
RUN="psql -U $($GET user) -d $($GET dbname) -h $($GET host) -c"
CHECK="psql -t -U $($GET user) -d $($GET dbname) -h $($GET host) -F , --no-align --pset footer -f"

### BUILD PROCESS STARTS HERE ###

# Could inspect the shorthand first, I suppose, as a guard against injection before it's run

echo "RUN is:"
echo "$RUN"

echo

echo "CHECK is:"
echo "$CHECK"

echo

./scripts/pause.py

$RUN "SELECT wipe_tables();"
$CHECK tests/test_wipe_tables.sql > tests/test.out 2>&1
./scripts/checkpoint.py  # Flags you can pass: dirty strict quiet

$RUN "SELECT init_tables();"
$CHECK tests/test_init_tables.sql > tests/test.out 2>&1
./scripts/checkpoint.py

$RUN "SELECT pop_tables();"
$CHECK tests/test_pop_tables.sql > tests/test.out 2>&1
./scripts/checkpoint.py

# Question for Dan: Do you wrap your build process in one big transaction?
# Would need to modify this if so, commits are made after each high-level build function.

