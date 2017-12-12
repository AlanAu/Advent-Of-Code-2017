#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-12'

'''
--- Part Two ---

To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).
'''

inFile = open("8.txt",'r')
instructions = inFile.readlines() #real input
registers = {}
regMax = 0

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
    currReg = registers[reg]
    if currReg > regMax: regMax = currReg
 
print("The largest value in any register at any time was: "+str(regMax))  
