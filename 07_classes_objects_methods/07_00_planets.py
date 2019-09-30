'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self,name,colour,system):
        self.name = name
        self.colour = colour
        self.system = system

e = Planet('Earth', 'blue', 'Milkyway')
m = Planet('Mars','red','Milkyway')
j = Planet('Jupiter','orange','Milkyway')
print(f'{e.name} is a planet that is {e.colour} in the {e.system}')
print(f'{m.name} is a planet that is {m.colour} in the {m.system}')
print(f'{j.name} is a planet that is {j.colour} in the {j.system}')



