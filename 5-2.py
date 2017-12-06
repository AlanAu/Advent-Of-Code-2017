#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-06'

'''
--- Part Two ---

Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
'''

inFile = open("5.txt",'r')
instructions = list(map(int,inFile.read().strip().split())) #real input
#instructions = [0,3,0,1,-3] #debug only, should return '10'

steps = 0
index = 0

while index in range(0,len(instructions)):
    value = instructions[index]
    if value > 2:
        instructions[index] -= 1
    else:
        instructions[index] += 1
    index += value
    steps += 1

print ("Number of steps to reach exit: "+ str(steps))
