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
timeLimit = 26
startValve = 'AA'
valvesOn = []
startRate = 0
routes.append({'location':startValve,'lastLocation':startValve,'elocation':startValve,'elastLocation':startValve,'activated':valvesOn,'tallyFlow':startRate,'timeLeft':timeLimit})
while any(r['timeLeft'] for r in routes):
    for rIndex in range(0,len(routes)): 
        r = routes[rIndex]
        if (r['timeLeft']):
            if(len(routes)<=1600 or (r['timeLeft'] > 16 and r['tallyFlow']>=((len(routes)/1600*getAvgFlow()))) or (r['timeLeft'] <= 16 and r['tallyFlow']>=(getAvgFlow()))):
                if (not r['location'] in r['activated'] and getRate(r['location'])):
                    if (not r['elocation'] in r['activated'] and getRate(r['elocation'])):
                        if(not r['location'] == r['elocation']):
                            routes.append({'location':r['location'],'lastLocation':r['location'],'elocation':r['elocation'],'elastLocation':r['elocation'],'activated':(r['activated'] + [r['location']] + [r['elocation']]),'tallyFlow':r['tallyFlow'] + ((getRate(r['location'])*(r['timeLeft']-1))) + ((getRate(r['elocation'])*(r['timeLeft']-1))),'timeLeft':r['timeLeft']-1})
                    for ep in getPaths(r['elocation']):
                        if (not ep == r['elastLocation']):
                            routes.append({'location':r['location'],'lastLocation':r['location'],'elocation':ep,'elastLocation':r['elocation'],'activated':(r['activated'] + [r['location']]),'tallyFlow':r['tallyFlow'] + ((getRate(r['location'])*(r['timeLeft']-1))),'timeLeft':r['timeLeft']-1})
                for p in getPaths(r['location']):
                    if (not p == r['lastLocation']):
                        if (not r['elocation'] in r['activated'] and getRate(r['elocation'])):
                            routes.append({'location':p,'lastLocation':r['location'],'elocation':r['elocation'],'elastLocation':r['elocation'],'activated':r['activated'] + [r['elocation']],'tallyFlow':r['tallyFlow'] + ((getRate(r['elocation'])*(r['timeLeft']-1))),'timeLeft':r['timeLeft']-1})
                        for ep in getPaths(r['elocation']):
                            if (not ep == r['elastLocation']):
                                routes.append({'location':p,'lastLocation':r['location'],'elocation':ep,'elastLocation':r['elocation'],'activated':r['activated'],'tallyFlow':r['tallyFlow'],'timeLeft':r['timeLeft']-1})
    routes = routes[rIndex+1:]

topFlow = 0
bestRoute = 0
for r in routes:
    if (r['tallyFlow'] > topFlow):
        bestRoute = r
        topFlow = r['tallyFlow']

print(bestRoute)

print(sorted(x['tallyFlow'] for x in routes)[-1])