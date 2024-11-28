class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)
        self.payload_capacity = payload_capacity

    def get_details(self):
        return f"Make: {self.make}, Model: {self.model}, Payload Capacity: {self.payload_capacity}"


truck = Truck("Ford", "F-150", 3000)
print(truck.get_details())
