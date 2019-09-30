'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''

#1 & 2
class Movie:
    def __init__(self, year,title):
        self.year = year
        self.title = title
        print(f'This movie was released in {self.year} and was called {self.title}.')

m = Movie(2019,'comedy')
print(m)
print(m.year)
print(m.title)


#3
class RomCom(Movie):
    def __init__(self,actor,humour):
#        super().__init__(self, year,title)
        self.actor = actor
        self.humour = humour


mov = RomCom('John T.','slapstick')
print(mov.actor)
print(mov.humour)
print(f'This RomCom stars {mov.actor} with a sense of {mov.humour} humour.')


#4: overwrite dunder of Movie, add instance variable 'pg' = 13 default value
class ActionMovie(Movie):
    def __init__(self,year,title,pg=13):
        self.pg = pg
        print(f'This movie was released in {year} and was called {title}, with a pg of {pg}.')

new = ActionMovie(2018,'GoGoGo')
print(new.pg)

