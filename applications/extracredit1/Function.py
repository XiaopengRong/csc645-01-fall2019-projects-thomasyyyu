class Function(object):

    def calculateShortestPath(self, startVertex, vertexList, edgeList):
        # originally, min distance was set to infinity, or max system size.
        startVertex.minDistance = 0
        for _ in range(0, len(vertexList) - 1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.destVertex
                distance = u.minDistance + edge.weight

                if distance < v.minDistance:
                    v.minDistance = distance

