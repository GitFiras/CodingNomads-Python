'''
Take two numbers from the user, an upper and lower bound.
Using a loop, calculate the sum of all numbers from the lower bound to the upper bound.

For example, if a user enters 1 and 100, the output should be:

The sum is: 5050
'''

num1 = 1
num2 = 12
sum_nums = 0
for num in range(num1, num2+1):
    sum_nums = sum_nums + num
print("The sum of the range between the two numbers is: ", str(sum_nums))