class Employee:
    company = "TechCrop"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}, Company: {self.company}")

emp1 = Employee("John")
emp2 = Employee("Mary")
emp1.display()
emp2.display()