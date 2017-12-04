#!/usr/bin/python

'''
--- Day 1: Inverse Captcha ---
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.
'''

inFile = open("1.txt",'r')
nums = str(inFile.read().strip())

#nums = "1122" #debug only, should yield 3
#nums = "1111" #debug only, should yield 4
#nums = "1234" #debug only, should yield 0
#nums = "91212129" #debug only, should yield 9

nums = list(map(int,nums)) #real input

nums.append(nums[0]) #add first digit to end, in case of circular edge case
total = 0

for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        total += nums[i]

print ("Solution: "+ str(total))
