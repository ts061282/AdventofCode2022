class main:
    f = open("C:\\Users\\tylon\\OneDrive\\Documents\\input.txt")

    score = 0

    for line in f:
        plays = line.strip().split(' ')
        print(score)
        match plays[1]:
            case 'X':
                match plays[0]:
                    case 'A':
                        score += 3
                    case 'B':
                        score += 1
                    case 'C':
                        score += 2
            case 'Y':
                match plays[0]:
                    case 'A':
                        score += 4
                    case 'B':
                        score += 5
                    case 'C':
                        score += 6
            case 'Z':
                match plays[0]:
                    case 'A':
                        score += 8
                    case 'B':
                        score += 9
                    case 'C':
                        score += 7

    print ('the score is: ')
    print(score)