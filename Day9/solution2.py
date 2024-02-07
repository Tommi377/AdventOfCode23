import math
import time

filename = "input.txt"
start = time.time()

ans = 0

with open(filename) as fp:
    for line in fp:
        nums = []
        nums.append(list(map(lambda x: int(x), line.split())))
        n = len(nums[0])
        for i in range(0, n - 1):
            allzeros = True
            nums.append([])
            for j in range(0, n - i - 1):
                diff = nums[i][j + 1] - nums[i][j]
                nums[i + 1].append(diff)
                
                if diff != 0: allzeros = False
            if allzeros:
                exval = 0
                for k in range(i, -1, -1):
                    exval = nums[k][0] - exval
                ans += exval
                break
            
            
print(ans)            

end = time.time()
print(f"Run time: {end-start}")