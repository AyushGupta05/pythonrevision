import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,8]])

print(np.sum(array, axis = 1, keepdims = True))

print(np.mean(array, axis = 1, keepdims = True))

print(np.std(array, axis = 1, keepdims = True))

print(np.var(array, axis = 1, keepdims = True))

print(np.min(array, axis = 1, keepdims = True))

print(np.max(array, axis = 1, keepdims = True))

print(np.argmin(array, axis = 1, keepdims = True))