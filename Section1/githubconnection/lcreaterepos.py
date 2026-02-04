from github import Github
## In Above Here Github is the clases which import from github library "that is py github library"
## In Above github is the package which refer to py. here main module is github

#Provide the Token
token = "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"
g = Github(token)

#Get the authenticated user
user = g.get_user()

#Create new repository
repo_name = "myrepos123"
repo = user.create_repo(repo_name)
print(f"Repise create {repo} successfully")
