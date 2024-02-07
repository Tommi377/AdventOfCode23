filename = "input.txt"

red = 12
green = 13
blue = 14

sum = 0
with open(filename) as fp:
    i = 0
    for line in fp:
        i += 1
        tests = line.split(': ')[1].strip().split('; ')
        impossible = False
        for test in tests:
            if impossible:
                break

            cases = test.split(', ')
            for case in cases:
                if impossible:
                    break
                
                if case[-1] == 'd':
                    impossible = int(case.split(' ')[0]) > red
                if case[-1] == 'n':
                    impossible = int(case.split(' ')[0]) > green
                if case[-1] == 'e':
                    impossible = int(case.split(' ')[0]) > blue
            
        if not impossible:
            sum += i

print(sum)