'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

while True:
    try:
        user_input = input("Please provide a number value: ")
        int_input = (int(user_input))
        if user_input == int:
           print(f'Your input {user_input} was correct.')
        break                                                       # break if correct
    except ValueError as val_err:
        print(f'Your input {user_input} was not a number value. Please try again.')