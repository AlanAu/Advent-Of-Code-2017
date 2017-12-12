#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-12'

'''
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

These instructions would be processed as follows:

    Because a starts at 0, it is not greater than 1, and so b is not modified.
    a is increased by 1 (to 1) because b is less than 5 (it is 0).
    c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
    c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?
'''

inFile = open("8.txt",'r')
instructions = inFile.readlines() #real input
registers = {}

def isTrue (comp, target, val):
    if comp == "==": return (int(target)==int(val))
    elif comp == ">": return (int(target)>int(val))
    elif comp == "<": return (int(target)<int(val))
    elif comp == ">=": return (int(target)>=int(val))
    elif comp == "<=": return (int(target)<=int(val))
    elif comp == "!=": return (int(target)!=int(val))
    else: print("Oops, you shouldn't be seeing this.",target,comp,val)
        
for line in instructions:
    inst = line.strip().split()
    reg, command, amount, ignore, target, comp, val = inst
    if reg not in registers: registers[reg] = 0
    if target not in registers: registers[target] = 0

    if isTrue(comp, registers[target], val):
        if command == "dec": registers[reg] -= int(amount)
        elif command == "inc": registers[reg] += int(amount)
 
regMax = 0
for reg in registers:
    currReg = registers[reg]
    if currReg > regMax: regMax = currReg
print("The largest value in any register is: "+str(regMax))  
