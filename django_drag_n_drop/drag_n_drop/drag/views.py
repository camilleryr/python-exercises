from django.shortcuts import render
import requests

class issue():
    def __init__(self, source_issue):
        self.id = source_issue['id']
        self.ticket_number = source_issue['number']
        self.title = source_issue['title']
        self.body = source_issue['body']


def index(request):
    headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                'Authorization': 'Basic Y2FtaWxsZXIueXJAZ21haWwuY29tOjNyZE5pZ2h0'}

    url = 'https://api.github.com/repos/camilleryr/bandstagram/issues'

    response = requests.get(url, headers=headers).json()

    issues = [issue(x) for ind, x in enumerate(response)]

    context = {
        'issues': issues,
    }
    return render(request, 'drag/index.html', context)