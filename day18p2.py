def trapped(x,y,z):
    global grid
    searching = []
    searched = []
    searching.append([x,y,z])
    trap = True
    while (trap):
        for path in searching:
            if (minX <= path[0] <= maxX and minY <= path[1] <= maxY and minZ <= path[2] <= maxZ):
                testing = [path[0]-1,path[1],path[2]]
                if (testing in inclusions):
                    return True
                if (not testing in grid and not testing in searched):
                    searching.append(testing)
                testing = [path[0]+1,path[1],path[2]]
                if (testing in inclusions):
                    return True
                if (not testing in grid and not testing in searched):
                    searching.append(testing)
                testing = [path[0],path[1]-1,path[2]]
                if (testing in inclusions):
                    return True
                if (not testing in grid and not testing in searched):
                    searching.append(testing)
                testing = [path[0],path[1]+1,path[2]]
                if (testing in inclusions):
                    return True
                if (not testing in grid and not testing in searched):
                    searching.append(testing)
                testing = [path[0],path[1],path[2]-1]
                if (testing in inclusions):
                    return True
                if (not testing in grid and not testing in searched):
                    searching.append(testing)
                testing = [path[0],path[1],path[2]+1]
                if (testing in inclusions):
                    return True
                if (not testing in grid and not testing in searched):
                    searching.append(testing)
            else:
                return False
            searched.append(path)
            searching.remove(path)
        if (len(searching) == 0):
            return True

input = open("input.txt")

grid = []

for line in input:
    line = line.strip()
    line = line.split(',')
    grid.append([int(line[0]),int(line[1]),int(line[2])])

openFaces = 0
for cube in grid:
    if (not [cube[0]-1,cube[1],cube[2]] in grid):
        openFaces += 1
    if (not [cube[0]+1,cube[1],cube[2]] in grid):
        openFaces += 1
    if (not [cube[0],cube[1]-1,cube[2]] in grid):
        openFaces += 1
    if (not [cube[0],cube[1]+1,cube[2]] in grid):
        openFaces += 1
    if (not [cube[0],cube[1],cube[2]-1] in grid):
        openFaces += 1
    if (not [cube[0],cube[1],cube[2]+1] in grid):
        openFaces += 1

minX = 100
maxX = 0
minY = 100
maxY = 0
minZ = 100
maxZ = 0
for cube in grid:
    if (cube[0] > maxX):
        maxX = cube[0]
    if (cube[0] < minX):
        minX = cube[0]
    if (cube[1] > maxY):
        maxY = cube[1]
    if (cube[1] < minY):
        minY = cube[1]
    if (cube[2] > maxZ):
        maxZ = cube[2]
    if (cube[2] < minZ):
        minZ = cube[2]

inclusions = []
for x in range(minX, maxX):
    for y in range(minY, maxY):
        for z in range(minZ, maxZ):
            if (not [x,y,z] in grid):
                if (trapped(x,y,z)):
                    inclusions.append([x,y,z])

for inclusion in inclusions:
    if ([inclusion[0]-1,inclusion[1],inclusion[2]] in grid):
        openFaces -= 1
    if ([inclusion[0]+1,inclusion[1],inclusion[2]] in grid):
        openFaces -= 1
    if ([inclusion[0],inclusion[1]-1,inclusion[2]] in grid):
        openFaces -= 1
    if ([inclusion[0],inclusion[1]+1,inclusion[2]] in grid):
        openFaces -= 1
    if ([inclusion[0],inclusion[1],inclusion[2]-1] in grid):
        openFaces -= 1
    if ([inclusion[0],inclusion[1],inclusion[2]+1] in grid):
        openFaces -= 1

print(openFaces)