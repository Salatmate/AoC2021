test = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.split('\n')
inp = open('Day 18.txt','r').read().split('\n')

import math

def part1(inp):
    snailfish = []
    for i in inp:
        i = i.replace(',',' ').replace(']',' ').replace('[',' ')
        snailfish.append([int(s) for s in i.split() if s.isdigit()])
    depth = []
    for i in inp:
        currdepthlist = []
        currdepth = 0
        for s in i:
            if s == '[': currdepth += 1
            elif s == ']': currdepth -= 1
            elif s != ',': currdepthlist.append(currdepth)
        depth.append(currdepthlist)
    while len(snailfish) > 1:
        it = 0
        snailfish[0] += snailfish.pop(1)
        depth[0] += depth.pop(1)
        done = False
        while not done:
            i = 0
            done = True
            while i < len(snailfish[it]):
                if depth[it][i] >= 4 and depth[it][i] == depth[it][i+1]:
                    depth[it][i] -= 1
                    if i > 0:
                        snailfish[it][i-1] += snailfish[it][i]
                    if i+2 < len(snailfish[it]):
                        snailfish[it][i+2] += snailfish[it][i+1]
                    snailfish[it].pop(i+1)
                    depth[it].pop(i+1)
                    snailfish[it][i] = 0
                    i = -1
                i += 1
            i = 0
            while i < len(snailfish[it]):
                if snailfish[it][i] > 9:
                    snailfish[it].insert(i+1,math.ceil(snailfish[it][i]/2))
                    snailfish[it][i] = math.floor(snailfish[it][i]/2)
                    depth[it].insert(i+1,depth[it][i]+1)
                    depth[it][i] += 1
                    done = False
                    break
                i += 1
        depth[it] = [i+1 for i in depth[it]]
    i = 0
    while len(snailfish[0]) > 1:
        if depth[0][i] == depth[0][i+1]:
            snailfish[0][i] = snailfish[0][i]*3 + snailfish[0][i+1]*2
            depth[0][i] -= 1
            snailfish[0].pop(i+1)
            depth[0].pop(i+1)
            i = -1
        i += 1
    print(snailfish[0][0])

import itertools
def part2(inp):
    snailfish = []
    for i in inp:
        i = i.replace(',',' ').replace(']',' ').replace('[',' ')
        snailfish.append([int(s) for s in i.split() if s.isdigit()])
    depth = []
    for i in inp:
        currdepthlist = []
        currdepth = 0
        for s in i:
            if s == '[': currdepth += 1
            elif s == ']': currdepth -= 1
            elif s != ',': currdepthlist.append(currdepth)
        depth.append(currdepthlist)
    greatest = 0
    perms = 0
    for perm in list(itertools.permutations(range(len(snailfish)),2)):
        perms += 1
        snails = snailfish[perm[0]] + snailfish[perm[1]]
        depths = depth[perm[0]] + depth[perm[1]]
        done = False
        while not done:
            i = 0
            done = True
            while i < len(snails):
                if depths[i] >= 4 and depths[i] == depths[i+1]:
                    depths[i] -= 1
                    if i > 0:
                        snails[i-1] += snails[i]
                    if i+2 < len(snails):
                        snails[i+2] += snails[i+1]
                    snails.pop(i+1)
                    depths.pop(i+1)
                    snails[i] = 0
                    i = -1
                i += 1
            i = 0
            while i < len(snails):
                if snails[i] > 9:
                    snails.insert(i+1,math.ceil(snails[i]/2))
                    snails[i] = math.floor(snails[i]/2)
                    depths.insert(i+1,depths[i]+1)
                    depths[i] += 1
                    done = False
                    break
                i += 1
        i = 0
        while len(snails) > 1:
            if depths[i] == depths[i+1]:
                snails[i] = snails[i]*3 + snails[i+1]*2
                depths[i] -= 1
                snails.pop(i+1)
                depths.pop(i+1)
                i = -1
            i += 1
        greatest = max(greatest,snails[0])
    print(greatest)
        
part1(inp)
part2(inp)
