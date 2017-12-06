#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-06'

'''
--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
'''

inFile = open("4.txt",'r')
phrases = inFile.readlines() #real input

#debug only: should return 3
#phrases = ["abcde fghij","abcde xyz ecdab","a ab abc abd abf abj","iiii oiii ooii oooi oooo","oiii ioii iioi iiio"] 

valid = 0

for phrase in phrases:
    phrase_valid = True
    word_dict = {}
    words = phrase.strip().split()
    for word in words:
        word = ''.join(sorted(word)) #not ideal, but words are short so it's okay
        if word in word_dict:
            phrase_valid = False
            break
        else:
            word_dict[word] = True
    if phrase_valid:
        valid += 1
    
print ("Number of valid passphrases: "+ str(valid))
