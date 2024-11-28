class Ractangle:
    def __init__(self , lenght,weight):
        self.lenght = lenght
        self.weight = weight

    def area(self):
        return self.lenght*self.weight

    def perimeter(self):
        return 2* (self.lenght+self.weight)


ract = Ractangle(10,5)
print(ract.area())
print(ract.perimeter())
