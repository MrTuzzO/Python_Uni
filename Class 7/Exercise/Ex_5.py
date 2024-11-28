class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age must be greater than 0")

person = Person(30)
print(person.get_age())
person.set_age(35)
print(person.get_age())