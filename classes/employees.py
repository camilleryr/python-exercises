class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
        self.name = name
        self.employee = []

    def get_name(self):
        """Returns the name of the company"""

    def add_employee(self, Employee):
        self.employee.append(Employee)
        
    def display(self):
        print(f'{self.name} :')
        for emp in self.employee:
            emp.display()


class Employee(object):
    '''This represents the people who work at a company'''

    def __init__(self, first_name = "", last_name = "", job_title = "", start_date = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.start_date = start_date

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_job_title(self, job_title):
        self.job_title = job_title

    def set_start_date(self, start_date):
        self.start_date = start_date

    def display(self):
        print(f'{self.first_name} {self.last_name} : {self.job_title} : {self.start_date}')

chris = Employee()
chris.set_first_name("Chris")
chris.set_last_name("Miller")
chris.set_job_title("Baller")
chris.set_start_date("Allways")

sarah = Employee("Sarah", "Szpak", "Mrs Manager", "A.T.T.")

stephen = Employee("Stephen", "Szpak", "Bro In Law", "10/27/16")

shadow_ln = Company("Shadown Ln")

shadow_ln.add_employee(chris)
shadow_ln.add_employee(sarah)
shadow_ln.add_employee(stephen)
shadow_ln.display()