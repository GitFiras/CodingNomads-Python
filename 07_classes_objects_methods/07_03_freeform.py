'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''

class Glass:
    '''class of Glass with attributes of a glass'''
    def __init__(self,glass_shape,glass_colour,glass_temperature):
        self.glass_shape = glass_shape
        self.glass_colour = glass_colour
        self.glass_temperature = glass_temperature
        print(f'This {Glass} is {glass_shape}, {self.glass_colour} and is best used {self.glass_temperature}')

    def __str__(self):
        return f'This {Glass} is {glass_shape}, {self.glass_colour} and is best used {self.glass_temperature}'

    def Drink(self,temperature,colour,flavour,mixable):
        self.temperature = temperature
        self.colour = colour
        self.flavour = flavour
        self.mixable = mixable

    def Serving(self,coaster,plate,with_food):
        self.coaster = coaster
        self.plate = plate
        self.with_food = with_food

    # additonal object
    # def User(self,age,mood,personality):
    #     self.age = age
    #     self.mood = mood
    #     self.personality = personality

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

