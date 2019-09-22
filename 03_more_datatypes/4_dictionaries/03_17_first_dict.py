'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

d=dict()
for x in range(1,11):
    d[x]=x**2
print(d)