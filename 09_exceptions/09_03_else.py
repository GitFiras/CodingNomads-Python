'''
Write a script that demonstrates a try/except/else.

'''

while True:
    try:
        input_ = int(input("Please provide a number higher than 1: "))
        calc_ = input_ + 100
        if input_ < int(1):
            print("This number is too low. Please provide a higher number.")
            print(input_)
    except IndexError as ind_err:
        print("Please provide a different input.")
    except ValueError as val_err:
        print("Please provide a number.")
    else:
        print(calc_)