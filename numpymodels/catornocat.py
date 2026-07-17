import numpy as np
import h5py
# h5 is structured container for arrays

import matplotlib.pyplot as plt 
# lets me display images from dataset

#view inside the h5 

datatest = h5py.File("test_catvsnoncat.h5", "r")

# r means read mode
test_x = datatest["test_set_x"][:] 
# this means load all values from this key
test_x = np.array(test_x)
# and then covert it to an array

test_y = np.array(datatest["test_set_y"][:])



datatrain = h5py.File("train_catvsnoncat.h5", "r")
print (datatrain.keys())

train_x = np.array(datatrain ["train_set_x"][:])
train_y = np.array(datatrain ["train_set_y"][:])

classes = np.array(datatrain ["list_classes"][:])


## all data loading into variables done
# test_set_x, test_set_y, train_set_x, train_set_y

# train_x_flatten = train_x.reshape( train_x.shape[0],train_x.shape[1] * train_x.shape[2] * train_x.shape[3]).T
train_x_flatten = train_x.reshape( train_x.shape[0],-1).T
train_y_flatten = train_y.reshape( train_y.shape[0],-1).T
test_x_flatten = test_x.reshape( test_x.shape[0],-1).T
test_y_flatten = test_y.reshape( test_y.shape[0],-1).T
# -1 means figure it out automatically and shi
train_x_flatten = train_x_flatten/255

test_x_flatten = test_x_flatten/255



def sigmoid (z):
    return (1/(1 +np.exp(-z)))

def initialize_with_zeros (dim):
    w = np.zeros((dim,1))
    b = 0.0

    return w,b 

def propogate(w,b,X,Y):
    m = X.shape[1]  
    A = sigmoid ((w.T @ X )+ b)
    cost = -1/m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))

    dw = 1/m * X @ (A-Y).T
    db = 1/m * np.sum(A - Y)

    grads = {
        "dw" : dw,
        "db" : db
    }  
    return grads,cost

def optimize (w,b,X,Y, num_iterations = 1000, learning_rate = 0.09):
   

    
    costs = []

    for i in range( num_iterations):
        grads, cost = propogate (w,b,X,Y)
        dw = grads["dw"]
        db = grads["db"]
        
        w = w - learning_rate * dw
        b = b - learning_rate * db

        if i % 20 == 0:
            costs.append(cost)
            
    

    params = {
        "w" : w,
        "b" : b
    }

    grads = {"dw": dw,
             "db": db}

    return params, grads, costs


def predict (w, b, X):
    A = sigmoid(np.dot(w.T,X) + b)
     
    # condition and return as integers. wouldve returned as bool without the int type
    return Y_prediction

def model (x_train, y_train, x_test, y_test, num_iterations = 10000, learning_rate = 0.5):

    w,b = initialize_with_zeros(x_train.shape[0])
    params,grads,costs = optimize (w,b,x_train, y_train, num_iterations, learning_rate)
    w = params["w"]
    b = params["b"]

    y_prediction_test = predict(w,b,x_test)
    y_prediction_train = predict(w, b, x_train)

    train_accuracy = 100 - np.mean(np.abs(y_prediction - test_set_Y)) * 100
    print("train accuracy:", train_accuracy)
    # substracts and absolute 
    test_accuracy = 100 - np.mean(np.abs(y_prediction_test - y_test)) * 100
    print("test accuracy:", test_accuracy)

    d = {
        
        "Y_prediction_train": y_prediction_train,
        "Y_prediction_test": y_prediction_test,
        "w": w,
        "b": b,
        "train accuracy": train_accuracy,
        "test accuracy": test_accuracy,
        "learning rate" : learning_rate
    }


    return d
 
# does on forward pass and give a prediction
d = model(train_x_flatten, train_y_flatten, test_x_flatten, test_y_flatten, 2000, 0.005)
best_train_accuracy = d["train accuracy"]
best_test_accuracy = d ["test accuracy"]
learning_rate_train = d["learning rate"]
learning_rate_test = d["learning rate"]

for learning in np.arange(0.007, 0.06, 0.002):
    d = model(train_x_flatten, train_y_flatten, test_x_flatten, test_y_flatten, 2000, learning)
    if d["train accuracy"] > best_train_accuracy:
        best_train_accuracy = d["train accuracy"] 
        learning_rate_train = d["learning rate"]
    if d ["test accuracy"] > best_test_accuracy:
        best_test_accuracy = d ["test accuracy"]
        learning_rate_test = d["learning rate"]
    print(f"The Learning rate is {d['learning rate']} and its accuracy for test set it {d ['test accuracy']} and for training set is {d['train accuracy']}")

print (best_train_accuracy, learning_rate_train)
print(best_test_accuracy, learning_rate_test)
