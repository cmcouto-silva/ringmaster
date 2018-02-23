# Inject tests into the database build process.

Author: Matt Christie (christiemj09@gmail.com)

## Introduction

### About

This repository lays out a way to specify database builds in shell scripts that
include automated tests in the build process. A build pauses after it encounters
test errors or failed tests, prompting the user to cease or continue execution.
Tests are run after each call to a build function.

Some benefits of this process:

* A build shell script fully specifies the build process for a specific build. Anyone who is code literate can do a complete trace of the build after it is run.
* Injecting tests into the build process documents function-level expected behavior.
* Injecting tests into the build process catches errors closer to their source, preventing them from propagating.

To supplement user-written tests, the repository includes definitions for views that display
information on the indexes and table constraints in a database. These can be used to survey
constraints that are maintained by the database vs. assumed constraints that need to be tested
more rigorously.

As an aside, some other functionality for documenting and inspecting database function calls
is also included. While not used in the formal build process, these tools highlight some
of the ways that Python can be used to interact with a database.

### Core usage and contents

Test the build process control flow:

```
$ test-checkpoint
```

Create an example database, load functions into it:

```
$ createdb -U <user> -h localhost <dbname>
$ for f in `ls functions`; do
>     psql -U <user> -d <dbname> -h localhost -f "functions/$f"
> done
```

Run an example build:

```
$ ./builds/example_build.sh
```

Tests that a build runs can be stored anywhere, but a good place for them is underneath `tests`:

```
$ ls tests
```

Load index and constraint views:

```
$ for sql in `ls sql/*_info.sql`; do
>    psql -U <user> -d <dbname> -h localhost -f "$sql"
> done
```

### Peripheral usage and contents

Run a function from the command line (injection prevented by SQLAlchemy):

```
$ # Pointed at local example database
$ run hello_world
$ run add 1 2

$ # Pointed at gibbs-test
$ run uuid_generate_v4
$ run create_property_key "FAZ BOA VISTA II"
```

Call a function from a saved set of arguments:

```
$ # Pointed at gibbs-test
$ # Grab function declarations (needed for call script)
$ decs public
$ # Call a function using an argument file
$ call create_property_key calls/faz_boa_vista_ii.json
```

Call a function from an interactive Python shell:

```
$ # Pointed at gibbs-test
$ python
...
>>> from ringmaster import sql
>>> create_property_key = sql.DatabaseFunction('create_property_key')
>>> result, = create_property_key('FAZ BOA VISTA II')
>>> print(result)  # Result is a tuple; res[0] is the string
```

## Using `ringmaster` to manage a project

`ringmaster` includes the script `ringmaster-init` that sets up a project root directory,
creating well-known locations for project elements like configuration, metadata, and tests:

```
$ mkdir -p project_root
$ cd project_root
$ ringmaster-init
...
$ ls -aR
```

Directories that `ringmaster-init` creates for project use:

* `builds` Shell scripts that encapsulate an entire build, carrying the database from one state to the next.
* `calls` JSON files specifying a call to a database function. Used to document a function call.
* `config` JSON files specifying arguments to any user-defined client-side scripts (cf. scripts directory).
* `creds` JSON files holding database credentials used to connect to a database.
* `decs` JSON files holding database function declarations that are fetched with the `decs` script. Input for the `call` script.
* `docs` Written material or other resources that document a project.
* `functions` Definitions of database functions, (i.e. CREATE OR REPLACE FUNCTION ...), especially build functions.
* `input` Input files to populate a database with. Symlinks to files elsewhere are encouraged but not required.
* `output` Output files generated while working on a project. Can be results, intermediate results, temporary debugging output, etc.
* `scripts` Any user-defined client-side scripts.
* `sql` Non-function SQL, like DDL, helper views, or other SQL relevant to a project.
* `tests` Boolean-valued tests written in SQL that can be injected into a database's build process.

## Dependencies

* Python 2.7 or 3.6 (tested on 2.7.13, 2.7.14, 3.6.3)
* [psycopg2](http://initd.org/psycopg/docs/) (Python database adapter)
* [SQLAlchemy](https://www.sqlalchemy.org/) (SQL automation library)

## Setup

### Installing dependencies

On Mac OS X, Homebrew is recommended for installing and upgrading Python. On Linux,
distro package managers (apt-get for Ubuntu, yum for Fedora, ...) should work, but
versions of Python may be old. Other versions of Python are likely to work, but
have not been tested.

The Python package manager [pip](https://pip.pypa.io/en/stable/) is the recommended
way for installing psycopg2 and SQLAlchemy. On Mac OS X, Homebrew ships pip with new
versions of Python. To check if pip is installed on your computer:

```
$ which pip  # System pip
$ which pip2  # Homebrew pip for Python 2
$ which pip3  # Homebrew pip for Python 3
```

The recommended way to install Python packages is underneath the user's home directory
in a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/stable/). See
`PYTHON.md` for resources on how to use virtual environments to manage third-party code.

If foregoing virtual environments, install psycopg2 and SQLAlchemy globally using pip:

```
$ sudo -H pip install psycopg2
$ sudo -H pip install sqlalchemy
```

### Configuring database credentials

Save database credentials in a file. Contents of `example_creds.json`:

```
{
    "user": "<user>",
    "dbname": "<dbname>",
    "host": "<host>",
    "port": "<port>"
}
```

Create multiple credentials files to connect in different ways (as a different user,
to a different database, etc.).

Use a symlink to point at the currently desired database credentials.
The symlink is expected to be named `.creds` in the project root:

```
$ cd path/to/ringmaster
$ ln -sf path/to/example_creds.json .creds
```

### Make a PostgreSQL password file

To avoid having to provide a password when connecting to the database, make a `~/.pgpass` file
(instructions [here](https://www.postgresql.org/docs/9.6/static/libpq-pgpass.html)).


