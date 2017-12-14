#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-13'

'''
--- Part Two ---

There are more programs than just the ones in the group containing program ID 0. The rest of them have no way of reaching that group, and still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes either directly or indirectly. The programs you identified just a moment ago are all part of the same group. Now, they would like you to determine the total number of groups.

In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?
'''

inFile = open("12.txt",'r')
pipes = inFile.readlines() #real input

pipe_hash = {}
for pipe in pipes:
    data = pipe.strip().split(' <-> ')
    source = data[0]
    targets = list(data[1].split(', '))
    pipe_hash[source] = targets

groups = 0
while len(pipe_hash) > 0:
    #seed a new group
    group_hash = {}
    group_hash[list(pipe_hash.keys())[0]] = True

    #iterate until we're done adding new connections
    last_count = 0
    while last_count != len(group_hash):
        last_count = len(group_hash)
        add_list = []
        for pipe in group_hash:
            for target in pipe_hash[pipe]:
                if target not in group_hash:
                    add_list.append(target)
        for target in add_list:
            group_hash[target] = True

    #remove all of the pipes in that group
    for pipe in group_hash:
        del pipe_hash[pipe]
    groups += 1
print("There are "+str(groups)+" groups of pipes.")