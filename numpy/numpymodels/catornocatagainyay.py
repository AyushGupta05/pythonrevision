import numpy as np
import h5py 

test_data = h5py.File("test_catvsnoncat.h5", "r")
train_data = h5py.File("train_catvsnoncat.h5", "r")


test_data_x = np.array(test_data["test_set_x"])
test_data_y = np.array(test_data["test_set_y"])


train_data_x = np.array(train_data["train_set_x"])

train_data_y = np.array(train_data["train_set_y"])


train_data_x= train_data_x.reshape(train_data_x.shape[0],-1).T 

train_data_y = train_data_y.reshape(train_data_y.shape[0],-1).T
test_data_y = test_data_y.reshape(test_data_y.shape[0],-1).T
test_data_x= test_data_x.reshape(test_data_x.shape[0],-1).T 

test_data_x = test_data_x/255
train_data_x = train_data_x/255

def sigmoid (e):
    return 1 /(1+np.exp(-e))

def initialize ():
    w = np.random.randn (train_data_x.shape[0],1) * 0.01
    b = 0.0
    return w,b

def forward_propogation(data_x,data_y,w,b):
    m = train_data_x.shape[1]
    A = sigmoid(w.T @ data_x + b)
    cost = -(np.sum(data_y * np.log(A) + (1-data_y) * np.log(1-A)))/m
    dw = 1/m * data_x @ (A-data_y).T
    db = 1/m * np.sum(A - data_y)
    forwardpass = { 
        "A" : A,
        "cost" : cost,
        "dw" : dw,
        "db" : db
    }

    return forwardpass

def optimize (data_x,data_y,w,b,iterations, learning_rate):
    costs = []

    for i in range(iterations):
        forwardpass = forward_propogation(data_x,data_y,w,b)
        dw = forwardpass["dw"]
        db = forwardpass ["db"]
        cost = forwardpass["cost"]
        
        w -= learning_rate *dw
        b -= learning_rate * db

        if i % 20 == 0:
            costs.append(cost)
            print(f"the cost at iteration {i} is {cost}")

    return w,b,costs

def predict (data_x,w,b):
    A = sigmoid(w.T @ data_x + b)
    Y_prediction = (A>0.5).astype(int)
    return Y_prediction


def model (data_x,data_y,test_data_x,test_data_y,iterations = 10000, learning_rate = 0.005):
    w,b = initialize()
    w,b,costs = optimize (data_x,data_y,w,b,iterations, learning_rate)
    Y_prediction = predict(test_data_x,w,b)
    test_accuracy = 100 - np.mean(np.abs(Y_prediction - test_data_y)) * 100
    print(f"the accuracy is {test_accuracy}")
    params = {"w" : w, "b" : b, "costs" : costs}

    return params

model(train_data_x, train_data_y, test_data_x,test_data_y)









