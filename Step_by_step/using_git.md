# How to Use Git - The Most Common Commands (for the forgetful)

1. git clone: for cloning a project, see start_git_project.md for step by step
2. git add ., git commit -m "MESSAGE", git push origin main: commit code and save it up to GitHub/your git repo
3. git status: see the status of your files
4. git --no-pager log --oneline: nice formating of log
5. git pull origin main: pull everything from the main branch of origin


## For Git 2 on Boot.dev if you goof up
1. git commit --amend : version
   - git log --oneline -l -p : show content of previous commit
   - git commit --amend : can change the message for the latest commit. Changes the sha/hash for the commit
2. git reset --soft HEAD~1 : version
   - git reset --soft HEAD~1 : gets rid of the last commit, but not the changes. The changes are not staged anymore (git added)
   - Will often use this when fixing rebase merge conflict, as in, if you commit instead of rebase the changes you can just undo the commit with your changes intact.

