inp = [int(i) for i in open('Day 1.txt','r').read().split('\n')]
test = '''199
200
208
210
200
207
240
269
260
263'''
test = [int(i) for i in test.split('\n')]

def part1(inp):
    inc = 0
    for i in range(len(inp)-1):
        if inp[i+1] > inp[i]:
            inc+=1

    print(inc)

def part2(inp):
    inc = 0
    for i in range(len(inp)-3):
        if inp[i+1] + inp[i+2] + inp[i+3] > inp[i] +inp[i+1] + inp[i+2]:
            inc +=1
    print(inc)

part1(inp)
part2(inp)

