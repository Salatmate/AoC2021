test = [[11] + [int(y) for y in i] + [11] for i in '''2199943210
3987894921
9856789892
8767896789
9899965678'''.split('\n')]
test = [[11 for i in range(len(test[0]))]] + test + [[11 for i in range(len(test[0]))]]
inp = [[11] + [int(y) for y in i] + [11] for i in open('Day 9.txt','r').read().split('\n')]
inp = [[11 for i in range(len(inp[0]))]] + inp + [[11 for i in range(len(inp[0]))]]

def part1(inp):
    levels = 0
    for y in range(1,len(inp)-1):
        for x in range(1,len(inp[y])-1):
            if inp[y][x] == '5': print(int(inp[y][x]),int(inp[y+1][x]),int(inp[y-1][x]),int(inp[y][x+1]),int(inp[y][x-1]))
            if inp[y][x] < inp[y+1][x] and inp[y][x] < inp[y-1][x] and inp[y][x] < inp[y][x-1] and inp[y][x] < inp[y][x+1]:
                levels +=  int(inp[y][x]) + 1
    print(levels)
    
def part2(inp):
    lows = []
    for y in range(1,len(inp)-1):
        for x in range(1,len(inp[y])-1):
            if inp[y][x] == '5': print(int(inp[y][x]),int(inp[y+1][x]),int(inp[y-1][x]),int(inp[y][x+1]),int(inp[y][x-1]))
            if inp[y][x] < inp[y+1][x] and inp[y][x] < inp[y-1][x] and inp[y][x] < inp[y][x-1] and inp[y][x] < inp[y][x+1]:
                lows.append([y,x])
    basins = []
    for i in lows:
        done = []
        size = 0
        locations = [[i[0],i[1]]]
        while len(locations) != 0:
            size += 1
            y = locations[0][0]
            x = locations[0][1]
            if inp[y][x] < inp[y+1][x] and [y+1,x] not in done and inp[y+1][x] < 9:
                locations.append([y+1, x])
                done.append([y+1,x])
            if inp[y][x] < inp[y-1][x] and [y-1,x] not in done and inp[y-1][x] < 9:
                locations.append([y-1, x])
                done.append([y-1,x])
            if inp[y][x] < inp[y][x+1] and [y,x+1] not in done and inp[y][x+1] < 9:
                locations.append([y, x+1])
                done.append([y,x+1])
            if inp[y][x] < inp[y][x-1] and [y,x-1] not in done and inp[y][x-1] < 9:
                locations.append([y, x-1])
                done.append([y,x-1])
            locations.pop(0)
        basins.append(size)
    basins = sorted(basins)[-3:]
    print(basins[0] * basins[1] * basins[2])
    
part1(inp)
part2(inp)
