# class to represent a graph object
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

def bellman_ford(graph, start):
    """
    Bellman-Ford algorithm is a single-source shortest path algorithm that finds the shortest path from a source vertex to all other
    vertices in a weighted graph. The algorithm can handle negative edge weights.

    Time complexity: O(V*E), where V is the number of vertices and E is the number of edges in the graph
    Space complexity: O(V), where V is the number of vertices in the graph
    """
    graph = {
        'S': {'A': -1, 'B': -1},
        'A': {'C': -1, 'D': -1},
        'B': {'A': -1, 'C': -1, 'D': -1},
        'C': {'E': -1},
        'D': {'E': -1},
        'E': {}
    }

    # Initialize the distance table
    distance = {node: float('inf') for node in graph}
    distance['S'] = 0  # The distance from the source to itself is 0

    # Number of vertices in the graph
    V = len(graph)

    # Relax edges repeatedly
    for _ in range(V - 1):
        for u in graph:
            for v in graph[u]:
                if distance[v] > distance[u] + graph[u][v]:
                    distance[v] = distance[u] + graph[u][v]
        
        print("Iteration", _ + 1)
        for key, value in distance.items():
            print(key, value)

    # Check for negative cycles
    negative_cycle = False
    for u in graph:
        for v in graph[u]:
            if distance[v] > distance[u] + graph[u][v]:
                negative_cycle = True
                print("Negative cycle detected")
                break
        if negative_cycle:
            break

    # Print the final distances
    print("Final distances:")
    for key, value in distance.items():
        print(key, value)
