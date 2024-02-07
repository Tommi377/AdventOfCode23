import math
import time

filename = "input.txt"
starttime = time.time()

doprint = True
def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def print2d(array):
    for i in range(len(array)):
        print(array[i])

focal = {}
boxes = [[] for _ in range(256)]

with open(filename) as fp:
    label = ''
    h = 0
    for line in fp:
        for c in line:
            if c == ',' or c == '\n':
                label = ''
                h = 0
            elif c == '=':
                continue
            elif c.isdigit():
                if label not in boxes[h]:
                    boxes[h].append(label)
                focal[label] = int(c)
                label = ''
                h = 0
            elif c == '-':
                if label in boxes[h]:
                    boxes[h].remove(label)
                label = ''
                h = 0
            else:
                label += c
                h = ((h + ord(c)) * 17) % 256
        
        
s = 0        
for i, box in enumerate(boxes):
    for j, item in enumerate(box):
        s += (i + 1) * (j + 1) * focal[item]
        
        
print(s)
endtime = time.time()
print(f"Run time: {endtime-starttime}")