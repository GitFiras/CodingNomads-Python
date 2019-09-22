'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 'hello', 'welcome', 4, 4, 6, 8, 'to', 'to', 'python', 3]
print("The original list is: ", str(list_))
list_unique = list(dict.fromkeys(list_))
print("Unique list values are: ", list_unique)
