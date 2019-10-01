'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

# filename = words.txt
# file location on drive = C:\Users\firas\PycharmProjects\python_fundamentals\08_file_io
# file_open = open('C:\Users\firas\PycharmProjects\python_fundamentals\08_file_io\words.txt','r')

file_open = open('words.txt','r')
# print(file_open.read())         # open and read file

# Function to reverse words of string

def reverseWords(file_open):
    word_list = file_open.split("\n")                           # split words of string separated by new line

    word_list = word_list[-1::-1]                           # reverse list of words, # start from last element, 2: move to end of list, 3: difference of steps
    output = '\n'.join(word_list)                           # join words with new line

    if __name__ == "__main__":
        input = 'hello'
        print(reverseWords(file_open))

    return output

reverseWords(file_open)