import h5py as h5
import numpy as np 
import random

test_data = h5.File("test_catvsnoncat.h5","r") 
train_data = h5.File ("train_catvsnoncat.h5","r")



test_set_x = np.array(test_data["test_set_x"])
test_set_y = np.array(test_data["test_set_y"])
train_set_x = np.array(train_data["train_set_x"])
train_set_y = np.array(train_data ["train_set_y"])

train_set_x = train_set_x.reshape(train_set_x.shape[0],-1).T
test_set_x = test_set_x.reshape(test_set_x.shape[0],-1).T
train_set_y = train_set_y.reshape(1,-1)
test_set_y = test_set_y.reshape(1,-1)

train_set_x = train_set_x/255
test_set_x = test_set_x/255


def sigmoid (z):
    return 1/(1+np.exp(-z))

def tanh (z):
    return np.tanh(z)

def relu (z):
    return np.maximum(0,z)

def initialize_parameters(layer_dims):
    np.random.seed(1)
    parameters = {}
    L = len(layer_dims) - 1
    for i in range(1,L + 1):
        parameters["W" + str(i)] = np.random.randn (layer_dims[i], layer_dims[i-1]) *  np.sqrt(2 / layer_dims[i-1])
        parameters["b" + str(i)] = np.zeros((layer_dims[i],1))
    

    return  parameters 

def forward_propogation(X,parameters,activation):
    L = len(parameters)//2
    cache = {"A0" : X}
    for i in range(1,L):
        z = parameters["W"+str(i)] @ cache["A"+str(i-1)] + parameters["b"+str(i)]
        a = activation(z)
        cache["Z"+str(i)] = z 
        cache["A" + str(i)] = a

    
    z = parameters["W"+str(L)] @ cache["A"+str(L-1)] + parameters["b"+str(L)]
    a = sigmoid(z)
    cache["ZL"] = z 
    cache["AL"] = a

    return cache
        

def compute_cost(cache, Y):
    m = Y.shape[1]
    
    AL = np.clip(cache["AL"], 1e-15, 1 - 1e-15)
    cost = -1/m* (np.sum ((Y * np.log(AL)) + ((1-Y) * np.log( 1- AL))))

    return cost

def relu_derivative(Z):
    return (Z > 0).astype(float)

def backprop(Y, parameters, cache, activation_derivative):
    L = len(parameters)//2 
    m = Y.shape[1]

    gradients = {}

    AL = cache["AL"]
    gradients["dZ" + str(L)] = AL - Y

    for l in range (L,0,-1):
        dZ = gradients ["dZ" + str(l)]
        A_prev = cache["A" + str(l-1)]
        W = parameters["W" + str(l)]

        gradients["dW" + str(l)] = (1 / m) * dZ @ A_prev.T
        gradients["db" + str(l)] = (1 / m) * np.sum(dZ,axis=1,keepdims=True)

        if l > 1:
            dA_prev = W.T @ dZ 
            Z_prev = cache["Z"+str(l-1)]

            gradients["dA" + str(l - 1)] = dA_prev
            gradients["dZ" + str(l - 1)] = (dA_prev * activation_derivative(Z_prev))

    return gradients


def update_params(parameters, gradients, learning_rate):
    L = len(parameters)//2 
    for i in range(1,L+1):
        parameters["W" + str(i)] -= learning_rate * gradients["dW" + str(i)]
        parameters["b" + str(i)] -= learning_rate * gradients["db" + str(i)]

    return parameters

def predict(X,parameters,activation):
    cache = forward_propogation(X, parameters, activation)
    AL = cache["AL"]
    Y_prediction = (AL > 0.5).astype(int)
    return Y_prediction


def model (train_X, train_Y, test_X, test_Y, layer_dims,activation, activation_derivative,learning_rate = 0.0075, num_iterations = 3000):
    costs = []

    parameters = initialize_parameters(layer_dims)

    for i in range (0,num_iterations):
       cache =  forward_propogation(train_X,parameters,activation)
       cost = compute_cost(cache, train_Y)
       gradients = backprop(train_Y, parameters, cache, activation_derivative)
       parameters = update_params(parameters, gradients, learning_rate)

       if i%20 == 0:
        print(f"the cost is {cost} at iterations {i}")
        costs.append(cost)
    
    Y_prediction = predict(test_X,parameters, activation )
    test_accuracy = 100 - np.mean(np.abs(Y_prediction - test_Y)) * 100
    print(f"the test accuracy is {test_accuracy}")

    Y_prediction = predict(train_X,parameters, activation )
    train_accuracy = 100 - np.mean(np.abs(Y_prediction - train_Y)) * 100
    print(f"the train accuracy is {train_accuracy}")
    return parameters,costs
        
layer_dims = [12288,20,7,5,1]

parameters, costs = model(train_set_x,train_set_y,test_set_x,test_set_y,layer_dims, relu, relu_derivative, 0.00195, 4000)



