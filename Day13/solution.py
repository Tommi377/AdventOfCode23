import math
import time

filename = "input.txt"
starttime = time.time()

doprint = True
def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def solve(mp, mul):
    n = len(mp)
    for i in range(0, n - 1):
        o = 0
        while mp[i - o] == mp[i + 1 + o]:
            o += 1
            if i - o < 0 or i + 1 + o >= n:
                return mul * (i + 1)
    return 0

def print2d(array):
    for i in range(len(array)):
        print(array[i])
            
sum = 0
with open(filename) as fp:
    mp = []
    for line in fp:
        if line == '\n':
            tp = list(map(list, zip(*mp)))
            sum += solve(mp, 100)
            sum += solve(tp, 1)
            
            mp = []
            continue
        
        mp.append([])
        for c in line.strip():
            mp[-1].append(c)
            
print(sum)
endtime = time.time()
print(f"Run time: {endtime-starttime}")