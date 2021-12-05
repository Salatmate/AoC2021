test='''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.split('\n')
inp = open('Day 3.txt','r').read().split('\n')

def part1(inp):
    gamma = ''
    epsilon = '' 
    for i in range(len(inp[0])):
        one = 0
        zero= 0
        for x in inp:
            if x[i] == '0': zero += 1
            else: one += 1
        if zero > one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print('Gamma:',gamma)
    print('Epsilon:',epsilon)
    print('Power Consumption:',int(gamma,2) * int(epsilon,2))
    print('')
            
    
def part2(inp):
    oxlist = inp
    for i in range(len(inp[0])):
        oxone = 0
        oxzero= 0
        oxkeep= 0
        for x in oxlist:
            if x[i] == '0': oxzero += 1
            else: oxone += 1
        if oxzero <= oxone: oxkeep = 1
        oxlist = [x for x in oxlist if x[i] == str(oxkeep)]
        if len(oxlist) == 1: break
    colist = inp
    for i in range(len(inp[0])):
        coone = 0
        cozero= 0
        cokeep= 0
        for x in colist:
            if x[i] == '0': cozero += 1
            else: coone += 1
        if cozero > coone: cokeep = 1
        colist = [x for x in colist if x[i] == str(cokeep)]
        if len(colist) == 1: break
    print('Oxygen Rating:',oxlist[0])
    print('CO2 Rating:',colist[0])
    print('Life Support Rating:',int(oxlist[0],2) * int(colist[0],2))
    print('')
    
        
part1(inp)
part2(inp)
