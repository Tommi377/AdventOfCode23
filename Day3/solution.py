filename = "input.txt"

numbers = []
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
                if v != '.' and v != '\n':
                    specials.add((i, j))
                    specials.add((i - 1, j))
                    specials.add((i, j - 1))
                    specials.add((i + 1, j))
                    specials.add((i, j + 1))
                    specials.add((i + 1, j + 1))
                    specials.add((i - 1, j - 1))
                    specials.add((i - 1, j + 1))
                    specials.add((i + 1, j - 1))
                
        j += 1
        
if (len(nums) > 0):
    numbers.append((int(''.join(nums)), (n - 1 - len(nums), j - 1), len(nums)))

sum = 0        
           
for number in numbers:
    num = number[0]
    coord = number[1]
    length = number[2]
    
    included = False
    
    for l in range(length):
        if (coord[0] + l, coord[1]) in specials:
            included = True
            break
        
    # print(num, included)
        
    if included:
        sum += num
        
# print(n)
print(sum)
            
        
        