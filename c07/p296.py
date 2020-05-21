from pythonds.graphs import PriorityQueue, Graph, Vertex


def prim(G: Graph, start: Vertex):
    pq = PriorityQueue()

    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)

    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])

    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getDistance():
                newVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pd.decreaseKey(nextVert, newCost)
