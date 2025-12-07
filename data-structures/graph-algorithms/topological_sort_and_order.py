def topological_sort(graph):
    """
    Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v,
    vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

    Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph
    Space complexity: O(V), where V is the number of vertices in the graph
    """
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)

    visited = set()
    stack = []

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]

class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # stores in-degree of a vertex
        # initialize in-degree of each vertex by 0
        self.indegree = [0] * N
 
        # add edges to the undirected graph
        for (src, dest) in edges:
 
            # add an edge from source to destination
            self.adjList[src].append(dest)
 
            # increment in-degree of destination vertex by 1
            self.indegree[dest] = self.indegree[dest] + 1
 
 
# Recursive function to find all topological orderings of a given DAG
def findAllTopologicalOrders(graph, path, discovered, N):
 
    # do for every vertex
    for v in range(N):
 
        # proceed only if in-degree of current node is 0 and
        # current node is not processed yet
        if graph.indegree[v] == 0 and not discovered[v]:
 
            # for every adjacent vertex u of v, 
            # reduce in-degree of u by 1
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] - 1
 
            # include current node in the path 
            # and mark it as discovered
            path.append(v)
            discovered[v] = True
 
            # recursively call to continue to find
            findAllTopologicalOrders(graph, path, discovered, N)
 
            # backtrack: reset in-degree 
            # information for the current node
            for u in graph.adjList[v]:
                graph.indegree[u] = graph.indegree[u] + 1
 
            # backtrack: remove current node from the path and
            # mark it as undiscovered
            path.pop()
            discovered[v] = False
 
    # print the topological order if 
    # all vertices are included in the path
    if len(path) == N:
        print(path)
      
        
# Print all topological orderings of a given DAG
def printAllTopologicalOrders(graph):
    N = len(graph.adjList)
 
    discovered = [False] * N
 
    path = []
 
    findAllTopologicalOrders(graph, path, discovered, N)
