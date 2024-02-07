import math
import time

filename = "input.txt"
start = time.time()

def getdist(hold, time):
    return hold * time

def getroot(a, b, c):
    d = math.sqrt(b * b - 4 * a * c)
    r = (-b + d) / (2 * a)
    return int(r)

result = 1
with open(filename) as fp:
    # seed
    times = list(map(lambda x: int(x), fp.readline().split()[1:]))
    dists = list(map(lambda x: int(x), fp.readline().split()[1:]))
    
    for i in range(len(times)):
        m = times[i] // 2
        l = getroot(-1, times[i], -dists[i])
        
        ans = (m - l) * 2
        if times[i] % 2 == 0: ans -= 1
        
        result *= ans
        
print(result)    

end = time.time()
print(f"Run time: {end-start}")