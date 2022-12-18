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

print(openFaces)