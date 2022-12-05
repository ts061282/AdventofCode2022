class Main:

    f = open("C:\\Users\\tylon\\OneDrive\\Documents\\input.txt")

    global food
    global foodstore

    food = 0
    foodstore = []

    for line in f:
        if (line == '\n'):
            foodstore.append(food)
            food = 0
        else:
            food = food + int(line)

    foodstore.sort()
    foodstore.reverse()
    
    print("The most food is: ")
    print(foodstore[0])
    print("The second most food is: ")
    print(foodstore[1])
    print("The third most food is: ")
    print(foodstore[2])
    print("The total of the top three most food stores is: ")
    print(foodstore[0] + foodstore[1] + foodstore[2])
