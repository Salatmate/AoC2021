test2 = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

test = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''.split('\n')
inp = open('Day 8.txt','r').read().split('\n')

def part1(inp):
    ans = 0
    for i in inp:
        output = i.split('| ')[1]
        for x in output.split(' '):
            length = len(x)
            if length == 2 or length == 3 or length == 4 or length == 7:
                ans += 1
    print(ans)
                
    
def part2(inp):
    ans = 0
    for i in inp:
        patterns = i.split(' |')[0].split()
        patterns.sort(key=len)
        signals = [list('abcdefg') for i in range(7)]
        signals[0] = [i for i in list(patterns[1]) if i not in list(patterns[0])][0]
        signals[1] = [i for i in list(patterns[2]) if i not in list(patterns[0])]
        signals[2] = list(patterns[0])
        signals[3] = [i for i in list(patterns[2]) if i not in list(patterns[0])]
        signals[4] = [i for i in list('abcdefg') if i not in list(patterns[1])+list(patterns[2])]
        signals[5] = list(patterns[0])
        signals[6] = [i for i in list('abcdefg') if i not in list(patterns[1])+list(patterns[2])]

        char5 = patterns[3:6]
        if sum([chars.count(signals[1][0]) for chars in char5]) == 1:
            signals[1] = signals[1][0]
            signals[3] = signals[3][1]
        else:
            signals[1] = signals[1][1]
            signals[3] = signals[3][0]

        char6 = patterns[6:9]
        if sum([chars.count(signals[2][0]) for chars in char6]) == 2:
            signals[2] = signals[2][0]
            signals[5] = signals[5][1]
        else:
            signals[2] = signals[2][1]
            signals[5] = signals[5][0]
        if sum([chars.count(signals[4][0]) for chars in char6]) == 2:
            signals[4] = signals[4][0]
            signals[6] = signals[6][1]
        else:
            signals[4] = signals[4][1]
            signals[6] = signals[6][0]
            

        out = i.split('| ')[1].split()
        string = ''
        for digit in out:
            match sorted([signals.index(i) for i in digit]):
                case [0,1,2,4,5,6]: string += '0'
                case [2,5]: string += '1'
                case [0,2,3,4,6]: string += '2'
                case [0,2,3,5,6]: string += '3'
                case [1,2,3,5]: string += '4'
                case [0,1,3,5,6]: string += '5'
                case [0,1,3,4,5,6]: string += '6'
                case [0,2,5]: string += '7'
                case [0,1,2,3,4,5,6]: string += '8'
                case [0,1,2,3,5,6]: string += '9'
        ans += int(string)
    print(ans)
                    
    
part1(inp)
part2(inp)
