class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Khirul", 23, [85, 90, 78])

student1.display()
print(student1.average_grade())
