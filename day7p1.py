def sumDir(dir):
    global solution
    dirSum = 0
    for items in dir.values():
        if type(items) == int:
            dirSum += items
        else:
            dirSum += sumDir(items)
    if dirSum <= 100000:
        solution += dirSum
    return dirSum

input = open("input.txt")

solution = 0
cd = {}
path = [cd]

for line in input:
    line = line.strip()
    args = line.split(" ")
    match args[0]:
        case "$":
            match args[1]:
                case "cd":
                    if (args[2] == ".."):
                        cd = path[-2]
                        path = path[:-1]
                    else:
                        if (args[2] not in cd):
                            cd.update({args[2]:{}})
                        cd = cd[args[2]]
                        path.append(cd)
                # case "ls": do nothing                    
        case "dir":
            cd.update({args[1]:{}})
        case other:  #file
            cd.update({args[1]:int(args[0])})

sumDir(path[0])
print(solution)
