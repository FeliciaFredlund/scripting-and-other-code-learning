# Step by Step List for Starting a GitHub Project with Terminal

## Starting from scratch

1. Create repository at Github
2. Copy the link
3. Navigate to the folder where you want the project folder to be
4. mkdir NEW_DIR
5. git clone REPO_URL NEW_DIR
6. Done

## Starting from an exisiting project

1. Navigate to the folder holding the project (or open folder in VS code)
2. git init
3. git add . -- OBS make sure there aren't extra files you don't want added, like .DS_Store on MAC
4. git commit -m "Initial files."
5. git branch -M main (to make sure branch is named main, -M forces the change)
6. git remote add origin REPO_URL
7. git push -u origin main

*Extra Curricular*
Might want to create a .gitignore
Might want to create a virtual enviroment, see create_virtual_environment.md for instructions