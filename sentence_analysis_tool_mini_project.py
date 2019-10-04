# Sentence Analysis Tool
# Write a script that takes a sentence from the user and returns:
#
# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

sentence = input("Please write a sentence ")
# lowercaselettercount = {w:len(w) for w in words}

#method 1:
# the number of lower case letters
#print("Number of lower case letters in the sentence is: ", sum(1 for c in sentence if c.islower()))
# method 2:
lower_counter = 0
upper_counter = 0
for c in sentence:
    if c.islower():
        lower_counter += 1
    if c.isupper():
        upper_counter += 1
print("Number of lower case & upper letters in the sentence is: ", lower_counter, upper_counter)



# the number of uppercase letters
print("Number of upper case letters in the sentence is: ", sum(1 for c in sentence if c.isupper()))

# the number of punctuation
special_list = ["!",","," \ ",".","?","-"]
count = 0;
for character in sentence:                              # for loop to look up in list or tuple
    if character in special_list:                       # membership test =  True / False
        count = count + 1
print("Number of punctuations in the sentence is: ", count)

# the total number of characters
print("Number of characters in the sentence is: ", len(sentence))