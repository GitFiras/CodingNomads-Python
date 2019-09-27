'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
print("Assignment 1 - Method 1:")

def div_by_4_or_7(x):
    if x % 4 == 0:
        print(f"{x} is divisible by 4: ",True)              # boolean True if function returns True
        return True
    elif x % 7 == 0:
        print(f"{x} is divisible by 7: ",True)              # boolean True if function returns True
        return True
    else:
        print(f"{x} is divisible by 4 or 7: ",False)        # boolean False if function returns False
        return False

var = div_by_4_or_7(7)                                      # calling the function with variable input = 7
print(var)

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

print("Assignment 2")

def div_by_4_and_7(z):
    if z % 4 == 0 and z % 7 == 0:
        print(f'{z} is divisible by 4 and 7: {True}')
        return True
    else:
        print(f"{z} is not divisible by 4 and 7: ",False)
        return False

var2 = div_by_4_and_7(28)                                   # calling the function with variable input = 28
print("divisible by 4 and 7: ",var2)

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
num = 0
# while num != 100:                 # optional while loop
num = int(input("Please insert a number between 1 and 1,000,000,000: "))        # user input INT
div_by_4_or_7(num)                                                              # calling function with input = num
div_by_4_and_7(num)                                                             # calling function with input = num

# print your new variables to display the results
xx = div_by_4_or_7(num)                                                         # new variable based on function
yy = div_by_4_and_7(num)                                                        # new variable based on function
print("div_by_4_or_7",xx)
print("div_by_4_and_7",yy)
