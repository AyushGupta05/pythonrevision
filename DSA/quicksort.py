
if len(nums) < =1:
    return nums
 
pivot = nums[0]
smaller = []
equal = []
larger = []

for num in nums:
    if num < pivot:
        smaller.append(num)
    elif num > pivot:
        larger.append(num)
    else:
        equal.append(num)

return quick_sort(smaller) + equal + quick_sort(larger)