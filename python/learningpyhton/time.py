import time

timer = int(input ("how long of a timer do you want"))

for x in reversed(range(timer +1)):
    print(x)
    time.sleep(1)

print ("times up")