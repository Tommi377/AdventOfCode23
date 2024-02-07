import math
import time

filename = "input.txt"
starttime = time.time()

galaxies = []
xgals = set()
ygals = set()
nx = 0
ny = 0

with open(filename) as fp:
    j = 0
    for line in fp:
        i = 0
        for c in line.strip():
            if c == '#': 
                galaxies.append([i, j, False])
                xgals.add(i)
                ygals.add(j)
            i += 1
        nx = i
        j += 1
    ny = j
        
print(sorted(xgals))
print([(x, y) for x, y, _ in galaxies])

mul = 1000000-1

offset = 0
for x in range(nx):
    if x not in xgals:
        offset += mul
    else:
        for i in range(len(galaxies)):
            if galaxies[i][0] == x and not galaxies[i][2]:
                galaxies[i][0] += offset
                galaxies[i][2] = True
offset = 0
for y in range(ny):
    if y not in ygals:
        offset += mul
    else:
        for i in range(len(galaxies)):
            if galaxies[i][1] == y and galaxies[i][2]:
                galaxies[i][1] += offset
                galaxies[i][2] = False

#print([(x, y) for x, y, _ in galaxies])

sum = 0
pairs = []
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
                
        sum += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])

print(sum)

endtime = time.time()
print(f"Run time: {endtime-starttime}")