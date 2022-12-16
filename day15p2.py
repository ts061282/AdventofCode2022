def countSlice(sensorSet, slice):
    sensor = sensorSet["sensor"]
    beacon = sensorSet["beacon"]
    sensorRange = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    if ((sensor[1] - sensorRange) <= slice <= (sensor[1] + sensorRange)):
        yoffset = abs(sensor[1] - slice)
        xrange = sensorRange - yoffset
        return([sensor[0]-xrange,sensor[0]+xrange])

input = open("input.txt")

sensors = []

for line in input:
    line = line.strip()
    line = line[10:]
    line = line.split(":")
    line[0] = line[0].split(', ')
    sensor = [int(line[0][0][2:]),int(line[0][1][2:])]
    line[1] = line[1][22:]
    line[1] = line[1].split(', ')
    beacon = [int(line[1][0][2:]),int(line[1][1][2:])]
    sensors.append({"sensor":sensor,"beacon":beacon})

distressX = -1
distressMax = 4000000

for slice in range(0,distressMax+1):

    sliceCoverage = []

    for sensorSet in sensors:
        sensorSlice = countSlice(sensorSet, slice)
        addSensorSlice = True
        if (not sensorSlice == None):
            for coverage in sliceCoverage:
                if (coverage[0] <= sensorSlice[0] <= coverage[1]) or (coverage[0] <= sensorSlice[1] <= coverage[1]):
                    expandedCoverage = [sorted([coverage[0],sensorSlice[0]])[0],sorted([coverage[1],sensorSlice[1]])[1]]
                    sliceCoverage.append(expandedCoverage)
                    sliceCoverage.remove(coverage)
                    addSensorSlice = False
            if (addSensorSlice):
                sliceCoverage.append(sensorSlice)

    lastLen = 0
    while (not lastLen == len(sliceCoverage)):
        lastLen = len(sliceCoverage)
        for coverage in sliceCoverage:
            for othercoverage in sliceCoverage:
                if (not othercoverage == coverage):
                    if (othercoverage[0] <= coverage[0] <= othercoverage[1]) or (othercoverage[0] <= coverage[1] <= othercoverage[1]):
                        expandedCoverage = [sorted([othercoverage[0],coverage[0]])[0],sorted([othercoverage[1],coverage[1]])[1]]
                        sliceCoverage.append(expandedCoverage)
                        sliceCoverage.remove(othercoverage)
                        sliceCoverage.remove(coverage)
                        break

    for coverage in sliceCoverage:
        if (not(coverage[0] <= 0 and coverage[1] >= distressMax)):
            if (coverage[0] <= 0 or coverage[1] >= distressMax):
                if (0 < coverage[0] <= distressMax):
                    distressX = coverage[0] -1
                else:
                    distressX = coverage[1] + 1
                break

    if (distressX >= 0):
        print(distressX * 4000000 + slice)
        break
    


