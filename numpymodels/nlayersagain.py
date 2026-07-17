import h5py as h5
import numpy as np 

test_data = h5.File("test_catvsnoncat.h5","r")
train_data = h5.File("train_catvsnoncat.h5","r")

test_set_x = np.array(test_data["test_set_x"])
test_set_y = np.array(test_data["test_set_y"])
train_set_x = np.array(train_data["train_set_x"])
train_set_y = np.array(train_data["train_set_y"])

test_set_x = test_set_x.reshape(test_set_x.shape[0],-1).T 
train_set_x = train_set_x.reshape(train_set_x.shape[0],-1).T

test_set_y = test_set_y.reshape(1,-1)
train_set_y = train_set_y.reshape(1,-1)
test_set_x = test_set_x/255
train_set_x = train_set_x/255


def relu (z):
    return np.maximum(0,z)
def sigmoid(z):
    return 1/ (1+np.exp(-z))
def relu_derivative(z):
    return (z > 0).astype(float)
def initialize_parameters (n_layers):
    parameters = {}
    
    for i in range(1,len(n_layers)):
        parameters["W" + str(i)] = np.random.randn(n_layers[i],n_layers[i-1]) * 0.01
        parameters["b" + str(i)] = np.zeros((n_layers[i],1))
        
    return parameters 

def forward_propogation(X, parameters):
    n = len(parameters)//2
    cache = {"A0":X} 
    for i in range(1,n):
        z = parameters["W" + str(i)] @ cache["A"+str(i-1)] + parameters["b" + str(i)]
        a = relu(z)

        cache["Z" + str(i)] = z 
        cache["A" + str(i)] = a
    
    z = parameters["W" + str(n)] @ cache["A"+str(n-1)] + parameters["b" + str(n)]
    a = sigmoid(z)
    cache["Z" + str(n)] = z 
    cache["AL"] = a

    return cache 

def computecost(cache,Y):
    AL = cache["AL"]
    m = Y.shape[1]
    AL = np.clip(AL, 1e-8, 1 - 1e-8)

    cost = -1/m *  np.sum(((Y * np.log(AL)) + ((1-Y) * np.log(1-AL))))

    return cost

def backpropogation(Y,parameters,cache):
    n = len(parameters)//2
    gradients=  {}
    m = Y.shape[1]
    AL = cache["AL"]
    gradients ["dZ" + str(n)] = AL - Y
    for i in range (n,0,-1):
        dZ= gradients["dZ" + str(i)]
        A_prev = cache ["A" + str(i-1)]
        W = parameters["W" + str(i)]

        gradients["dW" + str(i)] = 1/m * (dZ @ A_prev.T)
        gradients["db" + str(i)] = 1/m * np.sum(dZ, axis = 1, keepdims = True)

        if i > 1:
            gradients["dA"+str(i-1)] = W.T @ dZ
            Z_prev = cache["Z" + str(i-1)]
            gradients["dZ"+str(i - 1)] = gradients["dA"+str(i-1)] * relu_derivative(Z_prev)
    return gradients




def update_params(parameters, gradients, learning_rate):
    L = len(parameters)//2 
    for i in range(1,L+1):
        parameters["W" + str(i)] -= learning_rate * gradients["dW" + str(i)]
        parameters["b" + str(i)] -= learning_rate * gradients["db" + str(i)]

    return parameters

def predict(X,parameters):
    cache = forward_propogation(X, parameters)
    AL = cache["AL"]
    Y_prediction = (AL >= 0.5).astype(int)
    return Y_prediction


def model (train_X, train_Y, test_X, test_Y, layer_dims,learning_rate = 0.0075, num_iterations = 3000):
    costs = []

    parameters = initialize_parameters(layer_dims)

    for i in range (0,num_iterations):
       cache =  forward_propogation(train_X,parameters)
       cost = computecost(cache, train_Y)
       gradients = backpropogation(train_Y, parameters, cache)
       parameters = update_params(parameters, gradients, learning_rate)

       if i%20 == 0:
        print(f"the cost is {cost} at iterations {i}")
        costs.append(cost)
    
    Y_prediction = predict(test_X,parameters )
    test_accuracy = 100 - np.mean(np.abs(Y_prediction - test_Y)) * 100
    print(f"the test accuracy is {test_accuracy}")

    Y_prediction = predict(train_X,parameters)
    train_accuracy = 100 - np.mean(np.abs(Y_prediction - train_Y)) * 100
    print(f"the train accuracy is {train_accuracy}")
    return parameters,costs
        
layer_dims = [12288,20,7,5,1]

parameters, costs = model(train_set_x,train_set_y,test_set_x,test_set_y,layer_dims, 0.00195, 4000)

test_data.close()
train_data.close()