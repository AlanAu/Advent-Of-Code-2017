#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-12'

'''
--- Part Two ---

Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the garbage. The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

    <>, 0 characters.
    <random characters>, 17 characters.
    <<<<>, 3 characters.
    <{!>}>, 2 characters.
    <!!>, 0 characters.
    <!!!>>, 0 characters.
    <{o"i!a,<{i<a>, 10 characters.

How many non-canceled characters are within the garbage in your puzzle input?
'''

inFile = open("9.txt",'r')
groups = inFile.read() #real input

i = 0;
score = 0
garbage = False

while i < len(groups.strip()):
    curr = groups[i]
    i += 1
    if curr == '!': 
        i += 1
    elif curr == '<' and not garbage:
        garbage = True
    elif curr == '>' and garbage:
        garbage = False
    elif garbage:
        score += 1
print("Total number of garbage characters is: "+str(score))
