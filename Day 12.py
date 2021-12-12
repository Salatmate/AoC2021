test = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''.split('\n')
inp = open('Day 12.txt','r').read().split('\n')

import copy

def part1(inp):
    connections = {}
    for i in inp:
        if i.split('-')[0] not in connections.keys():
            connections[i.split('-')[0]] = []
        if i.split('-')[1] != 'start':
            connections[i.split('-')[0]] += [i.split('-')[1]]
            
        if i.split('-')[1] not in connections.keys():
            connections[i.split('-')[1]] = []
        if i.split('-')[0] != 'start':
            connections[i.split('-')[1]] += [i.split('-')[0]]
    done = 0
    paths = [['start']]
    while len(paths) > 0:
        path = paths.pop(-1)
        for i in connections[path[-1]]:
            if i.islower() and i in path:
                continue
            paths.append(path + [i])
            if paths[-1][-1] == 'end':
                done += 1
                paths.remove(path + [i])
    print(done)

def visited(inp):
    if [inp.count(i) for i in inp if i.islower()].count(2) == 2:
        return True
    return False

def part2(inp):
    connections = {}
    for i in inp:
        if i.split('-')[0] not in connections.keys():
            connections[i.split('-')[0]] = []
        if i.split('-')[1] != 'start':
            connections[i.split('-')[0]] += [i.split('-')[1]]
            
        if i.split('-')[1] not in connections.keys():
            connections[i.split('-')[1]] = []
        if i.split('-')[0] != 'start':
            connections[i.split('-')[1]] += [i.split('-')[0]]
    done = 0
    paths = [['start']]
    while len(paths) > 0:
        path = paths.pop(-1)
        for i in connections[path[-1]]:
            if i.islower() and (path.count(i) == 2 or (i in path and visited(path))):
                continue
            paths.append(path + [i])
            if paths[-1][-1] == 'end':
                done += 1
                paths.remove(path + [i])
    print(done)


part1(inp)
part2(inp)
