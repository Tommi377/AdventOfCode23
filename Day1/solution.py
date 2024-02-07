filename = "input.txt"

def isletterdigit(line, i):
    n = len(line)
    if line[i] == 'o':
        if i + 2 < n and line[i + 1] == 'n' and line[i + 2] == 'e':
            return '1'
    if line[i] == 't':
        if i + 2 < n and line[i + 1] == 'w' and line[i + 2] == 'o':
            return '2'
        if i + 4 < n and line[i + 1] == 'h' and line[i + 2] == 'r' and line[i + 3] == 'e' and line[i + 4] == 'e':
            return '3'
    if line[i] == 'f':
        if i + 3 < n and line[i + 1] == 'o' and line[i + 2] == 'u' and line[i + 3] == 'r':
            return '4'
        if i + 3 < n and line[i + 1] == 'i' and line[i + 2] == 'v' and line[i + 3] == 'e':
            return '5'
    if line[i] == 's':
        if i + 2 < n and line[i + 1] == 'i' and line[i + 2] == 'x':
            return '6'
        if i + 4 < n and line[i + 1] == 'e' and line[i + 2] == 'v' and line[i + 3] == 'e' and line[i + 4] == 'n':
            return '7'
    if line[i] == 'e':
        if i + 4 < n and line[i + 1] == 'i' and line[i + 2] == 'g' and line[i + 3] == 'h' and line[i + 4] == 't':
            return '8'
    if line[i] == 'n':
        if i + 3 < n and line[i + 1] == 'i' and line[i + 2] == 'n' and line[i + 3] == 'e':
            return '9'
    return None

sum = 0
with open(filename) as fp:
    for line in fp:
        first = None
        last = None
        for i, v in enumerate(line):
            ordv = ord(v) - ord('0')
            if ordv >= 1 and ordv <= 9:
                if first == None:
                    first = v
                last = v
            else:
                chr = isletterdigit(line, i)
                if chr != None:
                    if first == None:
                        first = chr
                    last = chr
        sum += int(first + last)

print(sum)