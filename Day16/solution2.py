import math
import time
from colorama import Fore, Back, Style

filename = "input.txt"
starttime = time.time()

doprint = True
def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def print2d(array):
    for i in range(len(array)):
        print(array[i])

m = []
energized = {}

with open(filename) as fp:
    h = 0
    cached = ''
    for line in fp:
        m.append([])
        for c in line:
            if c == '\n': break
            m[-1].append(c)
        
ny = len(m)
nx = len(m[0])
        
best = 0
queue = [((0, n), (1, 0)) for n in range(ny)] + \
    [((nx - 1, n), (-1, 0)) for n in range(ny)] + \
    [((n, 0), (0, 1)) for n in range(nx)] + \
    [((n, ny - 1), (0, -1)) for n in range(nx)]

for q in queue:
    energized = {}
    beams = [q]
                
    while len(beams):
        beam = beams.pop()
        pos = beam[0]
        vel = beam[1]
        
        while pos[0] >= 0 and pos[0] < nx and pos[1] >= 0 and pos[1] < ny:        
            if m[pos[1]][pos[0]] == '\\':
                vel = (vel[1], vel[0])
            elif m[pos[1]][pos[0]] == '/':
                vel = (-vel[1], -vel[0])
            elif m[pos[1]][pos[0]] == '|' and vel[0] != 0:
                beams.append((pos, (0, -1)))
                vel = (0, 1)
            elif m[pos[1]][pos[0]] == '-' and vel[1] != 0:
                beams.append((pos, (-1, 0)))
                vel = (1, 0)
            
            energized[pos] = 'h' if vel[1] == 0 else 'v'
            pos = (pos[0] + vel[0], pos[1] + vel[1])
            
            
            if pos in energized:
                if energized[pos] == 'b' or (energized[pos] == 'h' and vel[0] != 0) or (energized[pos] == 'v' and vel[1] != 0):
                    if m[pos[1]][pos[0]] != '\\' and m[pos[1]][pos[0]] != '/':
                        break
                else:
                    energized[pos] = 'b'
                    
    best = max(best, len(energized))
                
print(best)
endtime = time.time()
print(f"Run time: {endtime-starttime}")