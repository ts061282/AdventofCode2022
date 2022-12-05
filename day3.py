input = open("OneDrive\\Documents\\input.txt")

tally = 0
line = input.readline().strip()
line2 = input.readline().strip()
line3 = input.readline().strip()

while (line != ""):
    line = set(line)
    line2 = set(line2)
    line3 = set(line3)
    commonitem = (line & line2) & line3
    commonitem = commonitem.pop()
    commonitem = ord(commonitem)-96
    if commonitem <= 0:
        commonitem += 58
    tally += commonitem
    print(tally)
    line = input.readline().strip()
    line2 = input.readline().strip()
    line3 = input.readline().strip()

print(tally)
