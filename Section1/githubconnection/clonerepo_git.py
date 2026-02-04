import git     # Here git is the library

# Define the URL of git hub repository
repo_url = "https://github.com/singhnsy/csvserver.git"

# Deifne the directory where you want clone the reposity
#clone_dir = "\localhost\Ubuntu\home" 
clone_dir = "C:\Users\hp\DevSecOps\pythonfordevops\Section1\githubconnection\repo1"    

# Run  the git clone command
#output = git.Repo.clone_from(repo_url, clone_dir)
try:
    git.Repo.clone_from(repo_url, clone_dir)
    print(f"Repository clone sucessfully to {clone_dir}")
except git.GitError as e:
    print(f"Error cloneing the repository:{e}")