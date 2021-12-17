test = [20,30,-10,-5]
inp = open('Day 17.txt','r').read()
inp = [int(i) for i in [inp.split('=')[1].split('.')[0],inp.split(',')[0].split('.')[-1],inp.split('=')[2].split('.')[0],inp.split('.')[-1]]]

def part1(inp):
    min_y = inp[2]
    print(min_y*(min_y+1)//2)

from math import sqrt
def part2(inp):
    min_x,max_x,min_y,max_y = inp
    total_vel = 0
    for vel_y in range(min_y,abs(min_y)):
        for vel_x in range(int(sqrt(min_x)),max_x+1):
            x = 0
            y = 0
            curr_x = vel_x
            curr_y = vel_y
            while y > max_y or x < min_x:
                x += curr_x
                if curr_x > 0: curr_x -= 1
                if curr_x == 0 and not y > max_y: break
                y += curr_y
                curr_y -= 1
            if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
                total_vel += 1
    print(total_vel)

part1(inp)
part2(inp)
