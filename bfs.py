
from graph import Graph

conGraph = Graph({
    "0": {
        "2": {},
        "3": {}
    },
    "1": {
        "8": {}
    },
    "2": {
        "0": {},
        "3": {},
        "8": {}
    },
    "3": {
        "0": {},
        "2": {},
        "8": {},
    },
    "4": {
        "9": {},
        "7": {},
        "10": {}
    },
    "5": {
        "9": {},
        "6": {},
    },
    "6": {
        "5": {},
        "9": {}
    },
    "7": {
        "4": {},
        "10": {}
    },
    "8": {
        "1": {},
        "2": {},
        "3": {},
        "10": {},
    },
    "9": {
        "4": {},
        "5": {},
        "6": {},
    },
    "10": {
        "4": {},
        "8": {},
        "7": {},
    },
})

discGraph = Graph({
    "1": {
        "3": {}
    },
    "2": {
        
    },
    "3": {
        "1": {}
    },
    
})

def bfs(graph, start, find):
    visited = set({start})
    queue = [[start]]
    while len(queue) > 0:
        path = queue.pop(0)
        actual = path[-1]
        children = graph.getAdjacents(actual);
        for child in children:
            if child == find:  
                path.append(child)
                return {
                    "distance": len(path),
                    "path": path
                }

            if not child in visited :
                new_path = list(path)
                new_path.append(child)
                queue.append(new_path)
    return None;
    
def verifyConnectedGraph(graph):
    edges = graph.getEdges()
    restEdges = edges
    for firstEdge in edges:
        restEdges.remove(firstEdge)
        for secondEdge in restEdges:
            result = bfs(graph, firstEdge, secondEdge)
            if result == None:
                print("It is not a connected graph.")
                return
    print("It is a connected graph.")
    
verifyConnectedGraph(discGraph)
