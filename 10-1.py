#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-13'

'''
--- Day 10: Knot Hash ---

You come across some programs that are trying to implement a software emulation of a hash based on knot-tying. The hash these programs are implementing isn't very strong, but you decide to help them anyway. You make a mental note to remind the Elves later not to invent their own cryptographic functions.

This hash function simulates tying a knot in a circle of string with 256 marks on it. Based on the input to be hashed, the function repeatedly selects a span of string, brings the ends together, and gives the span a half-twist to reverse the order of the marks within it. After doing this many times, the order of the marks is used to build the resulting hash.

  4--5   pinch   4  5           4   1
 /    \  5,0,1  / \/ \  twist  / \ / \
3      0  -->  3      0  -->  3   X   0
 \    /         \ /\ /         \ / \ /
  2--1           2  1           2   5

To achieve this, begin with a list of numbers from 0 to 255, a current position which begins at 0 (the first element in the list), a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:

    Reverse the order of that length of elements in the list, starting with the element at the current position.
    Move the current position forward by that length plus the skip size.
    Increase the skip size by one.

The list is circular; if the current position and the length try to reverse elements beyond the end of the list, the operation reverses using as many extra elements as it needs from the front of the list. If the current position moves past the end of the list, it wraps around to the front. Lengths larger than the size of the list are invalid.

Once this process is complete, what is the result of multiplying the first two numbers in the list?
'''

inFile = open("10.txt",'r')
inText = inFile.read().strip() #real input
lengths = list(map(int,inText.split(',')))

listsize = 256
current = skip = 0

mylist = list(range(listsize))
mylist.extend(list(range(listsize)))

for interval in lengths:
    sublist = mylist[current: current+interval]
    sublist.reverse()
    mylist[current: current+interval] = sublist
    current += interval
    if current > listsize:
        mylist[:current-listsize] = mylist[listsize:current]
    else:
        mylist[listsize:] = mylist[:listsize]
    current += skip
    current = current % listsize
    skip += 1
print("Multiplying the first two numbers of your final list gives you: "+str(mylist[0]*mylist[1]))