from pythonds.graphs import Graph, Vertex


def knightGraph(bdSize):
    ktGraph = Graph()

    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)

    return ktGraph


def posToNodeId(row, column, board_size):
    return (row * board_size) + column


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = ((-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1))

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]

        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))

    return newMoves


def legalCoord(x, bdSize):
    return True if 0 <= x < bdSize else False


def knightTour(n, path, u: Vertex, limit):
    u.setColor('gray')
    path.append(u)

    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i += 1

        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
        else:
            done = True

        return done


def orderByAvail(n: Vertex):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor == 'white':
                    c += 1

            resList.append((c, v))

    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]
