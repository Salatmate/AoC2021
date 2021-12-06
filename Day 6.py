test = [int(i) for i in '''3,4,3,1,2'''.split(',')]
inp = [int(i) for i in open('Day 6.txt','r').read().split(',')]

def part1(inp):
    fish = [0 for i in range(9)]
    for i in inp:
        fish[i] += 1
    for i in range(80):
        birth = fish.pop(0)
        fish.append(birth)
        fish[6] += birth
    print(sum(fish))
    
def part2(inp):
    fish = [0 for i in range(9)]
    for i in inp:
        fish[i] += 1
    for i in range(256):
        birth = fish.pop(0)
        fish.append(birth)
        fish[6] += birth
    print(sum(fish))
        
part1(inp)
part2(inp)
