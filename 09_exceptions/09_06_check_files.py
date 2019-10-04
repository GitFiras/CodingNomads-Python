'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
with open("integers.txt","rt") as num_file:
    first_num = num_file.read()[0]
    print(f'First number is: {first_num}')

    try:
        cal1 = int(first_num) * 5               # int
        cal2 = cal1 + 20
        print(f'Result: {cal2}')
    except IOError as ioerr:                    # not applicable
        print("Something went wrong.")
    except ValueError as valerr:                # not applicable
        print("Wrong value.")