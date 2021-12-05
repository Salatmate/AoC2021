test='''forward 5
down 5
forward 8
up 3
down 8
forward 2'''.split('\n')
inp = open('Day 2.txt','r').read().split('\n')

def part1(inp):
    x = y = 0
    for s in inp:
        mag = int(s.split(' ')[1])
        match s.split(' ')[0]:
            case 'forward': x += mag
            case 'up': y -= mag
            case 'down': y += mag
    print(x*y)
def part2(inp):
    x = y = aim = 0
    for s in inp:
        mag = int(s.split(' ')[1])
        match s.split(' ')[0]:
            case 'forward':
                x += mag
                y += aim * mag
            case 'up': aim -= mag
            case 'down': aim += mag
    print(x*y)
    
part1(inp)
part2(inp)

