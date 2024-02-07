import math
import time

filename = "input.txt"
starttime = time.time()

ans = 0
nx = 140
ny = 140
adj = [[]] * nx * ny
mp = []
queue = []
visited = set()

def addadj(i, n, w, s, e):
    res = []
    if n and i >= nx:
        res.append(i - nx)
    if s and i < nx * ny - nx:
        res.append(i + nx)
    if e and i % nx != 0:
        res.append(i - 1)
    if w and i % nx != nx - 1:
        res.append(i + 1)
        
    return res

start = 0
with open(filename) as fp:
    i = 0
    for line in fp:
        for c in line.strip():
            mp.append(c)
            if c == '-': adj[i] = addadj(i, False, True, False, True)
            elif c == '|': adj[i] = addadj(i, True, False, True, False)
            elif c == 'L': adj[i] = addadj(i, True, True, False, False)
            elif c == 'F': adj[i] = addadj(i, False, True, True, False)
            elif c == '7': adj[i] = addadj(i, False, False, True, True)
            elif c == 'J': adj[i] = addadj(i, True, False, False, True)
            elif c == 'S': start = i
            elif c == '.': queue.append(i)
            # print(i, c, adj[i])
            i += 1
            
assert(nx * ny == i)
            
adj[start] = addadj(start, 
    start - nx >= 0 and start in adj[start - nx],
    start + 1 < ny * nx and start in adj[start + 1],
    start + nx < ny * nx and start in adj[start + nx],
    start - 1 >= 0 and start in adj[start - 1],
)

prev = start
current = adj[start][0]
i = 1
while current != start:
    temp = current
    current = adj[current][0] if adj[current][0] != prev else adj[current][1]
    prev = temp
    i += 1
        
print(math.ceil(i/2)) 

endtime = time.time()
print(f"Run time: {endtime-starttime}")