'''

Write a script that removes all duplicates from a list.

'''

# method 1: use set
list_ = [1, 2, 3, 4, 3, 5, 6, 4, 5]
list_ = set(list_) # make list into set (removes duplicates automatically: unordered unique elements)
list_ = list(list_) # make set into list
print(list_)

# method 2: list(dict.fromkeys(list_))

# method 3: executed with 'For loop'
list_ = [1, 2, 3, 4, 3, 5, 6, 4, 5]
list_unique = []
for num in list_:
    if num not in list_unique:
        list_unique.append(num)
list_ = list_unique
print(list_)