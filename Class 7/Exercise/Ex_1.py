class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, My name is {self.name} and I am {self.age} years old.")

s1 = Student("John", 18)
s1.introduce()