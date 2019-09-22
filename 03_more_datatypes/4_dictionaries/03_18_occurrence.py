'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

string_ = input("Insert a few words here: ")
print(string_)
letter_freq = {}
for i in string_:
    if i in letter_freq:
        letter_freq[i] += 1
    else:
        letter_freq[i] = 1
print ("Count of all characters is :\n "
                                        +  str(letter_freq))