#!/bin/bash

# Script for copying the python script template in Step_by_step to DIRECTORY/NEW_SCRIPT_NAME
# Author: Felicia Fredlund
# Last updated: 2025-06-05

# ./newpythonscriptinproject.sh

# ./newpythonscriptinproject.sh directory-for-new-script/file-name-of-script
# ./newpythonscriptinproject.sh Scripts/make_backup.sh

destination=""

if [ $# -eq 1 ]
then
    destination="$1"
fi

if [ $# -eq 0 ]
then
    echo "## Interactive mode chosen ##"
    read -p "Absolute or relative path to new script (including filename): " fullpath
    destination="$fullpath"
fi

if [[ $destination != *.py ]]
then
    destination=$destination.py
fi    

cp ~/Workspace/github.com/scripting-and-other-code-learning/Templates/python_template.py $destination