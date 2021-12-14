test = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
inp = open('Day 14.txt','r').read()

def part1(inp):
    polymer = inp.split('\n\n')[0]
    growth = inp.split('\n\n')[1].split('\n')
    insertion = {}
    for stage in growth:
        insertion[stage.split(' ')[0]] = stage.split(' ')[-1]
    for step in range(10):
        next_polymer = polymer[0]
        for i in range(len(polymer)-1):
            next_polymer += insertion[polymer[i] + polymer[i+1]]
            next_polymer += polymer[i+1]
        polymer = next_polymer
    quantity = []
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        quantity += [polymer.count(i)]
    quantity = [i for i in sorted(quantity) if i != 0]
    print(max(quantity) - min(quantity))

import copy 
def part2(inp):
    polymer = inp.split('\n\n')[0]
    growth = inp.split('\n\n')[1].split('\n')
    insertion = {}
    for stage in growth:
        insertion[stage.split(' ')[0]] = [0,stage.split(' ')[-1]]
    for i in range(len(polymer)-1):
        insertion[polymer[i] + polymer[i+1]][0] += 1
    for step in range(40):
        nextstage = copy.deepcopy(insertion)
        for key in list(insertion.keys()):
            if insertion[key][0] >= 1:
                nextstage[key][0] -= insertion[key][0]
                nextstage[key[0] + insertion[key][1]][0] += insertion[key][0]
                nextstage[insertion[key][1]+key[1]][0] += insertion[key][0]
        insertion = copy.deepcopy(nextstage)
    quantity = {}
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        quantity[i] = 0
        if i == polymer[0]: quantity[i] = 1
    for key in list(insertion.keys()):
        quantity[key[1]] += insertion[key][0]
    quantity = [i for i in sorted(list(quantity.values())) if i != 0]
    print(max(quantity) - min(quantity))

part1(inp)
part2(inp)
