#!/usr/bin/python

'''
--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.
'''

inFile = open("1.txt",'r')
nums = str(inFile.read().strip()) #real input

#nums = "1212" #debug only, should yield 6
#nums = "1221" #debug only, should yield 0
#nums = "123425" #debug only, should yield 4
#nums = "123123" #debug only, should yield 12
#nums = "12131415" #debug only, should yield 4

nums = list(map(int,nums))

half = len(nums)/2
nums.extend(nums) #double it so indexes don't break

total = 0

for i in range(half):
    if nums[i] == nums[i+half]:
        total += nums[i] * 2

print ("Solution: "+ str(total))
