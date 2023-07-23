import os

# Change directory to the workspace
os.chdir('workspace')

# Initialize the local directory as a Git repository
os.system('git init')

# Add all new and modified files to the staging area
os.system('git add .')

# Commit the changes
os.system('git commit -m "Committing changes"')

# Add remote repository
os.system('git remote add origin git@github.com:Kaneofthrones/comstar-auto.git')

# Rename current branch to 'main'
os.system('git branch -M main')

# Push changes to the remote repository
os.system('git push -u origin main')