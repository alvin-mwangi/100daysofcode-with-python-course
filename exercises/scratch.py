'''
returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
'''

# initial/brute force solution:
# get set of numbers
# for each number in set, count how many occurrences appear in the array
# return numbers that occur only once, ordered by index of first occurrence 

# alt solution:
# make a dictionary where key = number, and value = occurrences of that number
# populate dictionary as follows:
# for each value in array:
    # check if dictionary contains entry where key = number
        # if not: add the number to the dictionary, initialize value to 1 (occurrence)
        # if found: increment value (occurrence) for that key in the dictionary
# output all elements in the dictionary where the value = 1 (occurrence)
# issue: dictionary order is not guaranteed; results may be returned in random order
# --- use OrderedDict instead

from collections import OrderedDict


def returnUnique(inputList):
    
    numCountDict = OrderedDict()

    for i in inputList:
        if numCountDict.get(i) == None:
            numCountDict[i] = 1 # this is the first time we've seen this number, initialize count to 1
        else:
            numCountDict[i] += 1 # increment count of occurrences for this number

    #print(numCountDict)

    return [i for i,j in numCountDict.items() if j == 1] # extract the numbers that occurred only once


if __name__ == "__main__":
    print(returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))

