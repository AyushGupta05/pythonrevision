import numpy as np

ages = np.array([[21,17,18,19,20], [38,29,41,942,11]])
print(ages)
valid_age = np.where(ages > 18, ages, 0 )
## new array = np.where(condition, array, fill value)

print(valid_age)