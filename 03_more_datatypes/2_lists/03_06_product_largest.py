'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''


numbers = input("Please insert ten numbers separated by commas ")
numbers = numbers.split(',')  # splits values into a list
print(type(numbers))

int_numbers = []                                # list for integers of number conversion
for num in numbers:                             # For loop
    int_numbers.append(int(num))                # append to list
print(int_numbers)
print("Max number of the list ", max(int_numbers))

# product of numbers in list
num_list = int_numbers
product = 1
for num_int in num_list:
    product *= num_int                        # *= is i = i * num_int
print("Product of numbers in list is: ", product)

