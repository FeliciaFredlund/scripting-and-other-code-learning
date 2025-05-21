#!/bin/bash

# Script for copying the python script template in Step_by_step to DIRECTORY/NEW_SCRIPT_NAME
# Author: Felicia Fredlund
# Last updated: 2025-05-21

# ./newpythonscriptinproject.sh

# ./newpythonscriptinproject.sh directory-for-new-script file-name-of-script
# ./newpythonscriptinproject.sh Scripts make_backup.sh

# ./newpythonscriptinproject.sh directory-for-new-script/file-name-of-script
# ./newpythonscriptinproject.sh Scripts/make_backup.sh

# bash ./newpythonscriptinproject.sh WITH SAME PARAMETER OPTIONS AS ABOVE

destination=""

if [ $# -eq 2 ]
then
    destination="$1/$2"
fi

if [ $# -eq 1 ]
then
    destination="$1"
fi

if [ $# -eq 0 ]
then
    echo "## Interactive mode chosen ##"
    read -p "Directory for script, absolute or relative path: " directory
    read -p "File name of the new script: " filename
    destination="$directory/$filename"
fi

if [[ $destination != *.py ]]
then
    destination=$destination.py
fi    

cp Templates/python_template.py $destination