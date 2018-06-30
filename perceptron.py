import numpy as np

class Perceptron():
    def __init__(self, weights, bias, values):
        self.weights = weights
        self.bias = bias
        self.values = values

    def step_function(self, x):
        return 1 if x >= 0 else 0
    
    def perceptron_output(self.weights, self.bias, self.values):
        calculation = np.dot(self.weights, self.values) + bias
        return self.step_function(calculation)

# Example of using
network = Perceptron([2,2], -2, [1,1])
network.perceptron_output()

