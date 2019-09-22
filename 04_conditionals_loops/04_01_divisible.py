'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
num = int(input('Please provide a number between 1 and 1,000,000,000: '))
if num % 3 == 0:                                # if output is 0, the number can be divided by 3 without residual value.
    print(int(num/3))
else:
    print("Your number cannot be divided by 3, please insert another number")
