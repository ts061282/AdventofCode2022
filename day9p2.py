import math

def updateKnot(headPos, tailPos):
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

knots = []
for knot in range(0,10):
    knots.append([0,0])
tailTrace = [knots[-1]]

for line in input:
    line = line.strip()
    line = line.split(" ")
    for step in range(1, int(line[1])+1):
        match line[0]:
            case 'R':
                knots[0][0] += 1
            case 'L':
                knots[0][0] -= 1
            case 'U':
                knots[0][1] += 1
            case 'D':
                knots[0][1] -= 1
        for knot in range(1,10):
            knots[knot] = updateKnot(knots[knot-1], knots[knot])
        if knots[9] not in tailTrace:
            tailTrace.append(knots[9])

print(len(tailTrace))