class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print(f"{self.name} Bark")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} Meow")

cat = Cat("Cat")
dog = Dog("Dog")

cat.sound()
dog.sound()