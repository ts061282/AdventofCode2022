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

slice = 2000000

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

coveredBeacons = 0
beaconX = []

for sensorSet in sensors:
    beacon = sensorSet["beacon"]
    if (beacon[1] == slice):
        if (not beacon[1] in beaconX):
            beaconX.append(beacon[1])
for x in beaconX:     
    for coverage in sliceCoverage:
        if (coverage[0] <= x <= coverage[1]):
            coveredBeacons += 1

totalCoverage = 0

for coverage in sliceCoverage:
    totalCoverage += coverage[1] - coverage[0] + 1

coverage = totalCoverage - coveredBeacons

print(coverage)