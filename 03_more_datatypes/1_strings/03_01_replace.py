'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

words = input("Please write a number of words, separated by commas ")
symbol = input("Please insert 1 symbol of choice ")
words2 = words[0] + words[1:].replace(words[0], "*")
print(words2)
