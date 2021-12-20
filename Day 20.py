test = '''#.#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#...

#..#.
#....
##..#
..#..
..###'''.split('\n\n')
inp = open('Day 20.txt','r').read().split('\n\n')

from copy import deepcopy
from math import inf
from collections import defaultdict
def part1(inp):
    output = inp[0]
    grid = inp[1].split('\n')
    lights = defaultdict(lambda:False)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                lights[(y,x)] = True
    for steps in range(1):
        min_y = inf
        min_x = inf
        max_y = 0
        max_x = 0
        for light in lights:
            min_y = min(light[0],min_y)
            min_x = min(light[1],min_x)
            max_y = max(light[0],max_y)
            max_x = max(light[1],max_x)
        darks = defaultdict(lambda:True)
        for y in range(min_y-2,max_y+3):
            for x in range(min_x-2,max_x+3):
                square = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
                current = output[int(''.join([str(int(lights[i] == True)) for i in square]),2)]
                if current == '.': darks[(y,x)] = False
        lights = defaultdict(lambda:False)
        for y in range(min_y-2,max_y+3):
            for x in range(min_x-2,max_x+3):
                square = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
                current = output[int(''.join([str(int(darks[i] == True)) for i in square]),2)]
                if current == '#': lights[(y,x)] = True
    print(len(lights))
    
def part2(inp):
    output = inp[0]
    grid = inp[1].split('\n')
    lights = defaultdict(lambda:False)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                lights[(y,x)] = True
    for steps in range(25):
        min_y = inf
        min_x = inf
        max_y = 0
        max_x = 0
        for light in lights:
            min_y = min(light[0],min_y)
            min_x = min(light[1],min_x)
            max_y = max(light[0],max_y)
            max_x = max(light[1],max_x)
        darks = defaultdict(lambda:True)
        for y in range(min_y-2,max_y+3):
            for x in range(min_x-2,max_x+3):
                square = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
                current = output[int(''.join([str(int(lights[i] == True)) for i in square]),2)]
                if current == '.': darks[(y,x)] = False
        lights = defaultdict(lambda:False)
        for y in range(min_y-2,max_y+3):
            for x in range(min_x-2,max_x+3):
                square = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
                current = output[int(''.join([str(int(darks[i] == True)) for i in square]),2)]
                if current == '#': lights[(y,x)] = True
    print(len(lights))
    
part1(inp)
part2(inp)
