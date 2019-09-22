'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

# num = int(input("Please provide a number: "))         # user input
num = 11                                                 # fixed input value for assignment
months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
if num in months_dict:
    print("The number you have inserted corresponds with the month of: ", months_dict[num])
else:
    print("Other")