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
    return 1 /(1+np.exp(-z))

def tanh (z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

def initialize_layers (X, Y):
    n_x = X.shape[0]
    n_h = 100
    n_y = Y.shape[0]
    return (n_x, n_h, n_y)

def initialize_parameters (n_x,n_h,n_y):
    np.random.seed(3)
    w1 = np.random.randn(n_h,n_x)  * 0.01
    w2 = np.random.randn (n_y,n_h) * 0.01
    b1 = np.zeros((n_h, 1))
    b2 = np.zeros((n_y, 1))

    params = {"w1" : w1, "w2" : w2, "b1" : b1, "b2" : b2}
    return params

def forward_propogation(X,params):
    w1 = params["w1"]
    w2 = params["w2"]
    b1 = params ["b1"]
    b2 = params ["b2"]
    
    z1 = (w1 @ X + b1)
    a1 = tanh(z1)
    z2 = (w2 @ a1 + b2)
    a2 = sigmoid (z2)

    cache = {"z1" : z1, "a1" : a1, "z2" : z2, "a2" :a2}

    return a2,cache

def compute_cost (cache, Y):
    a2 = cache["a2"]
    m = Y.shape[1]
    cost = -(np.sum(Y * np.log(a2) + (1-Y) * np.log(1-a2)))/m

    return cost

def backward_propogation(cache, X, Y, params):
    m = X.shape[1]
  
    w2 = params["w2"]
   

    a1 = cache ["a1"]
    a2 = cache ["a2"]

    dz2 = a2 - Y 
    dw2 = 1/m * (dz2 @ a1.T)
    db2 = 1/m * (np.sum(dz2, axis = 1, keepdims = True))
    da1 = w2.T @ dz2
    dz1 = da1 * (1-((a1)**2))
    dw1 = 1/m * (dz1 @ X.T)
    db1 = 1/m * (np.sum(dz1, axis = 1, keepdims = True))
    grads = {
        "dw1": dw1,
        "db1": db1,
        "dw2": dw2,
        "db2": db2
    }

    return grads

def optimize (params, X, Y, learning_rate = 1.1, iterations = 1000):
    costs = []

    for i in range(iterations):
        a2, cache = forward_propogation(X, params)
        grads = backward_propogation(cache,X,Y,params)
        params["w1"] -= learning_rate * grads["dw1"]
        params["w2"] -= learning_rate * grads["dw2"]
        params["b1"] -= learning_rate * grads["db1"]
        params["b2"] -= learning_rate * grads["db2"]
        if i % 20 == 0:
            
            cost = compute_cost(cache, Y)
            print (f"the cost is {cost} at iteration {i}")
            costs.append(cost)
    
    
    return params, costs

def predict (params,X):
    A2, cache = forward_propogation(X, params)
    prediction = (A2>0.5).astype(int)

    return prediction



def model(train_data_x,train_data_y,test_data_x, test_data_y,learning_rate,iterations):
    n_x,n_h,n_y = initialize_layers (train_data_x, train_data_y)
    params = initialize_parameters (n_x,n_h,n_y)
    params, costs = optimize (params, train_data_x, train_data_y, learning_rate, iterations)
    prediction = predict(params,test_data_x)
    test_accuracy = 100 - np.mean(np.abs(prediction - test_data_y)) * 100
    print(f"the accuracy is {test_accuracy}")

model(train_set_x,train_set_y,test_set_x,test_set_y,0.05, 1000)