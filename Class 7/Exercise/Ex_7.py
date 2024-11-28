class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f'Car(make= {self.make} , model= {self.model}, year= {self.year})'

car = Car('Tesla', 'Model S', '2020')
print(car)