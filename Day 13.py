test = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''
inp = open('Day 13.txt','r').read()
import itertools
def part1(inp):
    dots = [[int(j) for j in i.split(',')] for i in inp.split('\n\n')[0].split('\n')]
    folds = inp.split('\n\n')[1].split('\n')
    for dot in range(len(dots)):
        if folds[0][11] == 'x': along = 0
        else: along = 1
        line = int(folds[0][13:])
        if dots[dot][along] > line:
            dots[dot][along] = 2 * line - dots[dot][along]
    dots.sort()
    print(len(list(dots for dots,_ in itertools.groupby(dots))))
    
def part2(inp):
    dots = [[int(j) for j in i.split(',')] for i in inp.split('\n\n')[0].split('\n')]
    folds = inp.split('\n\n')[1].split('\n')
    for fold in folds:
        for dot in range(len(dots)):
            if fold[11] == 'x': along = 0
            else: along = 1
            line = int(fold[13:])
            if dots[dot][along] > line:
                dots[dot][along] = 2 * line - dots[dot][along]
    dots.sort()
    dots = list(dots for dots,_ in itertools.groupby(dots))
    maxx = 0
    maxy = 0
    for i in dots:
        if i[0] > maxx: maxx = i[0]
        if i[1] > maxy: maxy = i[1]
    string = ''
    for y in range(maxy+1):
        for x in range(maxx+1):
            string += '#' if [x,y] in dots else ' '
        string += '\n'
    print(string)
        
    
part1(inp)
part2(inp)
