test = [[-1] + [int(x) for x in i] + [-1] for i in'''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''.split('\n')]

test = [[-1 for i in range(len(test[0]))]] + test + [[-1 for i in range(len(test[0]))]]
inp = [[-1] + [int(x) for x in i] + [-1] for i in open('Day 11.txt','r').read().split('\n')]
inp = [[-1 for i in range(len(inp[0]))]] + inp + [[-1 for i in range(len(inp[0]))]]

def done(inp):
    for y in range(1,len(inp)-1):
        for x in range(1,len(inp[y])-1):
            if inp[y][x] > 9 and inp[y][x] < 100:
                return False
    return True

def printgrid(inp):
    string = ''
    for y in range(1,len(inp)-1):
        for x in range(1,len(inp[y])-1):
            string += str(inp[y][x])
        string += '\n'
    print(string)

def part1(inp):
    flashes = 0
    for steps in range(100):
        for y in range(1,len(inp)-1):
            for x in range(1,len(inp[y])-1):
                inp[y][x] += 1
        while not done(inp):
            for y in range(1,len(inp)-1):
                for x in range(1,len(inp[y])-1):
                    if inp[y][x] > 9 and inp[y][x] < 100:
                        inp[y][x] = 100
                        if inp[y+1][x+1] >= 0: inp[y+1][x+1] += 1
                        if inp[y-1][x-1] >= 0: inp[y-1][x-1] += 1
                        if inp[y+1][x-1] >= 0: inp[y+1][x-1] += 1
                        if inp[y-1][x+1] >= 0: inp[y-1][x+1] += 1
                        if inp[y+1][x] >= 0: inp[y+1][x] += 1
                        if inp[y-1][x] >= 0: inp[y-1][x] += 1
                        if inp[y][x+1] >= 0: inp[y][x+1] += 1
                        if inp[y][x-1] >= 0: inp[y][x-1] += 1
        
        for y in range(1,len(inp)-1):
            for x in range(1,len(inp[y])-1):
                if inp[y][x] >= 100:
                    inp[y][x] = 0
                    flashes += 1
    print(flashes)
    
def part2(inp):
    step = 0
    while True:
        step += 1
        flashes = 0
        for y in range(1,len(inp)-1):
            for x in range(1,len(inp[y])-1):
                inp[y][x] += 1
        while not done(inp):
            for y in range(1,len(inp)-1):
                for x in range(1,len(inp[y])-1):
                    if inp[y][x] > 9 and inp[y][x] < 100:
                        inp[y][x] = 100
                        if inp[y+1][x+1] >= 0: inp[y+1][x+1] += 1
                        if inp[y-1][x-1] >= 0: inp[y-1][x-1] += 1
                        if inp[y+1][x-1] >= 0: inp[y+1][x-1] += 1
                        if inp[y-1][x+1] >= 0: inp[y-1][x+1] += 1
                        if inp[y+1][x] >= 0: inp[y+1][x] += 1
                        if inp[y-1][x] >= 0: inp[y-1][x] += 1
                        if inp[y][x+1] >= 0: inp[y][x+1] += 1
                        if inp[y][x-1] >= 0: inp[y][x-1] += 1
        
        for y in range(1,len(inp)-1):
            for x in range(1,len(inp[y])-1):
                if inp[y][x] >= 100:
                    inp[y][x] = 0
                    flashes += 1
        if flashes == 100:
            break
    print(step)

part1(inp)
inp = [[-1] + [int(x) for x in i] + [-1] for i in open('Day 11.txt','r').read().split('\n')]
inp = [[-1 for i in range(len(inp[0]))]] + inp + [[-1 for i in range(len(inp[0]))]]
part2(inp)
