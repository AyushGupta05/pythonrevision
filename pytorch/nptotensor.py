import numpy as np 
import torch 
import torch.nn as nn
import torch.optim as optim 

numpy_array = np.array([1,2,3])
tensor_np = torch.from_numpy(numpy_array)

zeros = torch.zeros(3,3)
ones = torch.ones(2,4)
random = torch.rand(5,5)

# can use indexing same way as in list. use .item to convert into float, only works with tensors with one value

# math works same way as np, same as broadcasting 