#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-06'

'''
--- Day 5: A Maze of Twisty Trampolines, All Alike ---

An urgent interrupt arrives from the CPU: it's trapped in a maze of jump instructions, and it would like assistance from any programs with spare cycles to help find the exit.

The message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

How many steps does it take to reach the exit?
'''

inFile = open("5.txt",'r')
instructions = list(map(int,inFile.read().strip().split())) #real input
#instructions = [0,3,0,1,-3] #debug only, should return '5'

steps = 0
index = 0

while index in range(0,len(instructions)):
    value = instructions[index]
    instructions[index] += 1
    index += value
    steps += 1

print ("Number of steps to reach exit: "+ str(steps))
