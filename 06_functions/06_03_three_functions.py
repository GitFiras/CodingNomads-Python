'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
user_input = input("Hello, type 'hi' to start. ")
name_input = input("Hi there! What's your name? ")

def hello():
    user_input.isupper()
    greeting = "Hello there!"
    return greeting

def person():
    hello()
    my_name = []
    for letter in name_input:
        my_name.append(letter.upper())
        your_name = tuple(my_name)
        personal_greeting = hello(), name_input.upper(), " let me spell your name: ", your_name
    return personal_greeting

def thank_you():
    name_input.isupper()
    greeting2 = tuple(person()), f'Thank you {name_input}. This was it.'
    return greeting2

thank_you()
print(thank_you())
