test = '''Player 1 starting position: 4
Player 2 starting position: 8'''.split('\n')
inp = open('Day 21.txt','r').read().split('\n')

def parse(inp):
    p1 = int(inp[0].split()[-1])
    p2 = int(inp[1].split()[-1])
    return p1,p2

def part1(inp):
    p1,p2 = parse(inp)
    score1 = 0
    score2 = 0
    dice = 1
    rolls = 0
    while score1 < 1000 and score2 < 1000:
        p1 += ((dice-1)%100+1 + (dice)%100+1 + (dice+1)%100+1)
        p1 = (p1-1)%10+1
        score1 += p1
        rolls += 3
        dice += 3
        if score1 >= 1000: break
        p2 += (((dice-1)%100+1 + (dice)%100+1 + (dice+1)%100+1))
        p2 = (p2-1)%10+1
        score2 += p2
        dice += 3
        rolls += 3
    print(rolls*min(score1,score2))

from collections import defaultdict
def game(inp):
    turn = 0
    turns = defaultdict(lambda:0)
    pos = defaultdict(lambda:0)
    pos[(inp,0)] = 1
    notdone = defaultdict(lambda:0)
    while pos:
        turn += 1
        roll1 = defaultdict(lambda:0)
        for i in pos:
            if i[1] < 21:
                roll1[(((i[0])%10)+1,i[1])] += pos[i]
                roll1[(((i[0]+1)%10)+1,i[1])] += pos[i]
                roll1[(((i[0]+2)%10)+1,i[1])] += pos[i]
        roll2 = defaultdict(lambda:0)
        for i in roll1:
            roll2[(((i[0])%10)+1,i[1])] += roll1[i]
            roll2[(((i[0]+1)%10)+1,i[1])] += roll1[i]
            roll2[(((i[0]+2)%10)+1,i[1])] += roll1[i]
        pos = defaultdict(lambda:0)
        for i in roll2:
            pos[(((i[0])%10)+1,i[1]+((i[0])%10)+1)] += roll2[i]
            pos[(((i[0]+1)%10)+1,i[1]+((i[0]+1)%10)+1)] += roll2[i]
            pos[(((i[0]+2)%10)+1,i[1]+((i[0]+2)%10)+1)] += roll2[i]
        for i in pos:
            if i[1] < 21:
                notdone[turn] += pos[i]
            else:
                turns[turn] += pos[i]
                pos[i] = 0
    return notdone,turns
    
def part2(inp):
    p1,p2 = parse(inp)
    notdone1,turns1 = game(p1)
    notdone2,turns2 = game(p2)
    p1 = 0
    for i in turns1:
        p1 += turns1[i] * notdone2[i-1]
    p2 = 0
    for i in turns2:
        p2 += turns2[i] * notdone1[i]
    print(max(p1,p2))


part1(inp)
part2(inp)
