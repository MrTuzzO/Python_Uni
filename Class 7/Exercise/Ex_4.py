class Animal:
    def sound(self):
        return "Some generic animal sound"


class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())