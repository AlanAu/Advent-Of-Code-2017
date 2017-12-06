#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-06'

'''
--- Day 6: Memory Reallocation ---

A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that has been seen before.

Given the initial block counts in your puzzle input, how many redistribution cycles must be completed before a configuration is produced that has been seen before?
'''

inFile = open("6.txt",'r')
banks = list(map(int,inFile.read().strip().split())) #real input
#banks = [0,2,7,0] #debug only, should return '5'

cycles = 0
bank_dict = {}
bank_len = len(banks) 

while True:
    #check for duplicate state
    bank_str = ' '.join(list(map(str,banks)))
    if bank_str in bank_dict:
        break
    else:
        bank_dict[bank_str] = True

    #get max value and its index
    max_value = max(banks)
    ind = banks.index(max_value)
    
    #redistribute
    banks[ind] = 0
    while max_value > 0:
        max_value -= 1
        ind = (ind+1)%bank_len
        banks[ind] += 1
    cycles += 1
        
print ("Number of cycles before a repeat: "+ str(cycles))
