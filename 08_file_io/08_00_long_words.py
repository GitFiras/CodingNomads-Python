'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

# filename = words.txt
# file location on drive = C:\Users\firas\PycharmProjects\python_fundamentals\08_file_io
# file_open = open('C:\Users\firas\PycharmProjects\python_fundamentals\08_file_io\words.txt','r')

file_open = open('words.txt','r')
# print(file_open.read())         # open and read file


def long():
    long_ = []
    for word in file_open:
        string = []                 # empty string list
        # text = str.split("\n")       # split string at spaces
        # print(text)
        if len(word)>=20:             # if length of current sub string is greater than 20 then
            long_.append(word)         # append sub string in long list
            print(long_)

        print(long_)