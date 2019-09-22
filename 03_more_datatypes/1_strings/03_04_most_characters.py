'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

s1 = input("Please type a few words ")
s2 = input("Please type a few more words ")
s3 = input("Please type a another few words ")

list_ = [s1,s2,s3]
print(max(list_,key=len))