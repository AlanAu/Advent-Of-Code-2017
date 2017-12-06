#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-06'

'''
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    aa bb cc dd ee is valid.
    aa bb cc dd aa is not valid - the word aa appears more than once.
    aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
'''

inFile = open("4.txt",'r')
phrases = inFile.readlines() #real input

#phrases = ["aa bb cc dd ee","aa bb cc dd aa","aa bb cc dd aaa"] #debug only: should return 2

valid = 0

for phrase in phrases:
    phrase_valid = True
    word_dict = {}
    words = phrase.strip().split()
    for word in words:
        if word in word_dict:
            phrase_valid = False
            break
        else:
            word_dict[word] = True
    if phrase_valid:
        valid += 1
    
print ("Number of valid passphrases: "+ str(valid))
