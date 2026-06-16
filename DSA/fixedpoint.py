def fixed_point (nums):
    
    beg = 0
    end = len(nums) - 1

    while end >= beg:
        mid = ((beg + end) // 2)

        if nums[mid] == mid:
            return mid
        elif nums[mid] < mid:
            beg = mid + 1
        else:
            end = mid - 1
        

    return -1



tests = [
    {
        "input" : [-10, -5, 0, 3, 7],
        "output" : 3
    },
       {
        "input" : [-10, -5, 2, 4, 9],
        "output" : 2
    },
     {
        "input" : [-10, -5, 0, 4, 9],
        "output" : -1
    }
]


for test in tests:
    print(fixed_point(test["input"]) == test["output"])

