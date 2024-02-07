import math
import time
from collections import Counter
from functools import cmp_to_key

filename = "input.txt"
start = time.time()

m = dict()
with open(filename) as fp:
    ins = list(map(lambda x: 1 if x == 'R' else 0, list(fp.readline().strip())))
    
    fp.readline()
    for line in fp:
        split = line.split()
        s = split[0]
        l = split[2][1:4]
        r = split[3][0:3]
        
        m[s] = (l, r)
        
i = 0
current = 'AAA'
while current != 'ZZZ':
    current = m[current][ins[i % len(ins)]]
    i += 1

print(i)

end = time.time()
print(f"Run time: {end-start}")