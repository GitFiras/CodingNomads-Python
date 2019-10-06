'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

new_gen_object = (num for num in range(10))
print(list(new_gen_object))