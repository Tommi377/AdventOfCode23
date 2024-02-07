import math
import time
from colorama import Fore, Back, Style

filename = "input.txt"
starttime = time.time()

ans = 0
nx = 140
ny = 140
adj = [[]] * nx * ny
mp = []
queue = []
dots = []
main = set()
visited = set()
hits = set()

def addadj(i, n, e, s, w):
    res = []
    if n and i >= nx:
        res.append(i - nx)
    if s and i < nx * ny - nx:
        res.append(i + nx)
    if w and i % nx != 0:
        res.append(i - 1)
    if e and i % nx != nx - 1:
        res.append(i + 1)
        
    return res

def isin(c, mp):
    hits = 0
    col = (c // nx) * nx
    sym = None
    for i in range(c % nx + 1, nx):
        if mp[col + i] == '|': hits += 1
        elif mp[col + i] != '.':
            if sym:
                if sym == 'L' and mp[col + i] == '7': hits += 1
                elif sym == 'F' and mp[col + i] == 'J': hits += 1
                elif mp[col + i] == '-': continue
                sym = None
            else:
                sym = mp[col + i]
                if sym != 'L' and sym != 'F': print("ERROR")
        
    return hits % 2 == 1

def bfs(i, vis, h = False):
    vis.add(i)
    queue.append(i)
    s = 0
    while queue:
        node = queue.pop(0)
        s += 1
        if h:
            hits.add(node)

        for n in addadj(node, True, True, True, True):
            if n not in vis and mp[n] == '.':
                vis.add(n)
                queue.append(n)
    return s
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
            elif c == '.': dots.append(i)
            # print(i, c, adj[i])
            i += 1

assert(nx * ny == i)

up = start - nx >= 0 and start in adj[start - nx]
right = start + 1 < ny * nx and start in adj[start + 1]
down = start + nx < ny * nx and start in adj[start + nx]
left = start - 1 >= 0 and start in adj[start - 1]

adj[start] = addadj(start, up, right, down, left)

prev = start
current = adj[start][0]
main.add(current)
while current != start:
    temp = current
    current = adj[current][0] if adj[current][0] != prev else adj[current][1]
    main.add(current)
    prev = temp

if left and right: mp[start] = '-'
elif up and down: mp[start] = '|'
elif up and right: mp[start] = 'L'
elif down and right: mp[start] = 'F'
elif down and left: mp[start] = '7'
elif up and left: mp[start] = 'J'

for i in range(0, len(mp)):
    if i not in main: 
        mp[i] = '.'
        dots.append(i)
    
sum = 0
for i in dots:
    if i in visited: continue
    
    count = bfs(i, visited)
    if isin(i, mp):
        sum += count
        bfs(i, set(), True)

    
for j in range(0, ny):
    for i in range(0, nx):
        c = mp[j * nx + i]
        if (c == '.'):
            if j * nx + i in hits:
                print(Back.GREEN + ' ', end='') 
            else:
                print(Back.RED + ' ', end='')
        else: 
            print(Style.RESET_ALL, end='')
            if c == '-': adj[i] = print("━", end='')
            elif c == '|': adj[i] = print("│", end='')
            elif c == 'L': adj[i] = print("┕", end='')
            elif c == 'F': adj[i] = print("┍", end='')
            elif c == '7': adj[i] = print("┑", end='')
            elif c == 'J': adj[i] = print("┙", end='')
    print(Style.RESET_ALL)

print(sum, len(hits)) 
    
endtime = time.time()
print(f"Run time: {endtime-starttime}")