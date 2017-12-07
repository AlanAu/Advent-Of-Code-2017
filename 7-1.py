#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-07'

'''
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?
'''

inFile = open("7.txt",'r')
towers = inFile.readlines() #real input
candidates = {}

for tower in towers:
    tower = tower.strip().split(' -> ')
    if len(tower) == 1: #no disc
        continue

    base = tower[0].split()[0]
    if base not in candidates:
        candidates[base] = True #if we haven't seen this before, it's a candidate

    tops = tower[1].split(', ')
    for top in tops:
        candidates[top] = False #if on top of something, it can't be the base

for program in candidates:
    if candidates[program] is True:
        print ("The bottom program is: "+program)
        break
