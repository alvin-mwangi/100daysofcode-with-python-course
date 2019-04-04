# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# # double each value in the dictionary
# double_dict1 = {k:v*2 for (k,v) in dict1.items()}

# print(dict1)
# print(double_dict1)

# #change the keys
# dict1_keys = {k*2:v for (k, v) in dict1.items()}

# print(dict1_keys)

# create dictionary where the key is a number divisible by 2 in a range of 0-10
# and its value is the square of the number

# outputDict = {i:i**2 for i in range(11) if i % 2 == 0}
# print(outputDict)





bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
exclude_bites = {6, 10, 16, 18, 21}


def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return {k:v for (k,v) in bites.items() if k not in exclude_bites}

print(bites)
print(filter_bites())


