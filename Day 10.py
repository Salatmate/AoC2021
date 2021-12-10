test = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''.split('\n')
inp = open('Day 10.txt','r').read().split('\n')

def part1(inp):
    opening = ['(','[','{','<']
    closing = [')',']','}','>']
    corrupted = 0
    for i in inp:
        indent = []
        for s in i:
            if s in opening:
                indent.append(s)
            else:
                if closing.index(s) == opening.index(indent[-1]):
                    indent.pop(-1)
                else:
                    match s:
                        case ')': corrupted += 3
                        case ']': corrupted += 57
                        case '}': corrupted += 1197
                        case '>': corrupted += 25137
                    break
    print(corrupted)
    
def part2(inp):
    opening = ['(','[','{','<']
    closing = [')',']','}','>']
    scores = []
    for i in inp:
        corrupted = False
        indent = []
        for s in i:
            if s in opening:
                indent.append(s)
            else:
                if closing.index(s) == opening.index(indent[-1]):
                    indent.pop(-1)
                else:
                    corrupted = True
                    break
        if corrupted: continue
        indent.reverse()
        indent = [closing[opening.index(x)] for x in indent]
        score = 0
        for x in indent:
            score *= 5
            match x:
                case ')': score += 1
                case ']': score += 2
                case '}': score += 3
                case '>': score += 4
        scores.append(score)
    print(sorted(scores)[int((len(scores)-1)/2)])
    
part1(inp)
part2(inp)
