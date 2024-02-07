filename = "input.txt"

sum = 0
with open(filename) as fp:
    for line in fp:
        tests = line.split(': ')[1].strip().split('; ')
        
        red = 0
        green = 0
        blue = 0
    
        for test in tests:

            cases = test.split(', ')
            for case in cases:
                
                num = int(case.split(' ')[0])
                if case[-1] == 'd':
                    red = max(red, num)
                elif case[-1] == 'n':
                    green = max(green, num)
                elif case[-1] == 'e':
                    blue = max(blue, num)
            
        # print(red * green * blue)
        sum += red * green * blue

print(sum)