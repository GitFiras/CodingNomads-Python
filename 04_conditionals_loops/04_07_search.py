'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

num = 123
i = 0
x = 1000000000
while i <= x:
    i = i + 1
    if i == num:
        print("Therange includes the inserted number:", i)
        break
