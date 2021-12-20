test = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''.split('\n')
inp = open('Day 18.txt','r').read().split('\n')

import math
def reduce(snails,depth):
    i = 0
    while i < len(snails):
        if depth[i] >= 4 and depth[i] == depth[i+1]:
            depth[i] -= 1
            if i+2 < len(snails):
                snails[i+2] += snails[i+1]
            snails.pop(i+1)
            depth.pop(i+1)
            r = snails[i]
            snails[i] = 0
            if i > 0:
                snails[i-1] += r
                i -= 2
        i += 1
    i = 0
    while i < len(snails):
        if depth[i] >= 4 and depth[i] == depth[i+1]:
            depth[i] -= 1
            if i+2 < len(snails):
                snails[i+2] += snails[i+1]
            snails.pop(i+1)
            depth.pop(i+1)
            r = snails[i]
            snails[i] = 0
            if i > 0:
                snails[i-1] += r
                i -= 1
                if i > 1: i -= 1
        if snails[i] >= 10:
            snails.insert(i+1,math.ceil(snails[i]/2))
            depth.insert(i+1,depth[i]+1)
            snails[i] = math.floor(snails[i]/2)
            depth[i] += 1
            i -= 1
        i += 1
    depth = [i+1 for i in depth]
    return snails,depth

def magnitude(snails,depth):
    i = 0
    while len(snails) > 1:
        i = max(0,i)
        if depth[i] == depth[i+1]:
            snails[i] = snails[i]*3 + snails.pop(i+1)*2
            depth[i] -= 1
            depth.pop(i+1)
            i -= 2
        i += 1
    return snails[0]
    
def part1(inp):
    snailfish = []
    for i in inp:
        i = i.replace(',',' ').replace(']',' ').replace('[',' ')
        snailfish.append([int(s) for s in i.split() if s.isdigit()])
    depths = []
    for i in inp:
        currdepthlist = []
        currdepth = 0
        for s in i:
            if s == '[': currdepth += 1
            elif s == ']': currdepth -= 1
            elif s != ',': currdepthlist.append(currdepth)
        depths.append(currdepthlist)
    snails = snailfish[0]
    depth = depths[0]
    while len(snailfish) > 1:
        snails += snailfish.pop(1)
        depth += depths.pop(1)
        snails,depth = reduce(snails,depth)
    i = 0
    print(magnitude(snails,depth))
        

import itertools
def part2(inp):
    snailfish = []
    for i in inp:
        i = i.replace(',',' ').replace(']',' ').replace('[',' ')
        snailfish.append([int(s) for s in i.split() if s.isdigit()])
    depths = []
    for i in inp:
        currdepthlist = []
        currdepth = 0
        for s in i:
            if s == '[': currdepth += 1
            elif s == ']': currdepth -= 1
            elif s != ',': currdepthlist.append(currdepth)
        depths.append(currdepthlist)
    greatest = 0
    snailfish = [i for i in snailfish if len(i) > 10]
    depths = [i for i in depths if len(i) > 10]
    for perm in list(itertools.permutations(range(len(snailfish)),2)):
        snails, depth = reduce(snailfish[perm[0]]+snailfish[perm[1]],depths[perm[0]]+depths[perm[1]])
        greatest = max(magnitude(snails,depth),greatest)
    print(greatest)


part1(inp)
part2(inp)
