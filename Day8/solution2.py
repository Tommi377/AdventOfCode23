import math
import time
from collections import Counter
from functools import cmp_to_key

filename = "input.txt"
start = time.time()

m = dict()
nodes = list()
with open(filename) as fp:
    ins = list(map(lambda x: 1 if x == 'R' else 0, list(fp.readline().strip())))
    
    fp.readline()
    for line in fp:
        split = line.split()
        s = split[0]
        l = split[2][1:4]
        r = split[3][0:3]
        
        m[s] = (l, r)
        
        if s[2] == 'A':
            nodes.append(s)
        
loops = list()

print(len(ins))

for node in nodes:
    current = node
    step = 0
    goals = dict()
    visited = dict()

    while current + str(step % len(ins)) not in visited:
        visited[current + str(step % len(ins))] = step
        if current[2] == 'Z': goals[current + str(step % len(ins))] = step
        current = m[current][ins[step % len(ins)]]
        step += 1
        
    loops.append((node, visited[current + str(step % len(ins))], step, goals))

print(loops)

print(math.lcm(*[list(item[3].values())[0] for item in loops]))

end = time.time()
print(f"Run time: {end-start}")