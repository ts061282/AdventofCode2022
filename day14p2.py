import math
import os

def getLowestPoint():
    lowestpoint = 0
    for point in cavern:
        if (point[1] > lowestpoint):
            lowestpoint = point[1]
    return lowestpoint

def updateDisplay():
    os.system("cls")
    for y in range(0,getLowestPoint()+1):
        outline = ""
        for x in range(450,550):
            if ([x,y] in cavern):
                outline += "#"
            else:
                outline += "."
        print(outline)  

input_file = open("input.txt")

solution = 0

cavern = []

for line in input_file:
    line = line.strip()
    line = line.split(' -> ')
    lastcoord = []
    for coord in line:
        coord = [int(x) for x in coord.split(',')]
        if (lastcoord == []):
            if (not [coord[0],coord[1]] in cavern):
                cavern.append([coord[0],coord[1]])
        else:
            if (coord[0] == lastcoord[0]):
                step = int(math.copysign(1,coord[1]-lastcoord[1]))
                for y in range(lastcoord[1]+step,coord[1]+step,step):
                    if (not [coord[0],y] in cavern):
                        cavern.append([coord[0],y])
            if (coord[1] == lastcoord[1]):
                step = int(math.copysign(1,coord[0]-lastcoord[0]))
                for x in range(lastcoord[0]+step,coord[0]+step,step):
                    if (not [x,coord[1]] in cavern):
                        cavern.append([x,coord[1]])
        lastcoord = coord
    #   updateDisplay()
    # print(line)
    # print(cavern)
    # userinput = input("Press any key...")


lowPoint = getLowestPoint()
floor = 2 + lowPoint
for x in range(500-floor,500+floor+1):
    cavern.append([x,floor])

sandCount = 0
sandBlocked = False
while (not sandBlocked):
    # updateDisplay()
    sand = [500,0]
    sandStopped = False
    while (not sandStopped):
        if (not [sand[0],sand[1]+1] in cavern):
            sand = [sand[0],sand[1]+1]
        elif (not [sand[0]-1, sand[1]+1] in cavern):
            sand = [sand[0]-1, sand[1]+1]
        elif (not [sand[0]+1, sand[1]+1] in cavern):
            sand = [sand[0]+1, sand[1]+1]
        else:
            cavern.append(sand)
            sandStopped = True
            sandCount += 1
        if (sand == [500,0]):
            print(sand)
            sandStopped = True
            sandBlocked = True
    if (sand[1]%100 ==0):
        print(sand)


print(sandCount)