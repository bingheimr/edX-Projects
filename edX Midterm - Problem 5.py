"""
Write a Python function that returns a list
of keys in aDict that map to integer values
that are unique (i.e. values appear exactly
once in aDict). The list of keys you return
should be sorted in increasing order. (If
aDict does not contain any unique values,
you should return an empty list.)

This function takes in a dictionary and returns a list.
"""


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''

    uniqueVals = []

    v = list(aDict.values())
    k = list(aDict.keys())

    for i in range(len(v)):
        tracker = 0
        for x in range(i + 1, len(v)):
            if v[i] == v[x]:
                break
            else:
                tracker += 1
        for y in range(i):
            if v[i] == v[y]:
                break
            else:
                tracker += 1
        if tracker == (len(v) - 1):
            uniqueVals.append(k[i])

    return sorted(uniqueVals)