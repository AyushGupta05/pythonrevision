import numpy as np

array = np.array([[[1,2,3,4],[3,76,4,2]],[[1,2,3,4],[3,76,4,2]]])
array = array * 2

print(array.shape)
mdarray = np.array('A')


# 0d array only has one value
print(mdarray.ndim)
