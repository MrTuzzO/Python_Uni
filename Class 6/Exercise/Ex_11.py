class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed increased to {self.speed}")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"Speed decreased to {self.speed}")


car = Vehicle("BMW", 100)
car.accelerate(50)
car.brake(100)