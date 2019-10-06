'''
Write a script with a function that demonstrates the use of *args.

'''

def hello(*greeting):
    for item in greeting:
        print(greeting)
hello('hi, hello')