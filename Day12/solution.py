import math
import time

filename = "input.txt"
starttime = time.time()

doprint = False
part2 = True
dp = {}

def printd(*args, end = "\n"):
    if doprint:
        print(*args, end=end)

def rec(work, num, d = 0):
    if len(num) == 0: 
        if all(['#' not in x for x in work]):
            printd("Good")
            return 1
        else:
            printd("Bad")
            return 0
    if len(work) == 0:
        printd("Bad")
        return 0
    if str(work + num) in dp:
        return dp[str(work + num)]
    
    printd("  " * d, work, num)
    
    n = num[0]
    i = 0
    
    perms = 0
    for i in range(len(work)):
        if i > 0 and "#" in work[i - 1]:
            dp[str(work + num)] = perms
            return perms
        if n > len(work[i]): continue

        if len(work[i]) == n:
            perms += rec(work[i + 1:], num[1:], d + 1)
            continue
        elif len(work[i]) - 1 == n:
            if work[i][0] == "#" and work[i][-1] == "#":
                continue
            ans = rec(work[i + 1:], num[1:], d + 1)
            if work[i][0] != "#" and work[i][-1] != "#":
                ans *= 2
            perms += ans
            continue
        else:
            total = 0
            for x in range(n - 1, len(work[i])):
                if (x + 1 == len(work[i]) or work[i][x + 1] != '#') and '#' not in work[i][:x - n + 1]:
                    if len(work[i]) == x + 1 or len(work[i]) == x + 2: 
                        total += rec(work[i + 1:], num[1:], d + 1)
                    else:
                        newwork = [work[i][x + 2:]] + work[i + 1:]
                        total += rec(newwork, num[1:], d + 1)
            perms += total
            continue
            
    dp[str(work + num)] = perms
    return perms
       
       
def brute(s, num):
    for i in range(len(s)):
        if s[i] == '?':
            return brute(s[:i] + '.' + s[i+1:], num) + brute(s[:i] + '#' + s[i+1:], num)
        
    split = list(map(lambda x: len(x), filter(lambda x: x, s.split('.'))))
    if len(split) != len(num): 
        return 0
    
    
    for i in range(len(num)):
        if split[i] != num[i]:
            return 0
    return 1

 
sum = 0
fails = []
with open(filename) as fp:
    i = 0
    for line in fp:
        st, c = line.split()
        
        if part2:
            st = st + 4 * ("?" + st)
        
        s = list(filter(lambda x: x, st.split('.')))
        c = list(map(lambda x: int(x), c.split(',')))

        if part2:
            c = c * 5
        
        if i == 0:
            doprint = False
        r = rec(s, c)
        if i == 0:
            doprint = False
        b = r #brute(st, c)
        # print(s, c, r)
        
        if r != b: fails.append((st, c, r, b))
        
        sum += b
        i += 1
        
if len(fails):
    print("fails:")
    for f in fails:
        print(f)
        
print(sum)
endtime = time.time()
print(f"Run time: {endtime-starttime}")