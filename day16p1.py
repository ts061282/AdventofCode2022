def getAvgFlow():
    tally = 0
    for r in routes:
        tally += r['tallyFlow']
    return(tally / len(routes))

def getRate(location):
    for v in valves:
        if (v['valve'] == location):
            return v['rate']

def getPaths(location):
    for v in valves:
        if (v['valve'] == location):
            return v['paths']

input = open("input.txt")

solution = 0

valves = []

# 13; tunnels lead to valves CC, AA

for line in input:
    line=line.strip()
    valve = line[6:8]
    line = line[23:]
    rate = line.split(';')
    rate = rate[0]
    line = line[25:]
    line = line.split(" ")
    del(line[0])
    paths = []
    for v in line:
        paths.append(v.strip(','))
    valves.append({'valve':valve,'rate':int(rate),'paths':paths})

routes = []
timeLimit = 30
startValve = 'AA'
valvesOn = []
startRate = 0
routes.append({'location':startValve,'lastLocation':startValve,'activated':valvesOn,'tallyFlow':startRate,'timeLeft':timeLimit})
while any(r['timeLeft'] for r in routes):
    for rIndex in range(0,len(routes)): 
        r = routes[rIndex]
        if (r['timeLeft']):
            if(len(routes)<=200 or (r['timeLeft'] > 18 and r['tallyFlow']>=(0.75*getAvgFlow())) or (r['timeLeft'] <= 18 and r['tallyFlow']>=(0.99*getAvgFlow()))):
                if (not r['location'] in r['activated']):
                    routes.append({'location':r['location'],'lastLocation':r['location'],'activated':(r['activated'] + [r['location']]),'tallyFlow':r['tallyFlow'] + ((getRate(r['location'])*(r['timeLeft']-1))),'timeLeft':r['timeLeft']-1})
                for p in getPaths(r['location']):
                    if (not p == r['lastLocation']):
                        routes.append({'location':p,'lastLocation':r['location'],'activated':r['activated'],'tallyFlow':r['tallyFlow'],'timeLeft':r['timeLeft']-1})
    routes = routes[rIndex+1:]

topFlow = 0
bestRoute = 0
for r in routes:
    if (r['tallyFlow'] > topFlow):
        bestRoute = r
        topFlow = r['tallyFlow']

print(bestRoute)

print(sorted(x['tallyFlow'] for x in routes)[-1])