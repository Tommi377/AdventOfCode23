import math
import time
filename = "input.txt"
start = time.time()

def parseline(line):
    return list(map(lambda x: int(x), line.split()))

def parsevalues(arr, d, s, l):
    res = []
    toRemove = []
    toAdd = []
    for (i, j) in arr:
        if i >= s and i < s + l and i + j - 1 >= s and i + j - 1 < s + l:
            start = d + i - s
            length = j
            res.append((start, length))
            toRemove.append((i, j))
        elif i >= s and i < s + l:
            start = d + i - s
            length = s + l - i
            res.append((start, length))
            toAdd.append((s + l, i + j - s - l))
            toRemove.append((i, j))
        elif i + j - 1 >= s and i + j - 1 < s + l:
            start = d
            length = i + j - s
            res.append((start, length))
            toAdd.append((i, j - length))
            toRemove.append((i, j))
        elif i < s and i + j - 1 >= s + l:
            res.append((d, l))
            toAdd.append((i, s - i))
            toAdd.append((s + l, i + j - s - l))
            toRemove.append((i, j))
    
    for r in toRemove:
        arr.remove(r)
        
    for a in toAdd:
        arr.append(a)
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
    seedval = list(map(lambda x: int(x), fp.readline().split()[1:]))
    seed = []
    for i in range(0, len(seedval), 2):
        seed.append((seedval[i], seedval[i + 1]))
    
    fp.readline()
        
    soil = parsesection(seed)
    fert = parsesection(soil)
    water = parsesection(fert)
    light = parsesection(water)
    temp = parsesection(light)
    humid = parsesection(temp)
    loc = parsesection(humid)
    
    best = math.inf
    for (i, j) in loc:
        best = min(i, best)

    print(best)
    
end = time.time()

print(f"Run time: {end-start}")