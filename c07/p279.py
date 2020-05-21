from pythonds.graphs import Graph, Vertex


class DFSGraph(Graph):

    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsVisit(aVertex)

    def dfsVisit(self, startVertex: Vertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsVisit(nextVertex)

        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
