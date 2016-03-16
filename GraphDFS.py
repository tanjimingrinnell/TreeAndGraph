
def graphDFS(graphList):
    graphDFSRecursive(graphList[0], graphList)

def graphDFSRecursive(currentVertex, graphList):
    currentVertex.visited = True
    print currentVertex.v
    for vertex in currentVertex.adjacentVertices:
        if not(graphList[vertex - 1].visited):
            graphDFSRecursive(graphList[vertex - 1], graphList)