from django.shortcuts import render
import requests
import base64
import json

class issue():
    def __init__(self, source_issue):
        self.id = source_issue['id']
        self.ticket_number = source_issue['number']
        self.title = source_issue['title']
        self.body = source_issue['body']


def index(request):
    return render(request, 'drag/index.html')


def create(request):
    credentials = f'{request.POST.get("username", "")}:{request.POST.get("password", "")}'
    encoded_credentials = base64.b64encode(str.encode(credentials))

    headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                'Authorization': f'Basic {encoded_credentials}'}
    url = f'https://api.github.com/repos/{request.POST.get("source_repo", "")}/issues'

    response = requests.get(url, headers=headers).json()

    issues = [issue(x) for ind, x in enumerate(response)]

    context = {
        "sprint_name" : request.POST.get("sprint", ""),
        "source_repo" : request.POST.get("source_repo", ""),
        'issues': issues,
    }
    return render(request, 'drag/create.html', context)

def display(request):
    context = {
        "sprint_name" : request.POST.get("sprint_name", ""),
        "source_repo" : request.POST.get("source_repo", ""),
        'issue_array': json.loads(request.POST.get("issue_array", "")),
    }

    print(context)
    return render(request, 'drag/display.html', context)