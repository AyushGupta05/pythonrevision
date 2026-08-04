import numpy as np 
import torch 
import torch.nn as nn
import torch.optim as optim 
from torchvision import transforms

mean = 0.5,
std = 0.5
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((mean,),(std,))
])

# transforms process each data point as loaded
# to tensor transforms it to tensor and mean std scaling

dataset = SomeDataset("./data",train = True, download = True, transform = transform)
# where data lives, how to load a sample, how many total samples, how to apply transforms 

