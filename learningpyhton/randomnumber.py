import random

total = 0

for x in range(1,1001):
    number = random.randint(1 , 6)
    total += number


print (total/1000)




def average (x):
    total = 0
    for count in x:
        total += count
    
    return total/len(x)

def happy_birthday():
    print("happy_birthday")
    print("happy_birthday")
    print("happy_birthday")
    print("happy_birthday")

happy_birthday()

numberlist = [3,4,5,6]
print(average(numberlist))