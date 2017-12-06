#!/usr/bin/python

import math

'''
--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

What is the first value written that is larger than your puzzle input?
'''

num = 325489 #real input
next = 0

size = 11 #arbitrary, odd numbers only
mid = size//2

count = 0
col = mid + 1
row = mid
ring = 0

init_row = [0]*size
grid = []
for i in range(size):
    grid.append(init_row[:])
grid[mid][mid] = 1

def get_value(grid,row,col): #check inputs!
    value = grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1]
    value += grid[row][col-1] + grid[row][col+1]
    value += grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
    return(value)

while ring < mid-1:
    ring += 1
    for i in range(2*ring-1): #right
        value = get_value(grid, row, col)
        grid[row][col] = value
        if value > num:
            next = value
            break
        row -= 1
        
    for i in range(2*ring): #top
        value = get_value(grid, row, col)
        grid[row][col] = value
        if value > num:
            next = value
            break
        col -= 1

    for i in range(2*ring): #left
        value = get_value(grid, row, col)
        grid[row][col] = value
        if value > num:
            next = value
            break
        row += 1

    for i in range(2*ring+1): #bottom
        value = get_value(grid, row, col)
        grid[row][col] = value
        if value > num:
            next = value
            break
        col += 1

#for i in grid: print(i) #debug only, inspect grid to make sure it's working
print("For "+str(num)+" the solution is: "+str(next))
