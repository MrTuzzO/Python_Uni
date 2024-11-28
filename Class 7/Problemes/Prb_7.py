class Employee:
    company_name = "Google"

    def __init__(self, name, position):
        self.name = name
        self.position = position


em1 = Employee("John", "Software Engineer")
em2 = Employee("Mary", "AI Engineer")

print(f"Name: {em1.name} Position: {em1.position}, Company: {em1.company_name}")
print(f"Name: {em2.name} Position: {em2.position}, Company: {em2.company_name}")