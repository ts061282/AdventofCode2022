input = open("input.txt")

solution = 0

map = []

for line in input:
    line = line.strip()
    row = [int(x) for x in line]
    map.append(row)

for row in range(0, len(map)):
    for tree in range(0,len(map[row])):
        viewTally = 0
        scenicScore = 1
        if map[row][:tree]:
            for x in map[row][:tree][::-1]:
                viewTally += 1
                if x >= map[row][tree]:
                    break
        scenicScore *= viewTally
        viewTally=0
        if map[row][tree+1:]:
            for x in map[row][tree+1:]:
                viewTally += 1
                if x >= map[row][tree]:
                    break
        scenicScore *= viewTally
        viewTally=0
        if [column[tree] for column in map[:row]]:
            for x in [column[tree] for column in map[:row]][::-1]:
                viewTally += 1
                if x >= map[row][tree]:
                    break
        scenicScore *= viewTally
        viewTally=0
        if [column[tree] for column in map[row+1:]]:
            for x in [column[tree] for column in map[row+1:]]:
                viewTally += 1
                if x >= map[row][tree]:
                    break
        scenicScore *= viewTally
        if (scenicScore > solution):
            solution = scenicScore

print(solution)