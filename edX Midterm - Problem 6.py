"""
Create Function to implement following docstring details.
"""

def max_val(t):
    """
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t
    """

    maxNum = []
    for i in t:
        if isinstance(i, int):
            maxNum.append(i)
        else:
            maxNum.append(max_val(i))

    return max(maxNum)