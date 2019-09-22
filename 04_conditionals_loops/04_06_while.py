'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

num = 0
list_fifth_nums = []
while num <= 1000:
    if num % 5 == 0:
        list_fifth_nums.append(num)
        num += 5
print(list_fifth_nums)