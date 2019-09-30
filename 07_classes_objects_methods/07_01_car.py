'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
# 1
class Car:
    '''' Car class with attributes model, year, and max_speed '''
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        print(f'This {self.model} has been built in the year {self.year} and has a maximum speed of {max_speed} km/h.')

# 2
    def speed_up(self):
        """Increases the max_speed of Car by 5."""
        self.max_speed += 5
        print(f'The maximum speed of this {self.model} has increase by 5 km/h to {self.max_speed} km/h.')

# 3
p = Car('Porsche', 1988, 100)
b = Car('BMW', 2019, 220)
m = Car('Mercedes', 1950, 80)

print(p,b,m)            # details of all car objects
p.speed_up()            # increase speed of Car p with 5
print(p.max_speed)
b.speed_up()
print(b.max_speed)

