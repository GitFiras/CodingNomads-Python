'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
my_list = range(1,100000)
generator = (num for num in my_list if num % 1111 == 0)
floor_gen = [num // 1111 for num in generator]
print(floor_gen)