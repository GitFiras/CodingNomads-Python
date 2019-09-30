'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        area_rec = self.length * self.width
        print(f'The area of a rectangle is length: {self.length} multiplied by width: {self.width}, being: {self.length*self.width}')
        return area_rec

    def perimeter_rectangle(self):
        perimeter_rec = (2 * (self.length + self.width))
        print(f'The perimeter of a rectangle is two times the sum of the length: {self.length} plus the width: {self.width}, being: {2* (self.length + self.width)}')
        return perimeter_rec

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        area_circ = math.pi * (self.radius * self.radius)
        print(f'The area of a circle is pi: {math.pi} multiplied by the square of the radius: {self.radius}, being: {math.pi * (self.radius * self.radius)}')
        return area_circ

    def circumference_circle(self):
        circumference_circ = 2 * math.pi * self.radius
        print(f'The circumference of a circle is two times pi: {math.pi} multiplied by the radius: {self.radius}, being: {2 * math.pi * self.radius}')
        return circumference_circ


p = Rectangle(1.2,4.2)
r = Rectangle(4,6)
print(p.area_rectangle())
print(r.perimeter_rectangle())

q = Circle(2.5)
e = Circle(1)
m = Circle(5)
print(q.area_circle())
print(m.circumference_circle())