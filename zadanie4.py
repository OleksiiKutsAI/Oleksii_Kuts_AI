import numpy as np
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, n_inputs, bias=0.0, weights=None):
        self.bias = bias
        self.weights = np.array(weights) if weights else np.random.rand(n_inputs)

    def activate(self, x):
        return max(0.1 * x, x)

    def __call__(self, inputs):
        return self.activate(np.dot(inputs, self.weights) + self.bias)

n_inputs = 3
n_hidden_neurons_1 = 4
n_hidden_neurons_2 = 4
n_outputs = 1

# Tworzenie warstw
layers = [
    [Neuron(n_inputs) for _ in range(n_hidden_neurons_1)],
    [Neuron(n_hidden_neurons_1) for _ in range(n_hidden_neurons_2)],
    [Neuron(n_hidden_neurons_2, weights=[1.0]) for _ in range(n_outputs)],
]

def visualize_network(layers):
    fig, ax = plt.subplots()

    # Warstwa wejściowa
    for i in range(n_inputs):
        ax.plot([0, 1], [i, i], 'r-', alpha=0.5)
        ax.plot(1, i, 'rs', markersize=10)
        ax.text(1.1, i, f"Wejście {i + 1}", ha='left', va='center')  # Zmieniono ha na 'left'
    ax.text(-0.2, n_inputs / 2 - 0.5, 'warstwa wejściowa', fontsize=10, color='r', rotation=90, ha='center', va='center')

    # Pierwsza warstwa ukryta
    for i in range(n_hidden_neurons_1):
        for j in range(n_inputs):
            ax.plot([1, 1.5], [j, i], 'b-', alpha=0.5)
        ax.plot(1.5, i, 'bo', markersize=10)
        ax.text(1.6, i, f"Ukryta 1-{i + 1}", ha='left', va='center')  # Zmieniono ha na 'left'
    ax.text(1.25, n_hidden_neurons_1 / 2 - 0.5, 'warstwa ukryta 1', fontsize=10, color='b', rotation=90, ha='center', va='center')

    # Druga warstwa ukryta
    for i in range(n_hidden_neurons_2):
        for j in range(n_hidden_neurons_1):
            ax.plot([1.5, 2], [j, i], 'b-', alpha=0.5)
        ax.plot(2, i, 'bo', markersize=10)
        ax.text(2.1, i, f"Ukryta 2-{i + 1}", ha='left', va='center')  # Zmieniono ha na 'left'
    ax.text(1.75, n_hidden_neurons_2 / 2 - 0.5, 'warstwa ukryta 2', fontsize=10, color='b', rotation=90, ha='center', va='center')

    # Warstwa wyjściowa
    for i in range(n_outputs):
        for j in range(n_hidden_neurons_2):
            ax.plot([2, 2.5], [j, i], 'b-', alpha=0.5)
        ax.plot(2.5, i, 'go', markersize=10)
        ax.text(2.6, i, f"Wyjście {i + 1}", ha='left', va='center')  # Zmieniono ha na 'left'
    ax.text(2.25, 0, 'warstwa wyjściowa', fontsize=10, color='g', rotation=90, ha='center', va='center')

    ax.set_xlabel('Neurony')
    ax.set_ylabel('Warstwa')
    ax.set_title('Struktura Sieci Neuronowej')

    plt.tight_layout()
    plt.show()

visualize_network(layers)
