filename = "input.txt"

numbers = []
gears = []
specials = set()

def isnumber(c):
    ordv = ord(v) - ord('0')
    return ordv >= 0 and ordv <= 9

nums = []
with open(filename) as fp:
    n = 0
    j = 0
    for line in fp:
        if n == 0: n = len(line)
        
        for i, v in enumerate(line):
            if isnumber(v):
                nums.append(v)
            else:
                if (len(nums) > 0):
                    numbers.append((int(''.join(nums)), (i - len(nums), j), len(nums)))
                
                nums = []
                if v == '*':
                    gears.append((i, j))
                
        j += 1
        
if (len(nums) > 0):
    numbers.append((int(''.join(nums)), (n - 1 - len(nums), j - 1), len(nums)))

print(gears)

sum = 0    
for gear in gears:
    adj = []
    
    for number in numbers:
        num = number[0]
        coord = number[1]
        length = number[2]
        
        if gear[1] == coord[1]:
            if gear[0] == coord[0] - 1 or gear[0] == coord[0] + length:
                adj.append(num)
        elif gear[1] == coord[1] - 1 or gear[1] == coord[1] + 1:
            if gear[0] >= coord[0] - 1 and gear[0] <= coord[0] + length:
                adj.append(num)
                
                
    print(adj)
    if len(adj) == 2:
        sum += adj[0] * adj[1]
    
        
# print(n)
print(sum)
            
        
        