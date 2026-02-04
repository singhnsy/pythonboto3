# This subprocess module is as the "bridge" between Python and the Command Line.
# It allows Python to talk directly to the Operating System, enabling you to 
# run CLI tools like git, docker, terraform, or kubectl directly from your script.
import subprocess 

# Define the URL of git hub repository
repo_url = "https://github.com/singhnsy/csvserver.git"

# Deifne the directory where you want clone the reposity
#clone_dir = "/home/nsy/githubconnection/"   
#clone_dir = "(C:\Users\hp\DevSecOps\pythonfordevops\Section1\githubconnection\)" 
clone_dir = "C:\\Users\\hp\\DevSecOps\\pythonfordevops\\Section1\\githubconnection\\"  

# Run  the git clone command
subprocess.run(["git", "clone", repo_url, clone_dir])