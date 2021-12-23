test = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########'''
inp = open('Day 23.txt','r').read()

from collections import defaultdict
import heapq
from copy import copy,deepcopy
def energy(dist,unit):
    match unit:
        case 'A':return dist
        case 'B':return dist*10
        case 'C':return dist*100
        case 'D':return dist*1000
def room_pos(unit):
    match unit:
        case 'A':return 0
        case 'B':return 1
        case 'C':return 2
        case 'D':return 3
        
def part1(inp):
    win = [['A','A'],['B','B'],['C','C'],['D','D']]
    rooms = [[],[],[],[]]
    hall = ['.' for i in range(7)]
    grid = inp.split('\n')
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y >= 2 and grid[y][x] != ' ' and grid[y][x] != '#':
                rooms[(x-1)//2-1].append(grid[y][x])
    dupes = set()
    paths = [(0,rooms,hall)]
    heapq.heapify(paths)
    while paths:
        path = heapq.heappop(paths)
        if path[1] == win:
            break
        isdupe = ' '.join([''.join(i)+'/' for i in path[1]]) + ''.join(path[2])
        if isdupe in dupes:
            continue
        dupes.add(isdupe)
        if path[2][6] == 'A': print(path)
        rooms = path[1]
        for j in range(4):
            if len(rooms[j]) >= 1 and rooms[j] != win[j] and rooms[j].count(win[j][0]) != len(rooms[j]):
                curr_rooms = deepcopy(path[1])
                curr_room = curr_rooms[j]
                start = 3-len(curr_room)
                unit = curr_room.pop(0)
                hall = copy(path[2])
                if hall[0:j+2].count('.') == j+2:
                    curr_hall = copy(hall)
                    curr_hall[0] = unit
                    heapq.heappush(paths,(path[0]+energy(start+(j+2)*2,unit),curr_rooms,curr_hall))
                for i in range(1,j+2):
                    if hall[i:j+2].count('.') == 2+j-i:
                        curr_hall = copy(hall)
                        curr_hall[i] = unit
                        heapq.heappush(paths,(path[0]+energy(start+abs((i-j-1)*2-1),unit),curr_rooms,curr_hall))
                for i in range(j+2,6):
                    if hall[j+2:i+1].count('.') == i-j-1:
                        curr_hall = copy(hall)
                        curr_hall[i] = unit
                        heapq.heappush(paths,(path[0]+energy(start+((i-j-1)*2-1),unit),curr_rooms,curr_hall))
                if hall[j+2:7].count('.') == 5-j:
                    curr_hall = copy(hall)
                    curr_hall[6] = unit
                    heapq.heappush(paths,(path[0]+energy(start+8-j*2,unit),curr_rooms,curr_hall))
        curr_hall = copy(path[2])
        unit = curr_hall[0]
        if unit != '.':
            curr_rooms = deepcopy(path[1])
            room = room_pos(unit)
            if len(curr_rooms[room]) < 2 and curr_rooms[room].count(unit) == len(curr_rooms[room]) and curr_hall[0:room+2].count('.') == len(curr_hall[0:room+2])-1:
                curr_rooms[room].append(unit)
                curr_hall[0] = '.'
                heapq.heappush(paths,(path[0]+energy(3-len(curr_rooms[room])+abs((room+1)*2),unit),curr_rooms,curr_hall))
        curr_hall = copy(path[2])
        unit = curr_hall[6]
        if unit != '.':
            curr_rooms = deepcopy(path[1])
            room = room_pos(unit)
            if len(curr_rooms[room]) < 2 and curr_rooms[room].count(unit) == len(curr_rooms[room]) and curr_hall[room+2:7].count('.') == len(curr_hall[room+2:7])-1:
                curr_rooms[room].append(unit)
                curr_hall[6] = '.'
                heapq.heappush(paths,(path[0]+energy(3-len(curr_rooms[room])+abs(10-(room+1)*2),unit),curr_rooms,curr_hall))
        for j in range(1,6):
            curr_hall = copy(path[2])
            unit = curr_hall[j]
            if unit != '.':
                curr_rooms = deepcopy(path[1])
                room = room_pos(unit)
                if len(curr_rooms[room]) < 2 and curr_rooms[room].count(unit) == len(curr_rooms[room]) and curr_hall[min(j,room+2):max(j,room+1)+1].count('.') == len(curr_hall[min(j,room+2):max(j,room+1)+1])-1:
                    curr_rooms[room].append(unit)
                    curr_hall[j] = '.'
                    heapq.heappush(paths,(path[0]+energy(3-len(curr_rooms[room])+abs(j*2-1-(room+1)*2),unit),curr_rooms,curr_hall))
    print(path[0])
        
def part2(inp):
    win = [['A','A','A','A'],['B','B','B','B'],['C','C','C','C'],['D','D','D','D']]
    rooms = [[],[],[],[]]
    hall = ['.' for i in range(7)]
    grid = inp.split('\n')
    print(grid)
    grid.insert(3,'  #D#C#B#A#')
    grid.insert(4,'  #D#B#A#C#')
    print(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y >= 2 and grid[y][x] != ' ' and grid[y][x] != '#':
                rooms[(x-1)//2-1].append(grid[y][x])
    dupes = set()
    paths = [(-2,rooms,hall)]
    heapq.heapify(paths)
    while paths:
        path = heapq.heappop(paths)
        if path[1] == win:
            break
        isdupe = ' '.join([''.join(i)+'/' for i in path[1]]) + ''.join(path[2])
        if isdupe in dupes:
            continue
        dupes.add(isdupe)
        rooms = path[1]
        for j in range(4):
            if len(rooms[j]) >= 1 and rooms[j] != win[j] and rooms[j].count(win[j][0]) != len(rooms[j]):
                curr_rooms = deepcopy(path[1])
                curr_room = curr_rooms[j]
                start = 5-len(curr_room)
                unit = curr_room.pop(0)
                hall = copy(path[2])
                if hall[0:j+2].count('.') == j+2:
                    curr_hall = copy(hall)
                    curr_hall[0] = unit
                    heapq.heappush(paths,(path[0]+energy(start+(j+2)*2,unit),curr_rooms,curr_hall))
                for i in range(1,j+2):
                    if hall[i:j+2].count('.') == 2+j-i:
                        curr_hall = copy(hall)
                        curr_hall[i] = unit
                        heapq.heappush(paths,(path[0]+energy(start+abs((i-j-1)*2-1),unit),curr_rooms,curr_hall))
                for i in range(j+2,6):
                    if hall[j+2:i+1].count('.') == i-j-1:
                        curr_hall = copy(hall)
                        curr_hall[i] = unit
                        heapq.heappush(paths,(path[0]+energy(start+((i-j-1)*2-1),unit),curr_rooms,curr_hall))
                if hall[j+2:7].count('.') == 5-j:
                    curr_hall = copy(hall)
                    curr_hall[6] = unit
                    heapq.heappush(paths,(path[0]+energy(start+8-j*2,unit),curr_rooms,curr_hall))
        curr_hall = copy(path[2])
        unit = curr_hall[0]
        if unit != '.':
            curr_rooms = deepcopy(path[1])
            room = room_pos(unit)
            if len(curr_rooms[room]) < 4 and curr_rooms[room].count(unit) == len(curr_rooms[room]) and curr_hall[0:room+2].count('.') == len(curr_hall[0:room+2])-1:
                curr_rooms[room].append(unit)
                curr_hall[0] = '.'
                heapq.heappush(paths,(path[0]+energy(5-len(curr_rooms[room])+abs((room+1)*2),unit),curr_rooms,curr_hall))
        curr_hall = copy(path[2])
        unit = curr_hall[6]
        if unit != '.':
            curr_rooms = deepcopy(path[1])
            room = room_pos(unit)
            if len(curr_rooms[room]) < 4 and curr_rooms[room].count(unit) == len(curr_rooms[room]) and curr_hall[room+2:7].count('.') == len(curr_hall[room+2:7])-1:
                curr_rooms[room].append(unit)
                curr_hall[6] = '.'
                heapq.heappush(paths,(path[0]+energy(5-len(curr_rooms[room])+abs(10-(room+1)*2),unit),curr_rooms,curr_hall))
        for j in range(1,6):
            curr_hall = copy(path[2])
            unit = curr_hall[j]
            if unit != '.':
                curr_rooms = deepcopy(path[1])
                room = room_pos(unit)
                if len(curr_rooms[room]) < 4 and curr_rooms[room].count(unit) == len(curr_rooms[room]) and curr_hall[min(j,room+2):max(j,room+1)+1].count('.') == len(curr_hall[min(j,room+2):max(j,room+1)+1])-1:
                    curr_rooms[room].append(unit)
                    curr_hall[j] = '.'
                    heapq.heappush(paths,(path[0]+energy(5-len(curr_rooms[room])+abs(j*2-1-(room+1)*2),unit),curr_rooms,curr_hall))
    print(path[0])
    
part1(inp)
part2(inp)
    