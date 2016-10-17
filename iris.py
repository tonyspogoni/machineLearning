import nodeClass
from sklearn import datasets
import random

iris = datasets.load_iris()

nodes = [nodeClass.Node() for count in xrange(5)]

nodes[0].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[1].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[2].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[3].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[4].weights = [1.1,2.1,0.7,0.8,2.0]

irisD = iris.data.tolist()

nodes[1].attribute = irisD[0][0]
nodes[2].attribute = irisD[0][1]
nodes[3].attribute = irisD[0][2]
nodes[4].attribute = irisD[0][3]

nodes[0].value = -1
nodes[1].value = 0
nodes[2].value = 1
nodes[3].value = 0
nodes[4].value = 1

for x in xrange(5):
    print nodes[x].value