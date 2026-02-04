from github import Github
## In Above Here Github is the clases which import from github library "that is py github library"
## In Above github is the package which refer to py. here main module is github

#Provide the Token
token = "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"
g = Github(token)

#Get the authenticated user
user = g.get_user()
usr = user.login
print(usr)
print(f"Username:{user.login}")
print(f"Public Repose:{user.public_repos}")
print(f"Followers:{user.followers}")