#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-06'

'''
--- Part Two ---

Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?
'''

inFile = open("6.txt",'r')
banks = list(map(int,inFile.read().strip().split())) #real input
#banks = [2,4,1,2] #debug only, should return '4'

cycles = 0
duplicate = 0
bank_dict = {}
bank_len = len(banks) 

while True:
    #check for duplicate state
    bank_str = ' '.join(list(map(str,banks)))
    if bank_str in bank_dict:
        if bank_dict[bank_str] > 1:
            break
        else:
            bank_dict[bank_str] += 1
            if duplicate == 0:
                duplicate = cycles
    else:
        bank_dict[bank_str] = 1

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
        
print ("Number of cycles before a repeat: "+ str(cycles-duplicate))
