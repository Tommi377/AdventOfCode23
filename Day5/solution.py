import math
filename = "input.txt"

def parseline(line):
    return list(map(lambda x: int(x), line.split()))

def parsevalues(arr, d, s, l):
    res = []
    toRemove = []
    for i in arr:
        if i >= s and i < s + l:
            res.append(d + i - s)
            toRemove.append(i)
    
    for r in toRemove:
        arr.remove(r)        
    
    return res
            

def parsesection(arr):
    fp.readline()
    work = arr.copy()
    res = []
    while True:
        line = fp.readline()
        if len(line) < 3: break;
        res += parsevalues(work, *parseline(line))
    return res + work

with open(filename) as fp:
    # seed
    seeds = list(map(lambda x: int(x), fp.readline().split()[1:]))
    
    fp.readline()
        
    soil = parsesection(seeds)
    fert = parsesection(soil)
    water = parsesection(fert)
    light = parsesection(water)
    temp = parsesection(light)
    humid = parsesection(temp)
    loc = parsesection(humid)
    
    best = math.inf
    for v in loc:
        best = min(v, best)

    print(best)