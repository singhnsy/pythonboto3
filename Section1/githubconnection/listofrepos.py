from github import Github
## In Above Here Github is the clases which import from github library "that is py github library"
## In Above github is the package which refer to py. here main module is github

#Provide the Token
token = "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"
g = Github(token)

user = g.get_user("singhnsy")

#List for the reposiroties
for repo in user.get_repos():
    print(f"Repose Name:{repo}")