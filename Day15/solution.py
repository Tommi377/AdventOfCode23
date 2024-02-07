import math
import time

filename = "test.txt"
starttime = time.time()

doprint = True
def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def print2d(array):
    for i in range(len(array)):
        print(array[i])

sm = 0

with open(filename) as fp:
    h = 0
    cached = ''
    for line in fp:
        for c in line:
            if c == ',' or c == '\n':
                sm += h
                # print(h)
                h = 0
            else:
                h = ((h + ord(c)) * 17) % 256
        
        
            
            
print(sm)
endtime = time.time()
print(f"Run time: {endtime-starttime}")