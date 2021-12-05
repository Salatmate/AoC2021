test = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''.split('\n')
inp = open('Day 5.txt','r').read().split('\n')

def part1(inp):
    field = [[0 for y in range(1000)] for x in range(1000)]
    for i in inp:
        x1 = int(i.split(',')[0])
        x2 = int(i.split(',')[1].split(' ')[2])
        y1 = int(i.split(',')[1].split(' ')[0])
        y2 = int(i.split(',')[2])
        if x1 == x2:
            x = x1
            for y in range(y1,y2+(1 if y1 < y2 else -1),(1 if y1 < y2 else -1)):
                field[x][y] += 1
        elif y1 == y2:
            y = y1
            for x in range(x1,x2+(1 if x1 < x2 else -1),(1 if x1 < x2 else -1)):
                field[x][y] += 1
    intersect = 0
    for y in range(len(field)):
        for x in range(len(field)):
            if field[x][y] > 1:
                intersect += 1
    print(intersect)
        
    

def part2(inp):
    field = [[0 for y in range(1000)] for x in range(1000)]
    for i in inp:
        x1 = int(i.split(',')[0])
        x2 = int(i.split(',')[1].split(' ')[2])
        y1 = int(i.split(',')[1].split(' ')[0])
        y2 = int(i.split(',')[2])
        if x1 == x2:
            x = x1
            for y in range(y1,y2+(1 if y1 < y2 else -1),(1 if y1 < y2 else -1)):
                field[x][y] += 1
        elif y1 == y2:
            y = y1
            for x in range(x1,x2+(1 if x1 < x2 else -1),(1 if x1 < x2 else -1)):
                field[x][y] += 1
        elif x1 < x2 and y1 < y2:
            for n in range(abs(x2-x1)+1):
                field[x1+n][y1+n] += 1
        elif x1 < x2 and y1 > y2:
            for n in range(abs(x2-x1)+1):
                field[x1+n][y1-n] += 1
        elif x1 > x2 and y1 < y2:
            for n in range(abs(x2-x1)+1):
                field[x1-n][y1+n] += 1
        elif x1 > x2 and y1 > y2:
            for n in range(abs(x2-x1)+1):
                field[x1-n][y1-n] += 1
    intersect = 0
    for y in range(len(field)):
        for x in range(len(field)):
            if field[x][y] > 1:
                intersect += 1
    print(intersect)
    
part1(inp)
part2(inp)
