input = open("input.txt")

solution = 0

for line in input:
    for char in range(4, len(line)):
        signal = set(line[char-4:char])
        if len(signal) == 4:
            print(char)
            break
