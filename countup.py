import time

def count (start=0, end=10):
    for x in range(start,end+1):
        print (x)
        time.sleep(1)

count()