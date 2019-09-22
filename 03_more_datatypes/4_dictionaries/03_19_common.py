'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
# method 1 using +

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

dict_new = {key: dict_1.get(key, 0) + dict_2.get(key, 0)
          for key in set(dict_1) | set(dict_2)}
print(dict_new)

# method 2 using for loop

def new_dict (dict_1, dict_2):
    new_dict = {}

    for key in dict_1:
        if key in dict_2:
            new_value = dict_1[key] + dict_2[key]
        else:
            new_value = dict_1[key]

        new_dict[key] = new_value

    for key in dict_2:
        if key not in new_dict:
            new_dict [key] = dict_2[key]

    return new_dict
print(dict_new)