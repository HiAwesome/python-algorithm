from pythonds.graphs import PriorityQueue, Graph, Vertex


def dijkstra(aGraph: Graph, start: Vertex):
    pq = PriorityQueue()
    start.setDistance(0)

    pq.buildHeap([(v.getDistance(), v) for v in aGraph])

    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pd.decreaseKey(nextVert, newDist)
