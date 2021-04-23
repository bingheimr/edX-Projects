"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring
of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program
should print: 'Longest substring in alphabetical order is: beggh'

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print:'
Longest substring in alphabetical order is: abc'
"""

s = 'azcbobobegghakl'

longstring = s[0]
mystring = longstring

for i in range (1, len(s)):
    if s[i] >= mystring[-1]:
        mystring += s[i]
        if len(mystring) > len(longstring):
            longstring = mystring
    else:
        mystring = s[i]

print('Longest substring in alphabetical order is: ' + longstring)