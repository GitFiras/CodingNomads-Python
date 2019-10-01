'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

# filename = words.txt
# file location on drive = C:\Users\firas\PycharmProjects\python_fundamentals\08_file_io
# file_open = open('C:\Users\firas\PycharmProjects\python_fundamentals\08_file_io\words.txt','r')

file_open = open('words.txt','r')
# print(file_open.read())         # open and read file


def shortest():
    short_ = []
    for word in file_open:
        if len(word) == min(len(str(file_open))):             # if length of current sub string is minimum
            res = len(file_open.split())
            short_.append(word)                          # append  sub string in short list
        print(short_)


def longest():
    longest_ = []
    for word in file_open:
        string = []                 # empty string
        text = str.split("\n")       # split string at spaces
        print(text)

        if len(word) == max(len(str(file_open))):            # if length of current sub string is maximum
            shortest_.append(word)                          # append  sub string in long list
        print(shortest_)


def total_words():
    num_words = 0
    with open('file_open', 'r') as file:
        for word in file_open:
            words = word.split()
            num_words += len(words)
    print("Number of words:")
    print(num_words)
