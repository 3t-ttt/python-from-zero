from math import pi
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self, radius):
        c = 2 * pi * radius
        return c

    def calculate_area(self, radius):
        a = pi * (radius**2)
        return a

r = input("Enter radius: ")
c1 = Circle(r)
c1.calculate_circumference(r)
c1.calculate_area(r)
print(r)