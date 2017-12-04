#!/usr/bin/python

'''
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.
'''

inFile = open("2.txt",'r')
lines = inFile.readlines() #real input
#lines = ["5 1 9 5","7 5 3","2 4 6 8"] #debug only, should yield 18

checksum = 0

for line in lines:
    line = map(int,line.strip().split())
    diff = 0
    low = high = line[0]
    for num in line[1:]:
        if num < low:
            low = num
        elif num > high:
            high = num
    diff = high - low
    checksum += diff

print("Solution: "+str(checksum))
