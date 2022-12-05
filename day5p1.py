input = open("input.txt")

solution = ""

stack1 = 'NBDTVGZJ'
stack2 = 'SRMDWPF'
stack3 = 'VCRSZ'
stack4 = 'RTJZPHG'
stack5 = 'TCJNDZQF'
stack6 = 'NVPWGSFM'
stack7 = 'GCVBPQ'
stack8 = 'ZBPN'
stack9 = 'WPJ'
stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

for line in input:
    # solve
    moves = int(line.split(" from ")[0].split("move ")[1])
    source = int(line.split(" from ")[1].split(" to ")[0])
    destination = int(line.split(" to ")[1].strip())
    for move in range(1, moves+1):
        stacks[destination-1] += stacks[source-1][-1]
        stacks[source-1] = stacks[source-1][:-1]

        
for stack in stacks:
    solution += stack[-1]

print(solution)