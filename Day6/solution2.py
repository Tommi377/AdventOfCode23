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
    t = int(fp.readline().split(":")[1].replace(" ", ""))
    d = int(fp.readline().split(":")[1].replace(" ", ""))
    
    m = t // 2
    l = getroot(-1, t, -d)
    
    ans = (m - l) * 2
    if t % 2 == 0: ans -= 1
    
    result *= ans
        
print(result)    

end = time.time()
print(f"Run time: {end-start}")