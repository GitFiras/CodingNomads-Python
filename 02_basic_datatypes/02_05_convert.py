'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
num = input("Insert a number between 1 and 100 : ") # number as input
num = int(num) # number as integer
print("Inserted number is: ", end='')
print(num)
print("Inserted number as float is: ", end='')
num = float(num) # 1) input conversion from integer to float
print(num)

num2 = input("Insert a number between 1.0 and 100.0 : ") # number as input
num2 = float(num2)
print("Inserted number as integer is: ", end='')
num2 = int(num2) # 2) input conversion from integer to float
print(num2)



print("Inserted number divided by 5 is: ", end='')
print(num2 / (int(5))) # 3) division float and int

print("Inserted number 1 multiplied by inserted number 2 is: ", end='')
print(num * num2) # 4) Multiplicaiton of two input values. Note: decimals of floating input values are lost during conversions.

