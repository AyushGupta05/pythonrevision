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

def sigmoid(z):
    return 1/(1+np.exp(-z))

def relu(z):
    return np.maximum(0.0001*z,z)

def relu_derivative(z):
    return np.where(z > 0, 1.0, 0.0001)

def initialize(layer_sizes):
    params = {} 
    np.random.seed(1)
    n = len(layer_sizes)
    for i in range(1,n):
        params["w" + str(i)] = np.random.randn(layer_sizes[i],layer_sizes[i-1]) *  np.sqrt(2 / layer_sizes[i-1])
        # (104,12228)
        params["b" + str(i)] = np.zeros ((layer_sizes[i],1)) * 0.01
        # (12228,1)

        # w1 = ... 

    return params 

def forward_propogation(X, params,activation):
    n = len(params)//2
    cache = {"A0": X}
    for i in range(1,n):
        z = params["w" + str(i)] @ cache["A" + str(i-1)] + params["b" + str(i)]
        # (104,12228) (12228,...)
        A = activation(z)
        
        cache["z" + str(i)] = z
        cache["A" + str(i)] = A 
    
    z = params["w" + str(n)] @ cache["A" + str(n-1)] + params["b" + str(n)]
     
    A = sigmoid(z)
    cache["z" + str(n)] = z
    cache["AL"] = A 

    return cache

def compute_cost (Y, cache):
    AL = cache["AL"]
    m = Y.shape[1]
    AL = np.clip(cache["AL"], 1e-8, 1 - 1e-8)

    cost = -1/m * np.sum((Y)*np.log(AL) + (1-Y) * np.log(1-AL))

    return cost

def backpropogation (params, cache, Y,activation_derivative):

    grads = {}
    n = len(params) // 2
    AL = cache["AL"]
    grads["dz" + str(n)] = AL - Y 
    m = Y.shape[1]
    for i in range (n,0,-1):
        dz = grads["dz" + str(i)]
        A_prev = cache["A" + str(i-1)]

        grads["dw" + str(i)] = 1/m * (dz @ A_prev.T)
        grads["db" + str(i)] = 1/m * np.sum(dz, axis = 1, keepdims = True)

        if i > 1:
            w = params["w" + str(i)]
            grads["dA" + str (i-1)] = da_prev = w.T @ dz 
            grads ["dz" + str(i-1)] = da_prev * activation_derivative(cache["z" + str(i-1)])

    return grads
        



def update_params(params,grads, learning_rate):
    n = len(params)//2

    for i in range(1,n+1):
        params["w" + str(i)] -= learning_rate * grads["dw" + str(i)]
        params["b" + str(i)] -= learning_rate * grads["db" + str(i)]
    return params

def predict(X, params,activation):
    cache = forward_propogation(X, params,activation)
    AL = cache["AL"]
    Y_prediction = (AL > 0.5).astype(int)
    return Y_prediction

def model(test_x, test_y, train_x, train_y, activation, activation_derivative, layer_sizes, iterations = 1000, learning_rate = 0.06):
    params = initialize(layer_sizes)
    costs = []
    for i in range(iterations+1):
        cache = forward_propogation(train_x, params, activation)
        cost = compute_cost (train_y, cache)
        grads = backpropogation (params, cache, train_y,activation_derivative)
        params = update_params(params,grads, learning_rate)
    
        if i % 20 == 0:
            costs.append(cost)
            print(f"the cost is {cost} at iteration {i}")
    
    Y_prediction = predict(test_x, params, activation)
    
    accuracy = np.mean(Y_prediction == test_y) * 100
    print (f"the test set accuracy is {accuracy}")
    Y_prediction = predict(train_x, params, activation)
    
    accuracy = np.mean(Y_prediction == train_y) * 100
    print (f"the train set accuracy is {accuracy}")

layer_sizes = [12288,200,10,1]
model(train_set_x, train_set_y, test_set_x, test_set_y, relu, relu_derivative,layer_sizes,500, 0.04)


        
    

