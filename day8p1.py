input = open("input.txt")

solution = 0

map = []

for line in input:
    line = line.strip()
    row = [int(x) for x in line]
    map.append(row)

for row in range(0, len(map)):
    for tree in range(0,len(map[row])):
        if (tree == 0):
            left = True
        else:
            left = not any(x >= map[row][tree] for x in map[row][:tree])
        if (tree == len(map[row])):
            right = True
        else:
            right = not any(x >= map[row][tree] for x in map[row][tree+1:])
        if (row == 0):
            above = True
        else:
            above = not any(x >= map[row][tree] for x in [column[tree] for column in map[:row]])
        if (row == len(map)):
            below = True
        else:
            below = not any(x >= map[row][tree] for x in [column[tree] for column in map[row+1:]])
        if (left or right or above or below):
            solution += 1

print(solution)