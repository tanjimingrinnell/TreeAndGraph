from GraphDFS import *

class vertex:
    v = 0
    adjacentVertices = []
    visited = False

    def __init__(self, inputVertex, inputVertices):
        self.v = inputVertex
        self.adjacentVertices = inputVertices

# a complete graph of order 4 (or C_4 graph)
adjacentV1 = [2, 3, 4]
adjacentV2 = [1, 3, 4]
adjacentV3 = [1, 2, 4]
adjacentV4 = [1, 2, 3]
v1 = vertex(1, adjacentV1)
v2 = vertex(2, adjacentV2)
v3 = vertex(3, adjacentV3)
v4 = vertex(4, adjacentV4)
graphC4 = []
graphC4.append(v1)
graphC4.append(v2)
graphC4.append(v3)
graphC4.append(v4)

#random graph of order 8
g8v1 = vertex(1, [2, 4])
g8v2 = vertex(2, [1, 3])
g8v3 = vertex(3, [2, 5])
g8v4 = vertex(4, [1, 5, 6, 7])
g8v5 = vertex(5, [4 ,3])
g8v6 = vertex(6, [4, 8])
g8v7 = vertex(7, [4, 8])
g8v8 = vertex(8, [6, 7])

graphV8 = [g8v1, g8v2, g8v3, g8v4, g8v5, g8v6, g8v7, g8v8]

graphDFS(graphC4)

print ""

graphDFS(graphV8)