nums = [5,1,2,6,2,9]

for i in range (len(nums)):
    min_index = i 
    for j in range (i+1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i],nums[min_index] = nums[min_index],nums[i]
print(nums) 