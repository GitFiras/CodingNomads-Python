'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

#Not working
words = input("Please write a number of words ")
input_letter = input("Please insert 1 letter of choice that occurs in 1 of more words ")
index = 0

#index = words.find(input_letter)
#print ("the index of your letter is: ", index)

i = 0
#For Loop method:
for letter in words:
    print(letter)
    if input_letter == letter:
        index = i
        break
    i += 1
print("the index of your letter is: ", index)


#for index, letter in enumerate(words):
 #   if letter == '':
  #      letter.append(i)

