'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''
# sort numbers
numbers_ = [ 1, 5, 4, 67, 88, 99, 3, 2, 12]
numbers_.sort()
print(numbers_)

# check for odd numbers         use % to check: 0 = even, 1 is odd
x = len(numbers_)
if x % 2 == 1:
    numbers_.append(0)          # add '0' to the list, because list  is odd

# sort numbers in tuples of two in a list
list_numbers = []

# print(numbers_[::2])                              steps of 2, starting at the start of the list
for i in range(0,len(numbers_),2):                  # range start at start of list, till end of list, by steps of 2
    j = tuple(numbers_[i:i+2])                      # turn the 2 numbers into tuples
    list_numbers.append(j)                          # append new numbers to new list
print(list_numbers)
