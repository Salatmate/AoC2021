test = sorted([int(i) for i in '''16,1,2,0,4,2,7,1,2,14'''.split(',')])
inp = sorted([int(i) for i in open('Day 7.txt','r').read().split(',')])

def part1(inp):
    lowest = sum([abs(inp[0] - pos) for pos in inp])
    for i in range(inp[0]+1,inp[-1]):
        check = sum([abs(i - pos) for pos in inp])
        if check < lowest: lowest = check
    print(lowest)
    
def part2(inp):
    lowest = sum([(abs(inp[0]-pos)*(abs(inp[0]-pos)+1))/2 for pos in inp])
    for i in range(inp[0]+1,inp[-1]):
        check = sum([(abs(i-pos)*(abs(i-pos)+1))/2 for pos in inp])
        if check < lowest: lowest = check
    print(int(lowest))
    
part1(inp)
part2(inp)
