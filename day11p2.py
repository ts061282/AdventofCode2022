input = open("input.txt")

solution = 0
monkeys = []
monkey = 0
manageMod = 1

for line in input:
    line = line.strip()
    if (not line == ""):
        match (line[0:6]):
            case "Monkey":
                monkey = int(line[7:8])
            case "Starti":
                monkeys.append({"items": [int(x) for x in line[16:].split(", ")]})
                monkeys[monkey].update({"tally": 0})
            case "Operat":
                monkeys[monkey].update({"op":line.split(": ")[1]})
            case "Test: ":
                monkeys[monkey].update({"test":int(line[19:])})
                manageMod *= int(line[19:])
            case "If tru":
                monkeys[monkey].update({"true":int(line[25:])})
            case "If fal":
                monkeys[monkey].update({"false":int(line[26:])})

for round in range(1,10001):
    for monkey in range(0,len(monkeys)):
        items = len(monkeys[monkey].get("items"))
        for item in range(0,items):
            roundMonkey = monkeys[monkey]
            old = roundMonkey.get("items").pop()
            exec(monkeys[monkey].get("op"))
            new = new % manageMod
            if (new % monkeys[monkey].get("test") == 0):
                updateMonk = monkeys[monkeys[monkey].get("true")]
            else:
                updateMonk = monkeys[monkeys[monkey].get("false")]
            updateMonk.get("items").append(new)
            roundMonkey["tally"] += 1

monkeys = sorted(monkeys, key=lambda d: d["tally"])
solution = monkeys[-2]["tally"] * monkeys[-1]["tally"]

print(solution)