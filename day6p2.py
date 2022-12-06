input = open("input.txt")

solution = 0

for line in input:
    for char in range(14, len(line)):
        signal = set(line[char-14:char])
        if len(signal) == 14:
            print(char)
            break
