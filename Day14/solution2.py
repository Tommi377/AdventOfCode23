import math
import time
import functools

filename = "input.txt"
starttime = time.time()

doprint = True
def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def print2d(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end="")
        print()
        
def checkload(arr):
    load = 0
    
    for j in range(len(arr)):
        for i in range(len(arr[0])):
            c = arr[j][i]	
            if c == 'O':
                load += n - j
                
    return load
        
@functools.cache
def cycle(arr):
    for _ in range(4):
        newarr = [['.'] * n for _ in range(m)]
        fixed = [n] * m
        
        for j in range(len(arr)):
            for i in range(len(arr[0])):
                c = arr[j][i]
                
                
                if c == '#':
                    fixed[i] = n - j - 1
                    newarr[i][n - j - 1] = '#'
                elif c == 'O':
                    newarr[i][fixed[i] - 1] = 'O'
                    fixed[i] -= 1
                    
        arr = newarr
    return tuple([tuple(a) for a in newarr])

n = sum([1 for _ in open(filename)])
m = sum([1 for _ in open(filename).readline().strip()])
sm = 0
arr = []

with open(filename) as fp:
    j = 0
    for line in fp:
        i = 0
        arr.append([])
        for c in line.strip():
            arr[j].append(c)            
            i += 1
        j += 1
            

begin = tuple([tuple(a) for a in arr])
cs = None
cyclefirst = []
cyclestart = 0
cyclelen = 0

dict = {}
arr = tuple([tuple(a) for a in arr])
i = 0
target = 1000000000
while i < target:
    i += 1
    arr = cycle(arr)
    

    if arr not in dict:
        dict[arr] = i
    elif cyclelen == 0:
        cyclelen = i - dict[arr]
        fit = (target - i) // cyclelen
        i += fit * cyclelen

print(checkload(arr))
print2d(arr)
            
endtime = time.time()
print(f"Run time: {endtime-starttime}")