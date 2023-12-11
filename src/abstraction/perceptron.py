import numpy as np

############################################################################
# ReLU
# If there is a negetive value then we get when the fucntion deactivates.

############################################################################

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]
    
class LayerDense:
    def __init__(self, n_inputs, n_nuerons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_nuerons)
        self.biases = np.zeros((1, n_nuerons))
    
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
def someExample():
    layer1 = LayerDense(4, 5)
    layer2 = LayerDense(5, 2)
    
    layer1.forward(X)
    print("Layer 1")
    print(layer1.output)
    
    layer2.forward(layer1.output)
    print("Layer 2")
    print(layer2.output)