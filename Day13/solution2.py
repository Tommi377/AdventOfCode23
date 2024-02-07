import math
import time

filename = "input.txt"
starttime = time.time()

doprint = True
def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def solve(mp, vals, mul):
    n = len(mp)
    m = len(mp[0])
    for i in range(0, n - 1):
        o = 0
        used = False
        while (vals[i - o] == vals[i + 1 + o] and mp[i - o] == mp[i + 1 + o]) or (not used and abs(vals[i - o] - vals[i + 1 + o]) == 1):
            if vals[i - o] != vals[i + 1 + o] and not used:
                diff = 0
                for j in range(m):
                    if mp[i - o][j] != mp[i + 1 + o][j]:
                        diff += 1
                if diff == 1:
                    used = True
                else: break
               
            o += 1
            if (i - o < 0 or i + 1 + o >= n):
                if used:
                    return mul * (i + 1)
                else: break
    return 0

def print2d(array):
    for i in range(len(array)):
        print(array[i])
            
sm = 0
with open(filename) as fp:
    mp = []
    for line in fp:
        if line == '\n':
            tp = list(map(list, zip(*mp)))
            sm += solve(mp, [sum(x) for x in mp], 100)
            sm += solve(tp, [sum(x) for x in tp], 1)
            
            # print(solve(mp, [sum(x) for x in mp], 100), solve(tp, [sum(x) for x in tp], 1))
            # print2d(mp)
            
            mp = []
            continue
        
        mp.append([])
        for c in line.strip():
            if c == '.':
                mp[-1].append(0)
            else:
                mp[-1].append(1)
            
print(sm)
endtime = time.time()
print(f"Run time: {endtime-starttime}")