test = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''
inp = open('Day 4.txt','r').read()

def win(card,drawn):
    for i in range(5):
        if card[i] in drawn and card[i+5] in drawn and card[i+10] in drawn and card[i+15] in drawn and card[i+20] in drawn:
            return True

    for i in range(0,25,5):
        if card[i] in drawn and card[i+1] in drawn and card[i+2] in drawn and card[i+3] in drawn and card[i+4] in drawn:
            return True
    return False

    
def part1(inp):
    numbers = inp.split('\n')[0].split(',')
    cards = [i.split() for i in inp.split('\n\n')[1:]]
    drawn = []
    done = False
    for i in numbers:
        drawn.append(i)
        for card in cards:
            if win(card, drawn) == True:
                print(sum([int(i) for i in card if i not in drawn])*int(i))
                done = True
                break
        if done: break
    
def part2(inp):
    numbers = inp.split('\n')[0].split(',')
    cards = [i.split() for i in inp.split('\n\n')[1:]]
    drawn = []
    for i in numbers:
        drawn.append(i)
        for card in cards:
            if win(card, drawn) == True:
                latest = sum([int(i) for i in card if i not in drawn])*int(i)
                cards.remove(card)
    print(latest)
    
part1(inp)
part2(inp)
