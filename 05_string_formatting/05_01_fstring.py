'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]
# 1: split values of 'full_name' dict key into 'last_name' and 'first_name' values
# 2: print dict values {"quote"}" - "{last_name}", "{first_name}
# Solution direction: print(f'(famous_quotes{"quote"}, " - ","{last_name}", "{first_name}"' in famous_quotes)

for dict in famous_quotes:
    name = dict["full_name"].split()
#    print("'",dict["quote"],"'",'-',name[1],",",name[0])       # alternative method
    if len(name) == 3:
        print(f'"{dict["quote"]}" - {name[2]}, {name[0]} {name[1]}')
    else:
        print(f'"{dict["quote"]}" - {name[1]}, {name[0]}')


'''
#alternative method : for loop to enter dict values
for dict in famous_quotes:
    print(dict["quote"]," - ", dict["full_name"].split())
'''

'''
#alternative method :
quote1 = famous_quotes[0]
quote2 = famous_quotes[1]
quote3 = famous_quotes[2]
quote4 = famous_quotes[3]
quote5 = famous_quotes[4]
quote6 = famous_quotes[5]
quote7 = famous_quotes[6]

print(f'{quote1["quote"]} - {quote1["full_name"]}')
print(f'{quote2["quote"]} - {quote2["full_name"]}')
print(f'{quote3["quote"]} - {quote3["full_name"]}')
print(f'{quote4["quote"]} - {quote4["full_name"]}')
print(f'{quote5["quote"]} - {quote5["full_name"]}')
print(f'{quote6["quote"]} - {quote6["full_name"]}')
print(f'{quote7["quote"]} - {quote7["full_name"]}')
'''