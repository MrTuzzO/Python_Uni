class Circle:
    def __init__(self, r):
        self.pi = 3.1416
        self.r = r

    def area(self):
        return self.pi * self.r ** 2

    @staticmethod
    def form_diameter(d):
        radius = d / 2
        return Circle(radius)


circle = Circle.form_diameter(10)
print(circle.area())
