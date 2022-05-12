class Graph:
    def __init__(self, adjacencies):
            self.adjacencies = adjacencies
    
    def qtyEdges(self):
        return len(self.adjacencies.keys())
        
    def qtyVertexes(self):
        count = 0
        for key in self.adjacencies:
            count += len(self.adjacencies[key])
        return count/2
        
    def getEdges(self):
        edges = []
        for key in self.adjacencies:
            edges.append(key)
        return edges
    
    def getAdjacents(self, edge):
        neighbours = []
        for key in self.adjacencies[edge]:
            neighbours.append(key)
        return neighbours
    
    def getDegree(self, edge):
        neighbours = []
        for key in self.adjacencies[edge]:
            neighbours.append(key)
        return len(neighbours)
    
    def addEdge(self, edge, neighbours):
        if self.adjacencies.get(edge) != None:
            print("Edge already registered.")
        else:
            newEdge = {}
            for i in neighbours:
                newEdge[i] = {}
                self.adjacencies[i][edge] = {} 
            self.adjacencies[edge] = newEdge
    
    def removeEdge(self, edge):
        neighbours = self.adjacencies.get(edge)
        for key in neighbours:
            self.adjacencies[key].pop(edge) 
        self.adjacencies.pop(edge)
        
    def addVertex(self, v, w):
        self.adjacencies[v][w] = {}
        self.adjacencies[w][v] = {}
    
    def removeVertex(self, v, w):
        self.adjacencies[v].pop(w)
        self.adjacencies[w].pop(v)
        
