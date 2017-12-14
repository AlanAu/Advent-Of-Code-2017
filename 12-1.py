#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-13'

'''
--- Day 12: Digital Plumber ---

Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

How many programs are in the group that contains program ID 0?
'''

inFile = open("12.txt",'r')
pipes = inFile.readlines() #real input


pipe_hash = {}
for pipe in pipes:
    data = pipe.strip().split(' <-> ')
    source = data[0]
    targets = list(data[1].split(', '))
    pipe_hash[source] = targets


#seed the zero_hash
zero_hash = {'0':True}

#iterate until we're done adding new connections
last_count = 0
while last_count != len(zero_hash):
    last_count = len(zero_hash)
    add_list = []
    for pipe in zero_hash:
        for target in pipe_hash[pipe]:
            if target not in zero_hash:
                add_list.append(target)
    for target in add_list:
        zero_hash[target] = True
print("There are "+str(len(zero_hash))+" pipes in group 0.")