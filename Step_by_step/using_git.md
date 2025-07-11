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

## When forking projects to contribute suggestions
1. Fork project
2. Clone it to local machine
3. Add another git remote, so you can update your fork to the latest version. To avoid fixing what someone else have already fixed and to avoid merging conflicts. Example: git remote add upstream LINK-TO-ORIGINAL-REPO
4. Create new branch YOUR-FEATURE
5. Make changes
6. Commit and push to your own fork's YOUR-FEATURE branch
7. Create a pull request (PR) to the original_owner/repo main from your_username/repo YOUR-FEATURE. Remember to include a good description of what changes you made and why.

