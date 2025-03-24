# How to create a Virtual Environment
Most info taken from: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments

## For a specific project (also what to do in VS Code's terminal)
CREATE:
1. python3 -m venv .venv (explanation of the -m flag: https://stackoverflow.com/a/62923810)
2. add .venv to .gitignore
3. source .venv/bin/activate
4. which python
5. python3 -m pip install --upgrade pip
6. python3 -m pip --version
7. python3 -m pip install XXXX


ACTIVATE:
1. source .venv/bin/activate
2. which python (to check that it is using python from .venv/bin/python)
3. VS code: doublecheck pylance uses the right python version. Bottom right corner when in a python file. Switch to venv version

DEACTIVATE:
1. deactivate

DELETE:
1. rm -r .venv

## In general for the terminal
1. mkdir -p $HOME/.venvs  # create a folder for all virtual environments 
2. python3 -m venv $HOME/.venvs/XXX   # XXX is name of virtual environment
3. $HOME/.venvs/MyEnv/bin/python --version   # to check what version is used in venv
4. Install packages, two options:
   1. $HOME/.venvs/MyEnv/bin/python -m pip install XXXXX    # XXXXX is package name
   2. Activate venv and then use: python3 -m pip install XXXXX
5. source $HOME/.venvs/MyEnv/bin/activate    # Activating the venv