
def simpleExample():
    inputs = [1.2, 5.1, 2.1]
    weights = [3.1, 2.1, 8.7]
    bias = 3

    n = len(inputs)

    output = 0
    for i in range(n):
        output += inputs[i] * weights[i]

    output += bias

    print(output)