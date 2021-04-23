"""
Write a function that satisfies the following docstring:

def largest_odd_times(L):
    ''' Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None '''
"""

def largest_odd_times(L):
    """
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number
    of times in L. If no such element exists, returns None
    """
    temp = set(L)
    while len(temp) > 0:
        res = max(temp)
        if (L.count(res) % 2) != 0:
            return res
        else:
            temp.remove(res)