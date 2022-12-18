#import os for screen/terminal clearing
import os
#import time to delay for reasonable refresh rate
import time
#import copy to evaluate changes in rock coordingates
import copy

def screenUpdate(rock,rockCoords):
    os.system("cls")
    c = addRockToChamber(copy.deepcopy(chamber), rock, rockCoords)
    screenLines = 0
    for line in reversed(c):
        if (screenLines<=30):
            screenLines += 1
            print('|' + line + '|')
    print("+-------+")
    print(jets[jetIndex])

#read in jet stream
inputF = open("input.txt")
jets = ''
for line in inputF:
    jets += line.strip()

#function to return next jet in jet stream
jetIndex = 0
def getNextJet():
    global jetIndex
    jet = jets[jetIndex]
    jetIndex += 1
    if jetIndex == len(jets):
        jetIndex = 0
    return jet

#define canonical rocks
rocks = []
rock = ['####']
rocks.append(rock)
rock = ['.#.','###','.#.']
rocks.append(rock)
rock = ['###','..#','..#']
rocks.append(rock)
rock = ['#','#','#','#']
rocks.append(rock)
rock = ['##','##']
rocks.append(rock)

#function to return next rock in cycle
rockIndex = 0
def getNextRock():
    global rockIndex
    rock = rocks[rockIndex]
    rockIndex += 1
    if rockIndex == len(rocks):
        rockIndex = 0
    return rock

#function to set up initial chamber floor
chamberWidth = 7
chamber = []
chamberFloor = ''
for y in range(0,chamberWidth):
    chamberFloor += '#'
chamber.append(chamberFloor)

#locate new rock based on existing chamber
#top,left (rock[0][0]) corner of rock is coordinate of entire rock
def rockSpawnCoords(rock):
    rockX = 2
    rockY = 0
    for line in range(len(chamber)-1,-1,-1):
        if '#' in chamber[line]:
            rockY = line + 4
            break
    return [rockY,rockX]

#check if rock is overlapping cavern
def overlappingRock(rock,rockCoords):
    overlapping = False 
    for rockY in range(0,len(rock)):
        for rockX in range(0,len(rock[rockY])):
            if len(chamber) > rockY + rockCoords[0]:
                if chamberWidth > (rockX + rockCoords[1]):
                    if (rock[rockY][rockX] == '#' and chamber[rockY + rockCoords[0]][rockX + rockCoords[1]] == '#'):
                        overlapping = True
    return overlapping

#push rock according to jetstream
def pushRock(rock,rockCoords):
    global chamberWidth
    jet = getNextJet()
    if (jet == '<'):
        if (rockCoords[1] > 0):
            if (not overlappingRock(rock,[rockCoords[0],rockCoords[1]-1])):
                rockCoords[1] -= 1
    elif (not (rockCoords[1] + len(rock[0]) >= chamberWidth)):
        if (not overlappingRock(rock,[rockCoords[0],rockCoords[1]+1])):
            rockCoords[1] += 1
    return rockCoords

#drop rock by gravity
def dropRock(rock,rockCoords):
    if (not overlappingRock(rock,[rockCoords[0]-1,rockCoords[1]])):
        rockCoords[0] -= 1
    return rockCoords

#update rock and return new coords
def updateRock(rock, rockCoords):
    rockCoords = pushRock(rock, rockCoords)
    rC = copy.deepcopy(rockCoords)
    rockCoords = dropRock(rock, rockCoords)
    # screenUpdate(rock,rockCoords)
    return (not rC == rockCoords)

#add new rock to chamber structure
def addRockToChamber(chamber,rock,coords):
    for y in range(0,len(rock)):
        for x in range(0,len(rock[y])):
            if rock[y][x] == '#':
                while (not len(chamber) > coords[0]+y):
                    newline = ''
                    for char in range(0,chamberWidth):
                        newline += ' '
                    chamber.append(newline)
                chamberX = coords[1] + x
                chamber[coords[0]+y] = chamber[coords[0]+y][:chamberX] + rock[y][x] + chamber[coords[0]+y][chamberX+1:]
    return chamber

#main program loop
rockCount = 0
rocksToAdd = 2022
while (rockCount < rocksToAdd):
    rockCount += 1
    rock = getNextRock()
    coords = rockSpawnCoords(rock)
    # screenUpdate(rock,coords)
    # userInput = input("press any key...")
    while (updateRock(rock, coords)):
        pass #userInput = input("press any key...")
    # userInput = input("press any key...")
    chamber = addRockToChamber(chamber,rock,coords)

for line in range(len(chamber)-1,-1,-1):
    if '#' in chamber[line]:
        print(line)
        break