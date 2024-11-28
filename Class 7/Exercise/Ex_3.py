class Vehicle:
    def start(self):
        print("Vehicle Starting")


class Car(Vehicle):
    def start(self):
        print("Car is Starting")

car = Car()
car.start()