import nodeClass
from sklearn import datasets
import math
import random

iris = datasets.load_iris()

nodes = [nodeClass.Node() for count in xrange(5)]



irisD = iris.data.tolist()



#First Layer

#Weights are assigned
nodes[0].weights = [0.2,-0.3,0.4,-0.9,0.7]
nodes[1].weights = [0.3,-0.5,0.7,0.6,-0.6]

#Values are assigned
nodes[0].attribute = [-1] + irisD[0]
nodes[1].attribute = [-1] + irisD[0] # Add Bias to front of values

nodes[0].value = nodes[0].math1()


nodes[1].value = nodes[1].math1()

nodes[0].activation = nodes[0].activator(nodes[0].value)

nodes[1].activation = nodes[1].activator(nodes[1].value)

#Second Layer
nodes[2]
nodes[3]
nodes[4]


nodes[2].weights = [-0.9,0.7,0.6,-0.6]
nodes[3].weights = [0.3,-0.5,0.2,-0.3]
nodes[4].weights = [0.7,0.6,0.4,-0.9]

nodes[2].attribute = [-1] + [nodes[0].value] + [nodes[1].value]
nodes[3].attribute = [-1] + [nodes[0].value] + [nodes[1].value]
nodes[4].attribute = [-1] + [nodes[0].value] + [nodes[1].value]

nodes[2].value = nodes[2].math1()
nodes[3].value = nodes[3].math1()
nodes[4].value = nodes[4].math1()

nodes[2].activation = nodes[2].activator(nodes[2].value)
nodes[3].activation = nodes[3].activator(nodes[3].value)
nodes[4].activation = nodes[4].activator(nodes[4].value)

if nodes[2].value < nodes[2].activation:
    print 0
else:
    print 1

if nodes[3].value < nodes[3].activation:
    print 0
else:
    print 1

if nodes[4].value < nodes[4].activation:
    print 0
else:
    print 1