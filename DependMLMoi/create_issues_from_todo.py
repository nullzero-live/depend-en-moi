import os
from github import Github as gh
from github import Auth
from active_repo import get_remote_url, repo_main

auth = Auth.Token(os.getenv('GITHUB_TOKEN'))
g = gh(auth=auth)
g.getuser().login
repo = repo_main()

# Parse 'TODO.md' and extract todo items
def parse_todo_file(file_path):
    with open(file_path, 'r') as file:
        todos = file.readlines()
    return [line.strip() for line in todos if line.strip()]

# Check if an issue already exists
def issue_exists(repo, title):
    issues = repo.get_issues(state='open')
    return any(issue.title == title for issue in issues)

# Create an issue if it doesn't exist
def create_issue_if_not_exists(repo, todo):
    if not issue_exists(repo, todo):
        repo.create_issue(title=todo, body='')

repo = g.get_repo(repo)

todos = parse_todo_file('../TODO.md')
for todo in todos:
    create_issue_if_not_exists(repo, todo)
