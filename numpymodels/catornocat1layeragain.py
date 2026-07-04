import h5py as h5
import numpy as np 

test_data = h5.File("test_catvsnoncat.h5","r")
train_data = h5.File("train_catvsnoncat.h5", "r")

test_set_x = np.array(test_data["test_set_x"])
test_set_y = np.array(test_data["test_set_y"])
train_set_x = np.array(train_data["train_set_x"])
train_set_y = np.array(train_data["train_set_y"])

test_set_x = test_set_x.reshape(test_set_x.shape[0],-1).T
train_set_x = train_set_x.reshape(train_set_x.shape[0],-1).T

test_set_y = test_set_y.reshape(1,-1)
train_set_y = train_set_y.reshape(1,-1)

test_set_x = test_set_x / 255
train_set_x = train_set_x / 255

def sigmoid (z):
    return 1/(1+np.exp(-z))

def tanh (z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

def initialize_parameters(X,Y):
    n_x = X.shape[0]
    n_h = 10
    n_y = Y.shape[0]

    np.random.seed(5)
    w1 = np.random.randn(n_h,n_x) *0.01
    b1 = np.zeros((n_h,1))
    w2 = np.random.randn(n_y,n_h)  * 0.01
    b2 = np.zeros((n_y,1))

    params = {"w1" : w1, "b1" : b1, "w2" : w2, "b2" : b2}

    return params

def forward_propogation(X,params):
    w1 = params["w1"]
    w2 = params["w2"]
    b1 = params["b1"]
    b2 = params["b2"]

    z1 = w1 @ X + b1
    a1 = tanh(z1)
    z2 = w2 @ a1 + b2 
    a2 = sigmoid(z2)

    cache = {"a1" : a1, "a2" : a2}

    return cache

def compute_cost(X,cache,Y):
    m = X.shape[1]
    a2 = cache["a2"]
    cost = -1/m  * np.sum([Y * np.log(a2) + (1-Y)*np.log(1-a2)])

    return cost 

def backward_propogation(X, Y, params,cache):
    a2 = cache["a2"]
    a1 = cache["a1"]
    w2 = params["w2"]
    m = X.shape[1]
    dz2 = a2 - Y 
    dw2 = 1/m * (dz2 @ a1.T)
    db2 = 1/m * np.sum(dz2, axis=1, keepdims=True)
    dz1 = (w2.T  @ dz2 ) * (1-(a1**2))
    dw1 = 1/m * (dz1 @ X.T)
    db1 = 1/m * np.sum(dz1, axis=1, keepdims=True)

    derivatives = {"dw2" : dw2, "dw1" : dw1, "db1" : db1, "db2": db2}

    return derivatives

def optimize(X,Y, iterations=  1000, learning_rate = 0.07):
    costs = []
    params = initialize_parameters(X,Y)

    for i in range(iterations):
        cache = forward_propogation(X,params)
        derivatives = backward_propogation(X, Y, params,cache)
        params["w1"] -= learning_rate * derivatives["dw1"]
        params["w2"] -= learning_rate * derivatives["dw2"]
        params["b1"] -= learning_rate * derivatives["db1"]
        params["b2"] -= learning_rate * derivatives["db2"]
        if i % 20 == 0:
            cost = compute_cost(X,cache,Y)
            print(f"the cost is {cost} at iteration {i}")
            costs.append(cost)
    
    return params, costs

def predict(X,params):
    cache = forward_propogation(X,params)
    a2 = cache["a2"]
    Y_prediction = (a2 > 0.5).astype(int)

    return Y_prediction

def model (train_X,train_Y, test_X, test_Y,iterations,learning_rate):
    params,cost = optimize (train_X,train_Y, iterations,learning_rate)
    Y_prediction = predict(test_X,params)
    test_accuracy = 100 - np.mean(np.abs(Y_prediction - test_Y)) * 100
    print(f"the accuracy is {test_accuracy}")
    Y_prediction = predict(train_X,params)
    train_accuracy = 100 - np.mean(np.abs(Y_prediction - train_Y)) * 100
    print(f"the accuracy is {train_accuracy}")

model(train_set_x, train_set_y, test_set_x, test_set_y,1000,0.02)
    

            
