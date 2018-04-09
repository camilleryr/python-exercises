import requests

class issue():
    def __init__(self, source_issue, index):
        self.source_id = source_issue['id']
        self.source_ticket_number = source_issue['number']
        self.priority = index
        self.target_id = None

class automate():
    def __init__(self):
        self.issues = None
        self.target_backlog_id = None
        self.target_project_id = None
        self.headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                        'Authorization': 'Basic Y2FtaWxsZXIueXJAZ21haWwuY29tOjNyZE5pZ2h0'}

    def get_issues(self):
        url = 'https://api.github.com/repos/camilleryr/bandstagram/issues'
        response = requests.get(url, headers=self.headers).json()
        self.issues = [issue(x,len(response)-ind) for ind, x in enumerate(response)]
        # print(self.issues)
        return self

    def migrate_issues(self):
        url = 'https://api.github.com/repos/camilleryr/bandstagram/issues'
        response1 = requests.get(url, headers=self.headers).json()
        
        def match(x,y):
            return x==y

        url2 = 'https://api.github.com/repos/camilleryr/python-exercises/issues'
        for target_issue in self.issues:
            source_issue = next(i for i in response1 if match(i['id'], target_issue.source_id))
            body = {'title': target_issue.title, 'body': target_issue.body}
            
            response = requests.post(url2, json=body, headers=self.headers).json()
            target_issue.target_id = response['id']

        return self

    def create_project(self):
        url = 'https://api.github.com/repos/camilleryr/python-exercises/projects'
        body = {"name": "Test Project",
                "body": "This is a test project"}
        response = requests.post(url, json=body, headers=self.headers).json()
        self.target_project_id = response['id']

        return self

    def create_columns(self):
        url = f'https://api.github.com/projects/{self.target_project_id}/columns'
        columns=('Backlog', 'To Do', 'Ready For Testing', 'Done')
        for column in columns:
            response = requests.post(url, json={'name': column}, headers=self.headers)
            if column=='Backlog':
                self.target_backlog_id=response.json()['id']
            
        return self

    def groom_backlog(self):
        url = f'https://api.github.com/projects/columns/{self.target_backlog_id}/cards'
        sorted_issues = sorted(self.issues, key=lambda i: i.priority)

        for si in sorted_issues:
            body = {'content_id':si.target_id, "content_type":'Issue'}
            response = requests.post(url, json=body, headers=self.headers)

auto = automate()

auto.get_issues().migrate_issues().create_project().create_columns().groom_backlog()

# Source Repo will be saved to the DB and will need to be passed into the class on instantiation

# Target Repos will be entered from the client and will need to be grabbed from an HTTP request and 
# passed into the class on instantiation

# Username and Password will be entered from the client and will need to be grabbed from an HTTP 
# request and passed into the class on instantiation - https://docs.python.org/2/library/base64.html#base64.b64encode

# Get issues is currently creating a backlog from a repo of mine - 
# This will need to be refactored to pull the backlog info from the DB and sorted by priority

# compose migrate_issues => create_project => create_columns => groom_backlog into a single method
# and create an additinal abstracted method that can call the composed method for each target repo
# ie migrate(target) = composed method / migrate_all = for each target repo call compose method(target)

