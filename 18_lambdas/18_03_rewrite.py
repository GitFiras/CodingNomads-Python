'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

print([x.startswith('D') for x in names])

name_list = list(filter(lambda x: (x.startswith('D')),names))
print(name_list)
