'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

Fahrenheit = float(input("Please insert a value of Fahrenheit between 32 and 212"))
Celsius = float((Fahrenheit - 32) * ( 5 / 9))
print(round(Fahrenheit, 2), end= '')
print(" degrees fahrenheit = ", end= '')
print(round(Celsius, 1), end='')
print(" degrees Celsius")
