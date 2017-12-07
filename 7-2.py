#!/usr/bin/python3
__author__ = 'Alan Au'
__date__   = '2017-12-07'

'''
--- Part Two ---

The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

    ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
    padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
    fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?
'''

#NOTE: This code reports the needed information, but you'll have to do some visual inspection to get the answer.

inFile = open("7.txt",'r')
towers = inFile.readlines() #real input
weights = {}
stacks = {}
report_stacks = {}
seen_already = {}

#helper function to recursively get summed substack weights
def stack_weight(tower):
    total_weight = weights[tower]
    if tower in stacks:
        for sub_stack in stacks[tower]:
            total_weight += stack_weight(sub_stack)
    return(total_weight)
    
#store the weights and substacks for all towers
for tower in towers:
    data = tower.strip().split(' -> ')
    name = data[0].split()[0]
    weight = int(data[0].split()[1][1:-1])
    weights[name] = weight
    if len(data) > 1:
        top = data[1].split(', ')
        stacks[name] = top
    
#check for balanced towers
for tower in stacks:
    report = ""
    num_stacks = len(stacks[tower])
    expected = int((stack_weight(tower)-weights[tower])/num_stacks)
    balanced = True
    for substack in stacks[tower]:
        sub_weight = stack_weight(substack)
        report += substack +" ("+ str(sub_weight)+ ") "
        if sub_weight != expected:
            report_stacks[substack] = weights[substack] 
            balanced = False
    if balanced is False:
        output = "Tower "+tower+" is unbalanced. Expected: ("+str(expected)+")\nReport: "+report
        for substack in report_stacks:
            if substack in seen_already:
                seen_already[tower] = True #if a substack is unbalanced, parent is unbalanced
            else:
                seen_already[substack] = True
            output += "\nSubstack: "+substack+" Weight: "+str(weights[substack])
        if tower not in seen_already: #don't need to report unbalanced parent stacks
            print(output)
