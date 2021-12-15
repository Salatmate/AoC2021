test = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''.split('\n')
inp = open('Day 15.txt','r').read().split('\n')

import copy
from collections import defaultdict
import heapq
import math
def part1(inp):
    grid = [[int(j) for j in i] for i in inp]
    distance = defaultdict(lambda:math.inf)
    distance[(0,0)] = 0
    risk = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            risk[(y,x)] = grid[y][x]

    paths = [(0,(0,0))]
    length = len(grid)
    corner = (length-1,length-1)

    visited = set()
    while True:
        dist, curr_node = heapq.heappop(paths)
        if curr_node == corner:
            print(dist)
            break
        if curr_node in visited:
            continue
        visited.add(curr_node)
        
        N = (curr_node[0]-1,curr_node[1])
        W = (curr_node[0],curr_node[1]-1)
        E = (curr_node[0],curr_node[1]+1)
        S = (curr_node[0]+1,curr_node[1])
        adjs = []
        if N[0] >= 0 and N not in visited: adjs.append(N)
        if W[1] >= 0 and W not in visited: adjs.append(W)
        if E[1] < length and E not in visited: adjs.append(E)
        if S[0] < length and S not in visited: adjs.append(S)
        for adj in adjs:
            new_dist = dist + risk[adj]
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                heapq.heappush(paths,(new_dist,adj))


def part2(inp):
    grid = [[int(j) for j in i] for i in inp]
    full_grid = copy.deepcopy(grid)
    for y in range(len(grid)):
        for i in range(1,5):
            full_grid[y] += [(j+i)%10+1 if (j+i)%10 < j else j+i for j in grid[y]]
    for i in range(1,5):
        for y in range(len(grid)):
            full_grid += [[(j+i)%10+1 if (j+i)%10 < j else j+i for j in full_grid[y]]]
    grid = copy.deepcopy(full_grid)
    distance = defaultdict(lambda:math.inf)
    distance[(0,0)] = 0
    risk = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            risk[(y,x)] = grid[y][x]

    paths = [(0,(0,0))]
    length = len(grid)
    corner = (length-1,length-1)

    visited = set()
    while True:
        dist, curr_node = heapq.heappop(paths)
        if curr_node == corner:
            print(dist)
            break
        if curr_node in visited:
            continue
        visited.add(curr_node)
        
        N = (curr_node[0]-1,curr_node[1])
        W = (curr_node[0],curr_node[1]-1)
        E = (curr_node[0],curr_node[1]+1)
        S = (curr_node[0]+1,curr_node[1])
        adjs = []
        if N[0] >= 0 and N not in visited: adjs.append(N)
        if W[1] >= 0 and W not in visited: adjs.append(W)
        if E[1] < length and E not in visited: adjs.append(E)
        if S[0] < length and S not in visited: adjs.append(S)
        for adj in adjs:
            new_dist = dist + risk[adj]
            if new_dist < distance[adj]:
                distance[adj] = new_dist
                heapq.heappush(paths,(new_dist,adj))

part1(inp)
part2(inp)
