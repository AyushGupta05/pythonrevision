nums = [3,2,4]
target = 6
for i,x in enumerate(nums):
    for j,y in enumerate(nums):
        if i != j and x + y == target:
            print(i,j)
            exit()

