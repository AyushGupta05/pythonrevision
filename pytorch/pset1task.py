import random


trials = 10000000
totalwins = 0
for i in range(1,trials+1):
    S = 0
    x = None
    Y = None
    while S <= 200:
        number = random.randint(1,100)
        S += number 
        if S > 100 and x is None:
            x = number 
        if S > 200:
            y = number 
    if y > x:
        totalwins += 1

print(totalwins/trials)


