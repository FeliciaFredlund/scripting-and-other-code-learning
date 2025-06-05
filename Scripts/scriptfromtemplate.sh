#!/bin/bash

# Copy code template to new file with new name.
# Being able to do both python scrips and bash scripts, and also have an interactive mode
# Last updated: 2025-06-05

destination=""
template=""

if [ $# -eq 0 ]; then
    echo "## Interactive mode chosen ##"
    read -p "Bash script (b) or python script/file (p): " template
    read -p "Absolute or relative path to new script (including filename): " fullpath
    destination="$fullpath"
fi

if [ $# -eq 1 ]; then
    destination=$1
    if [[ $destination == *.py ]]; then
        template=p
    elif [[ $destination == *.sh ]]; then
        template=b
    else
        echo "No template could be selected from the new filename."
        read -p "Bash script (b) or python script/file (p): " template
    fi
fi


if [[ $template == "p" ]]; then
    if [[ $destination != *.py ]]; then
        destination=$destination.py
    fi 
    cp ~/Workspace/github.com/scripting-and-other-code-learning/Templates/python_template.py $destination
    exit 0
elif [[ $template == "b" ]]; then
    if [[ $destination != *.sh ]]; then
        destination=$destination.sh
    fi 
    cp ~/Workspace/github.com/scripting-and-other-code-learning/Templates/bash_template.sh $destination
    exit 0
else
    echo "ERROR: No valid template could be chosen."
    exit 1
fi
