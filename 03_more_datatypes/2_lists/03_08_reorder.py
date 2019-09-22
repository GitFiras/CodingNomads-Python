'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

#num = input("Please provide 10 numbers: ")
#x = num.split()
#print(x)

#list_ = list(map(int,num.split()))                  # split user input, make int, make into list
#print(list_)

list_2 = [1,2,3,4,5,6,7,8,9,10]
print(list_2)

x = list_2[1::2]                                    # starting at 2nd value, step size of 2
y = list_2[-2::-2]                                  # starting at the back of list. 1 before end, step  size of 2
print(x + y)
