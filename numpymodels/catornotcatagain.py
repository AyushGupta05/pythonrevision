import numpy as np
import h5py
# for dataset processign

import matplotlib.pyplot as plt
# for graphs and such


## original data processing

data_test = h5py.File("test_catvsnoncat.h5", "r")
data_train = h5py.File("train_catvsnoncat.h5", "r")


# list classes is a 2d so to get its values i need to do this print (data_test["list_classes"][:])

#for key in data_train.keys():
    #print (key)
# to get the values

test_set_x = np.array(data_test["test_set_x"])
test_set_y = np.array(data_test["test_set_y"])

train_set_x = np.array(data_train["train_set_x"])
train_set_y = np.array(data_train["train_set_y"])


train_set_x = train_set_x.reshape(train_set_x.shape[0],-1).T
# for x we want shape where one column represents one example
train_set_y = train_set_y.reshape(1,-1)
# for y we want shape (1,m). each image as one column
test_set_x = test_set_x.reshape(test_set_x.shape[0],-1).T
test_set_y = test_set_y.reshape(1,-1)
# with -1 it means figure it out so that total elements remains same
train_set_x = train_set_x / 255
test_set_x = test_set_x / 255
print(train_set_x.shape)
#print(train_set_y.shape)
#print(test_set_x.shape)
#print(test_set_y.shape)

def initialize():
    w = np.random.randn(test_set_x.shape[0],1)  * 0.01
    b = 0.0
    
    parameters = {"w":w, "b" : b}
    print (w.shape)
    return parameters


def sigmoid(z):
    return 1/(1+np.exp(-z)) 

def forward_propogation(parameters,X,Y):
    w = parameters["w"]
    b = parameters["b"]
    m = X.shape[1]
    A = sigmoid(w.T @ X + b)
    cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
    dw = (X @ (A-Y).T)/m
    db = (np.sum(A-Y)) / m
    stuff = {"A" : A, "cost" : cost, "dw" : dw, "db" : db}
    return stuff

def optimize (stuff, parameters, X, Y, learning_rate = 0.08, num_iterations = 1000):
    costs = []
  
    for i in range (num_iterations):
        w = parameters ["w"]
        b = parameters["b"]
        stuff = forward_propogation(parameters,X,Y)
        dw = stuff ["dw"]
        db = stuff ["db"]
        w -= learning_rate * dw
        b -= learning_rate * db

        parameters["w"] = w
        parameters["b"] = b
        if i % 20 == 0:
            costs.append(stuff["cost"])
            print (f"the cost is {stuff['cost']}")
        


    return w,b,costs


def predict (w,b,X):
    A = sigmoid(w.T @ X + b)
    Y_prediction = (A > 0.5).astype(int)
    return Y_prediction

def model(x_train,y_train, x_test, y_test, learning_rate = 0.08, num_iterations = 10000):
    parameters = initialize()
    stuff = forward_propogation(parameters,x_train,y_train)
    w,b,costs = optimize (stuff, parameters, x_train, y_train, learning_rate, num_iterations)
    y_test_prediction = predict(w,b,x_test)

    test_accuracy = 100 - np.mean(np.abs(y_test_prediction - y_test)) * 100
    print("test accuracy:", test_accuracy)

    params = {"w" : w, "b" : b, "cost" : costs, "y_test_prediction" : y_test_prediction}
    return params

params = model(train_set_x, train_set_y,test_set_x, test_set_y)
plt.plot(params["cost"])
plt.xlabel("Iterations (×20)")
plt.ylabel("Cost")
plt.title("Cost vs Iterations")
plt.show()

    




