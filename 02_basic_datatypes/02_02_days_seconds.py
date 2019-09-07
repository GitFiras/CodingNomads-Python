'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() funtion to collect users input. An example is demonstrated below.

'''

# the input of the user will be saved in the variable days.
# because the input() function collects the input as a string, we have to convert it to an int
# The string passed to the input() function is what the user is prompted with
# days = int(input("Please enter a number in days between 1 and 1,000,000,000: "))

# script to convert user input in number of days to number of seconds
# User input =  number of days
# Output is  number of days in seconds =  input amount of days * amount of seconds per day
# amount of seconds per day = seconds per minute * minutes per hour * hours per day = 60 * 60 * 24

days = int(input("Please insert a number of days between 1 and 1,000,000,000: "))
#days = int(days)
sec  = 60 * 60 * 24
print("amount of seconds in amount of days inserted:")
print(days * sec)

