#!/usr/bin/python

'''
--- Part Two ---

"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.
'''

inFile = open("2.txt",'r')
lines = inFile.readlines() #real input
#lines = ["5 9 2 8", "9 4 7 3", "3 8 6 5"] #debug only, should yield 9

def check_div(i,j):
    if j>i:
        i,j = j,i
    if i%j == 0:
        return i//j
    else:
        return 0

checksum = 0
for line in lines:
    line = map(int,line.strip().split())
    div = 0
    found = False
    for i in range(len(line)-1):
        for j in range(i+1,len(line)):
            div = check_div(line[i],line[j])
            if div > 0:
                checksum += div
                found = True
                break
        if found:
            break

print("Solution: "+str(checksum))
