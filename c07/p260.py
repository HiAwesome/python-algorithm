from pprint import pprint


class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:

    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertDict[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertDict

    def addEdge(self, f, t, cost=0):
        if f not in self.vertDict:
            self.addVertex(f)

        if t not in self.vertDict:
            self.addVertex(t)

        self.vertDict[f].addNeighbor(self.vertDict[t], cost)

    def getVertices(self):
        return self.vertDict.keys()

    def __iter__(self):
        return iter(self.vertDict.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    pprint(g.vertDict)

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print('(%s, %s)' % (v.getId(), w.getId()))

"""
{0: <__main__.Vertex object at 0x107abc510>,
 1: <__main__.Vertex object at 0x107abcdd0>,
 2: <__main__.Vertex object at 0x107ac7450>,
 3: <__main__.Vertex object at 0x107ac7490>,
 4: <__main__.Vertex object at 0x107ac74d0>,
 5: <__main__.Vertex object at 0x107ac7510>}
 
(0, 1)
(0, 5)
(1, 2)
(2, 3)
(3, 4)
(3, 5)
(4, 0)
(5, 4)
(5, 2)
"""
