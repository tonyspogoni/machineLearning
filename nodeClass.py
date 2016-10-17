class Node:

    value = 0
    numOfWeights = 0
    layers = 0
    weights = []
    attribute = 0

    def __int__(self, value, numOfWeights, layers, weights,attribute):
        self.value = value
        self.numOfWeights = numOfWeights
        self.layers = layers
        self.weights = weights
        self.attribute = attribute