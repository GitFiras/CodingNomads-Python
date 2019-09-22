'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1}
list_ = []

# Iteration from dict to list with tuples
for i in input_dict:
    j = (i, input_dict[i])
    list_.append(j)
print(list_)
print(sorted(list_, key =  lambda sorted_number : sorted_number[1]))        # sort by the number of index 1 [1].