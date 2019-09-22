'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

for num in range(1,101):
    if num % 2 != 0:                    # if num is not even (% 2 = 0 ), num is odd.
        print(num)