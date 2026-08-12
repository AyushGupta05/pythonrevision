import numpy as np 
import torch 
import torch.nn as nn
import torch.optim as optim 
from torchvision import transforms

class ExampleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = nn.Linear(1,20)
        self.relu = nn.ReLU()
        self.layer_2 = nn.linear(20,1)
    def forward(self,x):
        x = self.layer_1(x)
        x = self.relu(x)
        x = self.layer_2 (x)
        return x 

# same as  this but mor econtrol 
#
#model = nn.Sequential(

        #nn.Linear(1,3),
      #nn.ReLU(),
      #nn.Linear(3,1))

model = ExampleModel()
output = model(data)
# pytorch run its internal checks and update stuff

# evaluation 

model.eval() # sets model into eval mode 

with torch.no_grad (): #disable gradient tracking 
    correct = 0 
    total = 0 
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted  = torch.max(outputs,1) # class with highiest sccore 
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    accuracy = 100 * correct/total 

    print (f"accuracy : {accuracy }")

model.train()  ## backl to train mode 