'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

num_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list):
    '''function notes:
    function to take list of numbers and find the max, min, average and sum of the list numbers.
    Argument is num_list of numbers.
    Returns values of function.
    '''
  # define the function here
    max_ = max(example_list)
    min_ = min(example_list)
    average_ = (sum(example_list)/len(example_list))
    sum_ = sum(example_list)
    return [max_,min_,average_,sum_]

# call the function below here
print("method 1: assigned to 1 variable: ")
a = stats(num_list)               # put values in variables when assigned to variable separated by comma
print(a)                          # printed as list

print("method 2: assigned to separate variables, packed in tuples: ")
a,b,c,d = stats(num_list)               # put values in variables when assigned to variable separated by comma
print(f'The max value is: {a}, the min value is: {b}, the average value is: {c}, and the sum is: {d}')
# packing in tuples by default, printed as values when return is 'listed'