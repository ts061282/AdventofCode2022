def rightOrder(left,right):
    if (len(left) == 0 and len(right) > 0):
        return True
    for value in range(0,len(left)):
        if (value == len(right)):
            return False
        leftType = [isinstance(left[value],int),isinstance(left[value],list)]
        rightType = [isinstance(right[value],int),isinstance(right[value],list)]
        if (leftType[0] and rightType[0]):
            if (left[value] < right[value]):
                return True
            if (left[value] > right[value]):
                return False
        if (leftType[1] and rightType[1]):
            testList = rightOrder(left[value],right[value])
            if (not testList is None):
                return testList
        if (leftType[1] and rightType[0]):
            testList = rightOrder(left[value],[right[value]])
            if (not testList is None):
                return testList
        if (leftType[0] and rightType[1]):
            testList = rightOrder([left[value]],right[value])
            if (not testList is None):
                return testList
        if ((value == len(left)-1) and (value < len(right)-1)):
            return True
    return None

input = open("input.txt")

solution = 0
index = 1
left = 0
right = 0
orderedPackets = [[[2]],[[6]]]
sortDone = False

for lineNum, line in enumerate(input,1):
    # solve
    match (lineNum % 3):
        case 1:
            exec('left = ' + line.strip())
        case 2:
            exec('right = ' + line.strip())
        case 0:
            orderedPackets.append(left)
            orderedPackets.append(right)
orderedPackets.append(left)
orderedPackets.append(right)

while (not sortDone):
    sortDone = True
    for packet in range(0,len(orderedPackets)-1):
        if (not rightOrder(orderedPackets[packet],orderedPackets[packet+1])):
            orderedPackets[packet], orderedPackets[packet+1] = orderedPackets[packet+1], orderedPackets[packet]
            sortDone = False

solution = (orderedPackets.index([[2]])+1) * (orderedPackets.index([[6]])+1)

print(solution)