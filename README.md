# Scripting and other Code Learning
For misc code learning and some step by step guides

## Assorted_Learning
A directory for files where I am trying to learn something, but code I won't be using outside of the learning purpose.

## D0023D Communications
A couple of scripts made for connecting to and configuring a router with Netmiko for a uni course.

## D0042D Programmering
Scripts related to a python coding course at uni. Most of them are not useful for the future, except the paramiko scripts that I might want to iterate on and build out into a CLI with the actual Paramiko code abstracted out.

## Scripts
Scripts I have either written to actually use, or starts of scripts I might want to continue or adapt.

copyfilewithchanges.py is the start of a python script with quite a bit of file management built in. Could be nice to either build one like that out proper, or look up a python library/module that abstracts that well already.

heading-to-filename.py was a short script I wrote to change headings/lines of normal text TO usable filenames. I will probably iterate on this, and also make a version that takes files with bad filenames (meaning with spaces) and fix them to have no spaces. Could be nice to choose which deliminator to use instead of space.

make_backup.sh and restore_backup.sh are scripts written for a course that I think I want to iteratate on and make my own. Probably won't use encryption, I will see. But would be something to easy back up my linux computer, perhaps even something that could run on Windows and maybe also for Mac.

newpythonscript.sh is exactly what it says, more or less. It takes the python template in Templates and copies it with a new name to a directory of choice with a filename of choice. It makes sure .py is part of the filename.

scriptfromtemplate.sh is a generic bash script that takes a script template of choice from Templates and copies it into a chosen directory with a chosen filename. For Python, it will make sure the filename ends with .py. For Bash, it will check if it is being put in a bin folder, if not, it will make sure the filename ends in .sh.

## Step_by_step
Lots of markdown files with instructions on how to do different things. Also includes some short files with sample code that I tend to forget.

## Templates
Holds code templates that I want to copy. Can either be done manually or with one of the scripts in the Scripts folder.