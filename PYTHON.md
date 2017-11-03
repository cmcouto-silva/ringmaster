These are taken from a Python resources write-up I sent out after an informal Python
seminar I held in September 2017. They briefly go over the tools pip, virtualenv, and
virtualenvwrapper.

Feel free to reach out at christiemj09@gmail.com or on Slack if you have any questions.

## [pip](https://pip.pypa.io/en/stable/)

I assumed in the meeting that this was already known/being used, but I’ve always had to
install pip globally before proceeding when I’ve set up my machines in the past. I think
this is changing--some new releases of operating systems come with pip installed, or some
Python distributions come with pip--but just in case, above is the link to the definitive
package manager for Python.

## [virtualenv](https://virtualenv.pypa.io/en/stable/)

Allows you to install third-party and personal code in userspace (in your home directory),
and use that code anywhere on your computer. To use a virtual environment, you "activate"
it. You don’t have to worry about screwing up your global system directories, or about
conflicting versions of packages.

Also, Ian was right; there are security reasons for not installing things globally on your
computer: https://askubuntu.com/questions/802544/is-sudo-pip-install-still-a-broken-practice 

This raises the question, though: How do you install virtualenv globally on your computer
... without installing it globally on your computer? I’ve always just ripped the band-aid
off and globally installed virtualenv and virtualenvwrapper, and then I never install
anything globally ever again.

## [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/), [virtualenvwrapper-win](https://github.com/davidmarble/virtualenvwrapper-win/)

This is a set of shell scripts (or batch scripts in virtualenvwrapper-win for Windows)
that give you some nice commands for managing any virtual environments you might use.
There’s a little setup involved--you have to add the locations of a script and a directory
to your shell’s profile (files like `~/.bashrc`, `~/.profile`, `~/.bash_profile`, etc.), at
least for the UNIX version--but I think it’s worth it in terms of being able to easily set
up, tear down, and keep track of any virtual environments on your computer. Quick recap of
the commands:

* `lsvirtualenv`: lists all the virtual environments that currently exist
* `mkvirtualenv`: make a new, empty virtual environment
* `rmvirtualenv`: delete an existing virtual environment
* `workon`: "activate" or enter a virtual environment
* `deactivate`: "deactivate" or exit a virtual environment

## pip freeze

The command `pip freeze` shows you what pip has installed in your current environment.
On UNIX systems (and probably somehow on Windows machines), you can redirect the output
of this command into a file. This file documents the dependencies of your project (numpy,
scipy, requests, etc.) and can be used to fetch those dependencies if you want to use your
project on a new machine in a new virtual environment.

Example on UNIX systems:
```
$ pip freeze > requirements.txt
```

## pip install -r requirements.txt

This command installs all the packages that are listed in the file `requirements.txt`. This
is how you can easily reinstall everything that your project depends on in a new virtual
environment elsewhere, provided that new place has pip and virtualenv installed.

