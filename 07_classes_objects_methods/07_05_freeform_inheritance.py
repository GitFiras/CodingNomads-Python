'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Glass:
    '''class of Glass with attributes of a glass'''
    def __init__(self,glass_shape,glass_colour,glass_temperature):
        self.glass_shape = glass_shape
        self.glass_colour = glass_colour
        self.glass_temperature = glass_temperature
        print(f'This glass is {glass_shape}, {self.glass_colour} and is best used {self.glass_temperature}')

    def __str__(self,glass_shape):
        return f'This glass is {glass_shape}, {self.glass_colour} and is best used {self.glass_temperature}'

    def Drink(self,temperature,colour,flavour,mixable):
        self.temperature = temperature
        self.colour = colour
        self.flavour = flavour
        self.mixable = mixable

    def Serving(self,coaster,plate,with_food):
        self.coaster = coaster
        self.plate = plate
        self.with_food = with_food

p = Glass('round','blue','cold')
print('The shape of the glass is: ',p.glass_shape)
print(Glass)
print(p.Drink)

class Plate(Glass):
    '''class of a plate, with attributes of a plate for food'''
    def __init__(self,plate_shape,plate_colour):
        super().__init__(self)
        self.plate_shape = plate_shape
        self.plate_colour = plate_colour

    def __str__(self):
        return f'This {Plate} is {self.plate_shape} and {self.plate_colour}.'

    def content(self,food,snacks,decoration):
        self.food = food
        self.snacks = snacks
        self.decoration = decoration

    def Used_in(self,time_of_day,location,servant):
        self.time_of_day = time_of_day
        self.location = location
        self.servant = servant

    def __add__(self, other):
        pass

class Place:
    '''class of place, with attributes of a location with regard to the classes of glass, drink, plate'''
    def __init__(self,location,number_of_people):
        self.location = location
        self.number_of_people = number_of_people

    def __str__(self):
        return f'This {Place} is located in {self.location}, and fits {self.number_of_people}.'

    def Room(self, light_intensity,capacity,noise):
        self.light_intensity = light_intensity
        self.capacity = capacity
        self.noise = noise

    def Ambience(self,temperature,music,smell):
        self.temperature = temperature
        self.music = music
        self.smell = smell

# NEW SUB CLASS
class Restaurant(Glass):
    def __init__(self,glass_shape,glass_colour,glass_temperature,service,waiting_time,compliments):
        super().__init__(self,glass_shape,glass_colour)
    def waiter(self,capacity,noise,light_intensity,temperature,smell,service,waiting_time,compliments):
        print(f'The waiter will seat you in a {capacity} and {noise} room with {light_intensity},  a {temperature} atmosphere, and an {smell} smell it is.')

r = Restaurant('round','transparent','cold','excellent service','1 minute','Looking sharp tonight!')
print(r)
print(r.service)