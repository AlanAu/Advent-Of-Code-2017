#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-13'

'''
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

How many steps away is the furthest he ever got from his starting position?
'''

inFile = open("11.txt",'r')
moves = inFile.read().strip().split(',') #real input

#moves = ["ne","ne","ne"] #debug, 3 steps
#moves = ["ne","ne","sw","sw"] #debug, 0 steps
#moves = ["ne","ne","s","s"] #debug, 2 steps
#moves = ["se","sw","se","sw","sw"] #debug, 3 steps

dirhash = {"ns":0.0,"ew":0.0}
currdist = 0
maxdist = 0
for move in moves:
    if move == "n":
        dirhash["ns"]+=1.0
    elif move == "ne":
        dirhash["ns"]+=0.5
        dirhash["ew"]+=1.0
    elif move == "nw":
        dirhash["ns"]+=0.5
        dirhash["ew"]-=1.0
    elif move == "s":
        dirhash["ns"]-=1.0
    elif move == "se":
        dirhash["ns"]-=0.5
        dirhash["ew"]+=1.0
    elif move == "sw":
        dirhash["ns"]-=0.5
        dirhash["ew"]-=1.0
          
    ewdist = abs(dirhash["ew"])
    nsdist = abs(dirhash["ns"])+0.5

    if ewdist >= nsdist: 
        currdist = ewdist #we can zig-zag our way there at no nsdist penalty
    else: 
        currdist = nsdist + (ewdist/2) #ewdist/2 are diagonal steps, so we need to double-count them to get nsdist
    if currdist > maxdist:
        maxdist = currdist
print("The max number of steps away was: "+str(int(maxdist)))