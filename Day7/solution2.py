import math
import time
from collections import Counter
from functools import cmp_to_key

filename = "input.txt"
start = time.time()

strength = {
    'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
    '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12
}

def scorehand(hand):
    counts = Counter(hand)
    bestscore = 0
    
    jcount = counts.get('J', 0)
    if 'J' in counts.keys():
        del counts['J']
    
    for k in counts.keys():
        score = 0
        for key, value in counts.items(): # J1133
            val = value
            if k == key: val += jcount
            
            if val == 5:
                score += 100
            
            if val == 4:
                score += 80
                
            if val == 3:
                score += 50

            if val == 2:
                score += 10
        bestscore = max(score, bestscore)
        
    if len(counts) == 0: return 100
            
    return bestscore

def comparehand(hand1, hand2):
    h1sc = scorehand(hand1)
    h2sc = scorehand(hand2)
    
    if h1sc == h2sc:
        for i in range(5):
            if hand1[i] != hand2[i]:
                return 1 if strength[hand1[i]] > strength[hand2[i]] else -1        
    else:
        return 1 if h1sc > h2sc else -1        
    
        
hands = []
with open(filename) as fp:
    for line in fp:
        hand, bid = line.split()
        bid = int(bid)
        hands.append((hand, bid))
        
ranks = sorted(hands, key=cmp_to_key(lambda x, y: comparehand(x[0], y[0])))

sum = 0
for i in range(len(ranks)):
    sum += ranks[i][1] * (i + 1)

print(sum)

end = time.time()
print(f"Run time: {end-start}")