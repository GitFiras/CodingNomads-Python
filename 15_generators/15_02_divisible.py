'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
my_list = range(1,100000)
generator = (num for num in my_list if num % 1111 == 0)
print(list(generator))
