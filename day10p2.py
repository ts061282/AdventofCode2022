def updateScreen(screen, cycle, x):
    charPos = (cycle-1) % 40
    if (charPos in range(x-1,x+2)):
        char = '#'
    else:
        char = '.'
    return screen[int((cycle-1) / 40)].append(char)



input = open("input.txt")
screen = [[],[],[],[],[],[]]
x = 1
cycle = 0

for line in input:
    line = line.strip()
    line = line.split(" ")

    cycle += 1
    updateScreen(screen, cycle, x)
    if (not line[0] == "noop"):
        cycle += 1
        updateScreen(screen, cycle, x)
        x += int(line[1])

for rows in range(0,len(screen)):
    row = ""
    for chars in screen[rows]:
        row += str(chars)
    print(row)


    