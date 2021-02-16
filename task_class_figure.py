import math

class Figure(object):
    def get_area(self):
        raise NotImplementedError
        
    def get_perimeter(self):
        raise NotImplementedError


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimeter(self):
        return (self.a + self.b) * 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    
    def get_area(self):
        p2 = (self.a + self.b + self.c) / 2
        return (p2 * (p2 - self.a) * (p2 - self.b) * (p2 - self.c)) ** 0.5


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return (self.r ** 2) * math.pi

    def get_perimeter(self):
        return 2 * math.pi * self.r


num = Rectangle(1, 2)
print(num.get_area())
print(num.get_perimeter())

num2 = Triangle(5, 6, 7)
print(num2.get_area())
print(num2.get_perimeter())

num3 = Circle(10)
print(num3.get_area())
print(num3.get_perimeter())
        





