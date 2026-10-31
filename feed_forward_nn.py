import numpy as np

# activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# simple XOR inputs and expected outputs
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
expected = np.array([[0], [1], [1], [0]])

# We need 2 input neurons, 2 hidden neurons, 1 output neuron
hidden_weights = np.random.uniform(size=(2, 2))
hidden_bias = np.random.uniform(size=(1, 2))

output_weights = np.random.uniform(size=(2, 1))
output_bias = np.random.uniform(size=(1, 1))

# Feed forward step
hidden_activation = np.dot(inputs, hidden_weights) + hidden_bias
hidden_output = sigmoid(hidden_activation)

output_activation = np.dot(hidden_output, output_weights) + output_bias
predicted_output = sigmoid(output_activation)

print("Predicted Output after one feed forward pass:")
print(predicted_output)
