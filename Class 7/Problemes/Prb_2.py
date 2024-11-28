class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "woof woof woof woof"

dog = Dog()
print(dog.speak())