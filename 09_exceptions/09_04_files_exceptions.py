'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
# Use 'os.walk' for looping through files

'''# 1 open war_and_peace.text and read file, store file content to variable'''
with open(r"C:\Users\firas\PycharmProjects\python_fundamentals\09_exceptions\books\war_and_peace.txt",encoding="utf8") as file_w_p:
    content_w_p = file_w_p.read()           # file content to variable. Not working

'''# 2 open crime_and_punishment.txt, overwrite while content with empty string. WORKING'''
with open("crime_and_punishment.txt","w") as file_c_p:
    file_c_p.write("")

'''# 3 print first character from all 3 txt files. Not to terminate.'''

with open(r"C:\Users\firas\PycharmProjects\python_fundamentals\09_exceptions\books\war_and_peace.txt",encoding="utf8") as file_w_p:
    print(f'{file_w_p.read()[1]}')

with open(r"C:\Users\firas\PycharmProjects\python_fundamentals\09_exceptions\books\crime_and_punishment copy.txt",encoding="utf8") as file_c_p:
    print(f'{file_c_p.read()[1]}')

with open(r"C:\Users\firas\PycharmProjects\python_fundamentals\09_exceptions\books\pride_and_prejudice.txt",encoding="utf8") as file_p_p:
    print(f'{file_p_p.read()[1]}')


# File "/09_exceptions/09_04_files_exceptions.py", line 63
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 244-245: truncated \UXXXXXXXX escape
# Process finished with exit code 1
