# Python Program to Merge Two Dictionaries
# In this example, you will learn to merge two dictionaries into one in Python programming.

# using the | Operator

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
print(dict_1 | dict_2)

# using the ** operator. but this ocde will work with python 3.5 and 3.6. to know more about **kwargs  
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
# print({dict_1,  **dict_2})


# using copy() and Update()

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
dict_3 = dict_2.copy()
dict_3.update(dict_1)
print(dict_3)