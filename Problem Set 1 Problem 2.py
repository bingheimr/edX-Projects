"""
Assume s is a string of lower case characters.

Write a program that prints the number of times
the string 'bob' occurs in s.

For example, if s = 'azcbobobegghakl', then your
program should print: Number of times bob occurs is: 2
"""
s = 'azcbobobegghakl'
counter = 0


for i in range(0, len(s)-2):
    if s[i] == 'b':
        if s[i+1] == 'o':
            if s[i+2] == 'b':
                counter += 1
            else:
                continue

print("Number of times bob occurs is: " + str(counter))
