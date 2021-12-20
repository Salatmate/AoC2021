test = '''--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1'''.split('\n\n')
test2 = '''--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14'''.split('\n\n')
inp = open('Day 19.txt','r').read().split('\n\n')

from collections import defaultdict
from copy import deepcopy
import itertools
from math import inf
def orientation(scanner1,scanner2,index1,index2):
    orientation = deepcopy(scanner2)
    orientations = [list(itertools.permutations(i)) for i in orientation]
    for direct in range(len(orientations)):
        orientations[direct][1] = tuple([j*-1 for j in orientations[direct][1]])
        orientations[direct][2] = tuple([j*-1 for j in orientations[direct][2]])
        orientations[direct][5] = tuple([j*-1 for j in orientations[direct][5]])
        for x,y,z in orientations[direct][:6]:
            orientations[direct].append((x,-z,y))
            orientations[direct].append((x,-y,-z))
            orientations[direct].append((x,z,-y))
    coords = scanner1[index1]
    coords2 = orientations[index2]
    orient = deepcopy(orientations)
    for i in range(24):
        matching = 0
        coords1 = tuple(val1-val2 for val1,val2 in zip(coords,coords2[i]))
        for beacons in range(len(orientations)):
            orient[beacons][i] = tuple(val1+val2 for val1,val2 in zip(orient[beacons][i],coords1))
            if orient[beacons][i] in scanner1:
                matching += 1
        if matching >= 12:
            break
    orient = [j[i] for j in orient]
    offset = (x,y,z)
    return orient, offset

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def overlap(scanner1,scanner2):
    for index1,coord1 in enumerate(scanner1):
        distance1 = set()
        for i in scanner1:
            distance1.add(manhattan(coord1,i))
        for index2,coord2 in enumerate(scanner2):
            distance2 = set()
            for i in scanner2:
                distance2.add(manhattan(coord2,i))
            if len(distance1 & distance2) >= 12:
                return True, index1, index2
    return False, index1, index2
    
def part1(inp):
    scanners = defaultdict(list)
    scan_pos = defaultdict(tuple)
    scan_pos[0] = (0,0,0)
    for scanner in range(len(inp)):
        for beacon in inp[scanner].split('\n')[1:]:
            scanners[scanner].append(tuple([int(i) for i in beacon.split(',')]))
    beacon_map = scanners[0]
    checked = [0]
    done = []
    while checked:
        scan = checked.pop(0)
        done.append(scan)
        for i in range(len(scanners)):
            if i not in done and i not in checked:
                matched, index1, index2 = overlap(scanners[scan],scanners[i])
                if matched:
                    checked.append(i)
                    orient, offset = orientation(scanners[scan],scanners[i],index1,index2)
                    scanners[i] = orient
                    beacon_map += orient
    beacon_map.sort()
    print(len(list(beacon_map for beacon_map,_ in itertools.groupby(beacon_map))))
                
    
def part2(inp):
    scanners = defaultdict(list)
    scan_pos = defaultdict(tuple)
    scan_pos[0] = (0,0,0)
    for scanner in range(len(inp)):
        for beacon in inp[scanner].split('\n')[1:]:
            scanners[scanner].append(tuple([int(i) for i in beacon.split(',')]))
    checked = [0]
    done = []
    offsets = []
    while checked:
        scan = checked.pop(0)
        done.append(scan)
        for i in range(len(scanners)):
            if i not in done and i not in checked:
                matched, index1, index2 = overlap(scanners[scan],scanners[i])
                if matched:
                    checked.append(i)
                    orient, offset = orientation(scanners[scan],scanners[i],index1,index2)
                    scanners[i] = orient
                    offsets.append(offset)
    greatest = 0
    for i in itertools.combinations(offsets,2):
        greatest = max(manhattan(i[0],i[1]),greatest)
    print(greatest)
    
part1(inp)
part2(inp)
