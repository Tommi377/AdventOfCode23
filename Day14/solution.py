import math
import time

filename = "test2.txt"
starttime = time.time()

doprint = True
def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def print2d(array):
    for i in range(len(array)):
        print(array[i])

n = sum([1 for _ in open(filename)])
fixed = [n for _ in open(filename).readline().strip()]
sm = 0

with open(filename) as fp:
    j = 0
    for line in fp:
        i = 0
        for c in line.strip():    
            if c == '#':
                fixed[i] = n - j - 1
            elif c == 'O':
                sm += fixed[i]
                fixed[i] -= 1
            
            i += 1
        j += 1
            
            
print(sm)
endtime = time.time()
print(f"Run time: {endtime-starttime}")