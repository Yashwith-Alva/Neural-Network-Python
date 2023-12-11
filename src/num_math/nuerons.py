import numpy as np

# y = mx + c, where m = weight, x is input and c is bias.
def layeredNeuron():
    inputs = [1, 2, 3, 2.5]
    
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]
    
    bias = [2,3,0.5]
    
    output = np.dot(weights, inputs) + bias
    print(output)
    
def batchedNeurons():
    inputs = [[1, 2, 3, 2.5],
              [2.0, 5.0, -1.0, 2.0],
              [-1.5, 2.7, 3.3, -0.8]]
    
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]
    
    bias = [2,3,0.5]
    
    output = np.dot(inputs, np.array(weights).T) + bias
    print(output)
    
def multiLayerNeurons():
    inputs = [[1, 2, 3, 2.5],
              [2.0, 5.0, -1.0, 2.0],
              [-1.5, 2.7, 3.3, -0.8]]
    
    layer1_weights = [[0.2, 0.8, -0.5, 1.0],
                      [0.5, -0.91, 0.26, -0.5],
                      [-0.26, -0.27, 0.17, 0.87]]
    
    layer1_bias = [2,3,0.5]
    
    layer2_weights = [[0.1, -0.14, 0.5],
                      [-0.5, 0.12, -0.33],
                      [-0.44, 0.73, -0.13]]
    
    layer2_bias = [-1, 2, -0.5]
    
    layer1_out = np.dot(inputs, np.array(layer1_weights).T) + layer1_bias
    layer2_out = np.dot(layer1_out, np.array(layer2_weights).T) + layer2_bias
    
    print(layer2_out)