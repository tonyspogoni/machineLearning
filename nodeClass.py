import math
class Node:

    value = 0
    numOfWeights = 0
    layers = 0
    weights = []
    attribute = []
    bias = -1
    activation = 0

    def __int__(self, value, numOfWeights, layers, weights,attribute,bias,activation):
        self.value = value
        self.numOfWeights = numOfWeights
        self.layers = layers
        self.weights = weights
        self.attribute = attribute
        self.bias = bias
        self.activation = activation

    def math1(self):
        answer = [weights*attribute for weights,attribute in zip(self.weights,self.attribute)]
        ranswer = sum(answer)
        return ranswer


    def activator(self,value):
        x = value * -1
        return 1 / (1 + math.pow(math.e, x))