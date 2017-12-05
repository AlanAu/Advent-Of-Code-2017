#!/usr/bin/python

import math

'''
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward.

What is the Manhattan Distance between the location of the data and square 1?
'''

num = 325489 #real input
#num = 1 #debug only, should be 0
#num = 12 #debug only, should be 3
#num = 23 #debug only, should be 2
#num = 1024 #debug only, should be 31

side = int(math.floor(math.sqrt(num-1))) + 1
last = side * side
ring = (side-1)/2 #it's at least this distance to the correct ring
bottom = last - (side/2)
left = bottom - side + 1
top = left - side + 1
right = top - side + 1

#find the offset from the nearest center point
min_dist = min(abs(num-right), abs(num-top), abs(num-left), abs(num-bottom))
print("For "+str(num)+" the solution is: "+str(min_dist + ring))
