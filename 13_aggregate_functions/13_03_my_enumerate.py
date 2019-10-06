'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate():
    index = 0
    value_list = ['apple', 'banana', 'pineapple', 'orange', 'grape']    # list
    for value in value_list:                                            # loop for values in list
        index += 1                                                      # increase index by 1 with each value
        yield index -1, value                                           # yield output: index, value
print(list(my_enumerate()))                                             # call function and print in list