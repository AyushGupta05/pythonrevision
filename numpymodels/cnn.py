import h5py as h5
import numpy as np 

test_data = h5.File("test_catvsnoncat.h5","r")
train_data = h5.File("train_catvsnoncat.h5","r")

test_set_x = np.array(test_data["test_set_x"])
test_set_y = np.array(test_data["test_set_y"])
train_set_x = np.array(train_data["train_set_x"])
train_set_y = np.array(train_data["train_set_y"])

test_set_x = test_set_x/255
train_set_x = train_set_x/255
train_set_y = train_set_y.reshape(1, -1)
test_set_y = test_set_y.reshape(1, -1)

def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1/(1+np.exp(-z)) 
def pad (X, pad):
    X_pad = np.pad(X,((0,0), (pad,pad), (pad,pad), (0,0)), mode = "constant", constant_values=(0,0))
    return X_pad 

def initialize_params(filter_size, input_channels, num_filters):
    W = np.random.randn(filter_size,filter_size,input_channels,num_filters)* np.sqrt(2 / (filter_size * filter_size * input_channels))
    b = np.zeros((1,1,1,num_filters))

    return W,b 

def conv_forward(X,W,b,stride = 1, padding = 1):
    m, H_prev, W_prev, C_prev = X.shape
    f, _, _, C_out = W.shape
    H_out = ((H_prev + 2 * padding - f) // stride) + 1
    W_out = ((W_prev + 2 * padding - f) // stride) + 1

    X_pad = pad(X,padding)
    Z = np.zeros((m,H_out, W_out, C_out))

    # z is output before applying activation
    for i in range(m):
        for h in range (H_out):
            for w in range (W_out):
                vert_start = h  * stride 
                vert_end = vert_start + f

                horiz_start = w * stride
                horiz_end = horiz_start+f 

                X_slice = X_pad[i,vert_start:vert_end,horiz_start:horiz_end,:]

                for c in range (C_out):
                    Z[i,h,w,c] = (np.sum(X_slice * W [:,:,:,c])) + b [0,0,0,c]

    A = np.maximum(0.001*Z,Z)
    cache = (X,W,b,Z,stride,padding)
    return A, cache

def pool (A, pool_size = 2, stride = 2, mode = "max"):
    m, H_prev, W_prev, C_prev = A.shape
    H_out = ((H_prev - pool_size) // stride) + 1
    W_out = ((W_prev - pool_size) // stride) + 1
    P = np.zeros((m, H_out, W_out, C_prev))

    for i in range(m):
            for h in range (H_out):
                for w in range (W_out):
                    vert_start = h  * stride 
                    vert_end = vert_start + pool_size
    
                    horiz_start = w * stride
                    horiz_end = horiz_start+ pool_size

                    for c in range (C_prev):
                        pool_slice = A[i,vert_start:vert_end,horiz_start:horiz_end,c]
                        if mode == "max":
                            P[i,h,w,c] = np.max(pool_slice)
                        elif mode == "average":
                            P[i, h, w, c] = np.mean(pool_slice)
                        else:
                            raise ValueError("mode must be 'max' or 'average'")
    cache = (A, pool_size, stride, mode)

    
    return P, cache 
    
def flatten_forward(P):
    original_shape = P.shape
    m = P.shape[0]

    F = P.reshape(m, -1).T

    cache = original_shape

    return F, cache

def initialize_dense(F):
    W_dense = np.random.randn(1, F.shape[0]) * np.sqrt(1 /  F.shape[0])
    b_dense = np.zeros((1, 1))
    return W_dense, b_dense

def dense_forward (F,W_dense,b_dense):
    Z_dense = W_dense @ F +b_dense
    AL = sigmoid(Z_dense)

    cache = (F, W_dense, b_dense, Z_dense)
    return AL, cache
def compute_cost(AL, Y):
    

    AL = np.clip(AL, 1e-8, 1 - 1e-8)

    cost = -np.mean(Y * np.log(AL)+ (1 - Y) * np.log(1 - AL))

    return cost



def dense_backward(AL,Y,cache):
    F, W_dense,b_dense,Z_dense = cache 
    m = Y.shape[1]
    dZ_dense = AL - Y
    dW_dense = (dZ_dense @ F.T) / m
    db_dense = np.sum(dZ_dense,axis=1,keepdims=True) / m
    dF = W_dense.T @ dZ_dense
    return dF, dW_dense, db_dense

def flatten_backward(dF, original_shape):
    dP = dF.T.reshape(original_shape)
    return dP


def pool_backward(dP, cache):
    A, pool_size, stride, mode = cache

    m, H_prev, W_prev, C_prev = A.shape
    _, H_out, W_out, _ = dP.shape

    dA = np.zeros_like(A)

    for i in range(m):
        for h in range(H_out):
            for w in range(W_out):
                vert_start = h * stride
                vert_end = vert_start + pool_size

                horiz_start = w * stride
                horiz_end = horiz_start + pool_size

                for c in range(C_prev):
                    gradient = dP[i, h, w, c]

                    if mode == "max":
                        A_slice = A[
                            i,
                            vert_start:vert_end,
                            horiz_start:horiz_end,
                            c
                        ]

                        # True only where the maximum occurred
                        mask = A_slice == np.max(A_slice)

                        dA[
                            i,
                            vert_start:vert_end,
                            horiz_start:horiz_end,
                            c
                        ] += mask * gradient

                    elif mode == "average":
                        distributed_gradient = (
                            gradient / (pool_size * pool_size)
                        )

                        dA[
                            i,
                            vert_start:vert_end,
                            horiz_start:horiz_end,
                            c
                        ] += distributed_gradient

                    else:
                        raise ValueError(
                            "mode must be 'max' or 'average'"
                        )

    return dA


def leaky_relu_backward(dA, Z, alpha=0.001):
    derivative = np.where(Z > 0, 1.0, alpha)
    dZ = dA * derivative

    return dZ


def conv_backward(dZ, cache):
    X, W, b, Z, stride, padding = cache

    m, H_prev, W_prev, C_prev = X.shape
    f, _, _, C_out = W.shape
    _, H_out, W_out, _ = dZ.shape

    X_pad = pad(X, padding)
    dX_pad = np.zeros_like(X_pad)

    dW = np.zeros_like(W)
    db = np.zeros_like(b)

    for i in range(m):
        for h in range(H_out):
            for w in range(W_out):
                vert_start = h * stride
                vert_end = vert_start + f

                horiz_start = w * stride
                horiz_end = horiz_start + f

                X_slice = X_pad[i,vert_start:vert_end,horiz_start:horiz_end,:]

                for c in range(C_out):
                    current_gradient = dZ[i, h, w, c]

            
                    dX_pad[i,vert_start:vert_end,horiz_start:horiz_end,:] += W[:, :, :, c] * current_gradient

                    # Gradient with respect to this filter
                    dW[:, :, :, c] += (
                        X_slice * current_gradient
                    )

                    # Gradient with respect to this filter's bias
                    db[0, 0, 0, c] += current_gradient

    # Average parameter gradients across examples
    dW /= m
    db /= m

    # Remove padding from dX
    if padding == 0:
        dX = dX_pad
    else:
        dX = dX_pad[
            :,
            padding:-padding,
            padding:-padding,
            :
        ]

    return dX, dW, db

def backward_propagation(
    AL,
    Y,
    dense_cache,
    flatten_cache,
    pool_cache,
    conv_cache
):
    # Dense and sigmoid backward
    dF, dW_dense, db_dense = dense_backward(
        AL,
        Y,
        dense_cache
    )

    # Reverse flatten
    dP = flatten_backward(
        dF,
        flatten_cache
    )

    # Pooling backward
    dA = pool_backward(
        dP,
        pool_cache
    )

    # Extract Z from convolution cache
    X, W_conv, b_conv, Z, stride, padding = conv_cache

    # Leaky ReLU backward
    dZ = leaky_relu_backward(
        dA,
        Z,
        alpha=0.001
    )

    # Convolution backward
    dX, dW_conv, db_conv = conv_backward(
        dZ,
        conv_cache
    )

    gradients = {
        "dW_dense": dW_dense,
        "db_dense": db_dense,
        "dW_conv": dW_conv,
        "db_conv": db_conv,
        "dX": dX
    }

    return gradients

def update_parameters(
    W_conv,
    b_conv,
    W_dense,
    b_dense,
    gradients,
    learning_rate
):
    W_conv -= learning_rate * gradients["dW_conv"]
    b_conv -= learning_rate * gradients["db_conv"]

    W_dense -= learning_rate * gradients["dW_dense"]
    b_dense -= learning_rate * gradients["db_dense"]

    return W_conv, b_conv, W_dense, b_dense

def train_cnn(
    X,
    Y,
    filter_size=3,
    num_filters=8,
    conv_stride=1,
    padding=1,
    pool_size=2,
    pool_stride=2,
    pool_mode="max",
    learning_rate=0.01,
    num_iterations=100
):
    input_channels = X.shape[3]

    # Initialize convolution parameters
    W_conv, b_conv = initialize_params(
        filter_size,
        input_channels,
        num_filters
    )

    # Run one temporary forward pass to determine flattened size
    A, _ = conv_forward(
        X,
        W_conv,
        b_conv,
        stride=conv_stride,
        padding=padding
    )

    P, _ = pool(
        A,
        pool_size=pool_size,
        stride=pool_stride,
        mode=pool_mode
    )

    F, _ = flatten_forward(P)

    # Initialize dense parameters
    W_dense, b_dense = initialize_dense(F)

    costs = []

    for iteration in range(num_iterations):

        # Forward propagation
        A, conv_cache = conv_forward(
            X,
            W_conv,
            b_conv,
            stride=conv_stride,
            padding=padding
        )

        P, pool_cache = pool(
            A,
            pool_size=pool_size,
            stride=pool_stride,
            mode=pool_mode
        )

        F, flatten_cache = flatten_forward(P)

        AL, dense_cache = dense_forward(
            F,
            W_dense,
            b_dense
        )

        cost = compute_cost(AL, Y)

        # Backward propagation
        gradients = backward_propagation(
            AL,
            Y,
            dense_cache,
            flatten_cache,
            pool_cache,
            conv_cache
        )

        # Update parameters
        W_conv, b_conv, W_dense, b_dense = update_parameters(
            W_conv,
            b_conv,
            W_dense,
            b_dense,
            gradients,
            learning_rate
        )

        costs.append(cost)

        if iteration % 10 == 0:
            predictions = (AL >= 0.5).astype(int)
            accuracy = np.mean(predictions == Y) * 100

            print(
                f"Iteration {iteration}: "
                f"cost = {cost:.6f}, "
                f"accuracy = {accuracy:.2f}%"
            )

    parameters = {
        "W_conv": W_conv,
        "b_conv": b_conv,
        "W_dense": W_dense,
        "b_dense": b_dense,
        "filter_size": filter_size,
        "conv_stride": conv_stride,
        "padding": padding,
        "pool_size": pool_size,
        "pool_stride": pool_stride,
        "pool_mode": pool_mode
    }

    return parameters, costs

parameters, costs = train_cnn(
    train_set_x,
    train_set_y,
    filter_size=3,
    num_filters=8,
    conv_stride=1,
    padding=1,
    pool_size=2,
    pool_stride=2,
    pool_mode="max",
    learning_rate=0.01,
    num_iterations=100
)

def predict(X, parameters):
    A, _ = conv_forward(
        X,
        parameters["W_conv"],
        parameters["b_conv"],
        stride=parameters["conv_stride"],
        padding=parameters["padding"]
    )

    P, _ = pool(
        A,
        pool_size=parameters["pool_size"],
        stride=parameters["pool_stride"],
        mode=parameters["pool_mode"]
    )

    F, _ = flatten_forward(P)

    AL, _ = dense_forward(
        F,
        parameters["W_dense"],
        parameters["b_dense"]
    )

    predictions = (AL >= 0.5).astype(int)

    return predictions, AL

train_predictions, train_probabilities = predict(
    train_set_x,
    parameters
)

test_predictions, test_probabilities = predict(
    test_set_x,
    parameters
)

train_accuracy = np.mean(
    train_predictions == train_set_y
) * 100

test_accuracy = np.mean(
    test_predictions == test_set_y
) * 100

print("Train accuracy:", train_accuracy)
print("Test accuracy:", test_accuracy)

test_data.close()
train_data.close()