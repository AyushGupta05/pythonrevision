import torch 
import torch.nn as nn
import torch.optim as optim 

distances = torch.tensor([[1.0],[2.0],[3.0],[4.0]], dtype = torch.float32)
times = torch.tensor([[6.96],[12.11],[16.77],[22.21]], dtype = torch.float32)

# torch type float 32. torch optimized for math 

model = nn.Sequential(nn.Linear(1,1))



# takes 1 input, gives one outpout

loss_function = nn.MSELoss()

#mean squared error lod
optimizer = optim.SGD(model.parameters(),lr=0.01)
# sthocastic gradienet descent, wh ich weights and biases to change, learning rate


# actual training looop
for epoch in range(1000):
    optimizer.zero_grad()
    # resets opitmizer, clear gradients of last one

    outputs = model(distances)
    loss = loss_function(outputs,times)

    loss.backward()
    # how to adjust weights and biases 

    optimizer.step()
    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch + 1}: Loss = {loss}")
    # update the modle

# inference 
print("Loss:", loss.item())
print("Weight:", model[0].weight.item())
print("Bias:", model[0].bias.item())
with torch.no_grad(): # dont calcualte gradients, not training
    test_distance = torch.tensor([[25.0],[50.0]], dtype=torch.float32)
    predicted_time = model(test_distance)
    print(predicted_time)