input = open("input.txt")

solution = 0
input_map = []
visited = []
paths = []
start = [0,0]
end = [0,0]
foundEnd = False

for line in input:
    input_map.append([(ord(char) - ord('a')) for char in line.strip()])

for line in range(0,len(input_map)):
    for col in range(0,len(input_map[line])):
        if (input_map[line][col] == -14):
            input_map[line][col] = 0
            start = [col, line]
            visited.append(start)
            paths.append([start])
        if (input_map[line][col] == -28):
            input_map[line][col] = 25
            end = [col, line]

while (not foundEnd):
    for path in paths:
        lastNode = path[-1]
        neighbors = [[lastNode[0]-1,lastNode[1]],[lastNode[0]+1,lastNode[1]],[lastNode[0],lastNode[1]-1],[lastNode[0],lastNode[1]+1]]
        for neighbor in neighbors:
            if (neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[1] < len(input_map) and neighbor[0] < len(input_map[0])):
                if (not neighbor in visited):
                    if (input_map[neighbor[1]][neighbor[0]] - input_map[lastNode[1]][lastNode[0]] <= 1):
                        paths.append(path + [neighbor])
                        visited.append(neighbor)
                        if neighbor == end:
                            foundEnd = True

for path in paths:
    if (end in path):
        print(len(path)-1)
        break