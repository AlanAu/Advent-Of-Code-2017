#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-12'

'''
--- Day 9: Stream Processing ---

A large stream blocks your path. According to the locals, it's not safe to cross the stream at the moment because it's full of garbage. You look down at the stream; rather than water, you discover that it's a stream of characters.

You sit for a while and record part of the stream (your puzzle input). The characters represent groups - sequences that begin with { and end with }. Within a group, there are zero or more other things, separated by commas: either another group or garbage. Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. Your puzzle input represents a single, large group which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, some program has canceled some of the characters within it using !: inside garbage, any character that comes after ! should be garbaged, including <, >, and even another !.

You don't see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, and garbage always terminates according to the rules above.

Your goal is to find the total score for all groups in your input. Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

    {}, score of 1.
    {{{}}}, score of 1 + 2 + 3 = 6.
    {{},{}}, score of 1 + 2 + 2 = 5.

What is the total score for all groups in your input?
'''

inFile = open("9.txt",'r')
groups = inFile.read() #real input
#groups = "{}" #debug, should output 1
#groups = "{{{}}}" #debug, should output 6
#groups = "{{},{}}" #debug, should output 5

i = 0;
level = 0
score = 0
garbage = False

while i < len(groups.strip()):
    curr = groups[i]
    if curr == '!': 
        i += 1
    elif curr == '<' and not garbage:
        garbage = True
    elif curr == '>' and garbage:
        garbage = False
    elif curr == '{' and not garbage:
        level += 1
        score += level
    elif curr == '}' and not garbage:
        level -= 1
    i += 1
print("Total score is: "+str(score))
