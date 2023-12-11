
def singleNeuron():
    inputs = [1.2, 5.1, 2.1]
    weights = [3.1, 2.1, 8.7]
    bias = 3

    n = len(inputs)

    output = 0
    for i in range(n):
        output += inputs[i] * weights[i]

    output += bias

    print(output)
    
def layeredNeuron():
    inputs = [1, 2, 3, 2.5]
    
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]
    
    bias = [2,3,0.5]
    
    output = []
    for n_weights, n_bias in zip(weights, bias):
        out_neuron =  0
        for n_weight, n_input in zip(n_weights, inputs):
            out_neuron += n_input * n_weight
        out_neuron += n_bias
        output.append(out_neuron)
        
    print(output)

# input[0] * weight[0] + input[0]*weight[1] + input[2]*weight[2] + bias[0]
#