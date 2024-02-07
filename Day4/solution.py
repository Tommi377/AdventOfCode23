filename = "input.txt"

numbers = []
gears = []
specials = set()

def isnumber(c):
    ordv = ord(v) - ord('0')
    return ordv >= 0 and ordv <= 9

mult = { 1: 1 }
sum = 0
with open(filename) as fp:
    i = 0
    for line in fp:
        i += 1
        card = line.replace('  ', ' ').split(': ')[1].strip().split(' | ')
        win = card[0].split(' ')
        numbers = card[1].split(' ')
    
        plus = mult[i] if i in mult else 1
        j = 0
        for number in numbers:
            if number in win:
                j += 1
                if i + j not in mult: mult[i + j] = 1 + plus
                else: mult[i + j] += plus
                
        print (i, plus)
        sum += plus
                
print(sum)


            
        
        