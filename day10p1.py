def tallySignal(cycle, x):
    if (cycle in range(20, 261, 40)):
        return(cycle * x)
    else:
        return 0

input = open("input.txt")

solution = 0
x = 1
cycle = 0

for line in input:
    line = line.strip()
    line = line.split(" ")

    cycle += 1
    solution += tallySignal(cycle, x)
    if (not line[0] == "noop"):
        cycle += 1
        solution += tallySignal(cycle, x)
        x += int(line[1])
    

print(solution)