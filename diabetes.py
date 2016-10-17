import nodeClass

file = open('idd.data', 'r')

file.readline()
diabetes = []

for line in file:
    words = line.split()
    diabetes.append(words)



nodes = [nodeClass.Node() for count in xrange(10)]

nodes[0].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[1].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[2].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[3].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[4].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[5].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[6].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[7].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[8].weights = [1.1,2.1,0.7,0.8,2.0]
nodes[9].weights = [1.1,2.1,0.7,0.8,2.0]

nodes[1].attribute = diabetes[0][0]
nodes[2].attribute = diabetes[0][1]
nodes[3].attribute = diabetes[0][2]
nodes[4].attribute = diabetes[0][3]
nodes[5].attribute = diabetes[0][4]
nodes[6].attribute = diabetes[0][5]
nodes[7].attribute = diabetes[0][6]
nodes[8].attribute = diabetes[0][7]
nodes[9].attribute = diabetes[0][8]

nodes[0].value = -1
nodes[1].value = 1
nodes[2].value = 0
nodes[3].value = 1
nodes[4].value = 0
nodes[5].value = 1
nodes[6].value = 0
nodes[7].value = 0
nodes[8].value = 1
nodes[9].value = 0

for x in xrange(10):
    print nodes[x].value
