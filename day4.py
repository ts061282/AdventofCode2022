input = open("OneDrive\\Documents\\input.txt")

count = 0



for line in input:
    assignments = line.split(',')
    assignments[1] = assignments[1].strip()
    sections1 = assignments[0].split("-")
    sections2 = assignments[1].split("-")
    assignment1 = []
    assignment2 = []
    assignment1.extend(range(int(sections1[0]), int(sections1[1])+1))
    assignment2.extend(range(int(sections2[0]), int(sections2[1])+1))
    intersect = list(set(assignment1).intersection(set(assignment2)))
    print(line)
    print(intersect)
    if (len(intersect) > 0):
        count += 1
        print("Here's one")

print(count)
