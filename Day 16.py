test = '''C200B40A82'''
inp = open('Day 16.txt','r').read()

def subpacket(inp):
    packet_version = int(inp[0:3],2)
    packet_type = int(inp[3:6],2)
    if packet_type == 4:
        current_bit = 6
        while inp[current_bit] != '0':
            current_bit += 5
        current_bit += 5
        return current_bit, packet_version
    else:
        if inp[6] == '0':
            sub_length = int(inp[7:22],2)
            sub_inp = 22
        elif inp[6] == '1':
            sub_length = int(inp[7:18],2)
            sub_inp = 18
        while sub_length != 0:
            sub_bit, sub_version = subpacket(inp[sub_inp:])
            sub_inp += sub_bit
            packet_version += sub_version
            if inp[6] == '0': sub_length -= sub_bit
            elif inp[6] == '1': sub_length -= 1
        return sub_inp, packet_version
    
def part1(inp):
    h_size = len(inp) * 4
    h = (bin(int(inp, 16))[2:] ).zfill(h_size)
    print(subpacket(h)[1])

from math import prod
def subpacket2(inp):
    packet_type = int(inp[3:6],2)
    if packet_type == 4:
        current_bit = 6
        value = ''
        while inp[current_bit] != '0':
            value += inp[current_bit+1:current_bit+5]
            current_bit += 5
        value += inp[current_bit+1:current_bit+5]
        current_bit += 5
        value = int(value,2)
        return current_bit, value
    else:
        if inp[6] == '0':
            sub_length = int(inp[7:22],2)
            sub_inp = 22
        elif inp[6] == '1':
            sub_length = int(inp[7:18],2)
            sub_inp = 18
        sub_values = []
        while sub_length != 0:
            sub_bit, sub_value = subpacket2(inp[sub_inp:])
            sub_inp += sub_bit
            sub_values.append(sub_value)
            if inp[6] == '0': sub_length -= sub_bit
            elif inp[6] == '1': sub_length -= 1
        match packet_type:
            case 0: return sub_inp, sum(sub_values)
            case 1: return sub_inp, prod(sub_values)
            case 2: return sub_inp, min(sub_values)
            case 3: return sub_inp, max(sub_values)
            case 5: return sub_inp, 1 if sub_values[0] > sub_values[1] else 0
            case 6: return sub_inp, 1 if sub_values[0] < sub_values[1] else 0
            case 7: return sub_inp, 1 if sub_values[0] == sub_values[1] else 0
    
def part2(inp):
    h_size = len(inp) * 4
    h = (bin(int(inp, 16))[2:]).zfill(h_size)
    print(subpacket2(h)[1])
    
part1(inp)
part2(inp)
