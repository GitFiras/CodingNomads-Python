'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

# method 1: using max:
text = 'hello hi hi hi' 									#  input string
split_text = text.split()									# split string
print((max(split_text))) 									# to find most frequent element in a list

# method 2: using for loop:									# counting the number of words in a dict, no max counter.
seen_list = {}
for word in split_text:
	if word not in seen_list:
		seen_list[word] = 1
	else:
		seen_list[word] += 1
print(seen_list)