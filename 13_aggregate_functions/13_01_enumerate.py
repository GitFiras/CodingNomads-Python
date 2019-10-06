'''
Demonstrate the use of the .enumerate() function.
'''

courses = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

course_list = enumerate(courses)
print(f'This is the output of the enumerate function: {list(course_list)}')