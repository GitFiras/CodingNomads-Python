'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

while True:
    try:
        input_1 = int(input("Please insert a number for a quotient calculation: "))
        input_2 = int(input("Please insert a second number for this calculation: "))
        cal_ = input_1 / input_2
    except ValueError as valer:
        print("The provided input was not a valid number. Please insert a number.")

    except ZeroDivisionError as zerodiv:
        print("The provided input was zero. Cannot divide by zero. Please insert a number above zero for the second number.")
    else:
        print(cal_)
