import math
sum = 0
for i in range (0,100):
    sum += math.pow(2,i) * math.pow(0.5,i+1)

print(sum)

# from scipy import stats
#stats.binom.pmf(10(k),1000(n),0.1(p))

