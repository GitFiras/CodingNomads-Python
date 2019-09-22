'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

vowels = ('a','o','i','e','u')
s = input("Please type a few words ")
count = 0
for letter in s:
    if letter in vowels:
        count +=1
print("Number of vowels in the provided input: ", count)

