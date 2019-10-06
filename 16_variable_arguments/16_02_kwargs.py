'''
Write a script with a function that demonstrates the use of **kwargs.

'''
def destinations(**holidays):
    for country,city in holidays.items():
        print(country,city)
destinations(Europe='France', Asia='Indonesia')
