import math

def updateTail(headPos, tailPos):
    diffPos = [headPos[0] - tailPos[0], headPos[1] - tailPos[1]]
    if (abs(diffPos[0])>1 and abs(diffPos[1])>1):
        return [tailPos[0] + int(math.copysign(1, diffPos[0])), tailPos[1] + int(math.copysign(1,diffPos[1]))]
    elif (abs(diffPos[0])>1 and abs(diffPos[1])==1):
        return [tailPos[0] + int(math.copysign(1, diffPos[0])), tailPos[1] + int(math.copysign(1,diffPos[1]))]
    elif (abs(diffPos[0])==1 and abs(diffPos[1])>1):
        return [tailPos[0] + int(math.copysign(1, diffPos[0])), tailPos[1] + int(math.copysign(1,diffPos[1]))]
    elif (abs(diffPos[0])>1):
        return [tailPos[0] + int(math.copysign(1, diffPos[0])), tailPos[1]]
    elif (abs(diffPos[1])>1):
        return [tailPos[0], tailPos[1] + int(math.copysign(1,diffPos[1]))]
    else:  
        return tailPos

input = open("input.txt")

solution = 0

tail = [0,0]
head = [0,0]
tailTrace = [tail]

for line in input:
    line = line.strip()
    line = line.split(" ")
    for step in range(1, int(line[1])+1):
        match line[0]:
            case 'R':
                head[0] += 1
            case 'L':
                head[0] -= 1
            case 'U':
                head[1] += 1
            case 'D':
                head[1] -= 1        
        tail = updateTail(head, tail)
        if tail not in tailTrace:
            tailTrace.append(tail)

print(len(tailTrace))