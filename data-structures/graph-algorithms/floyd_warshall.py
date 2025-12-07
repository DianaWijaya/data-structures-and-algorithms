def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm is an all-pairs shortest path algorithm that finds the shortest path between every pair of vertices in a
    weighted graph. The algorithm works for both directed and undirected graphs and can handle negative edge weights.

    Time complexity: O(V^3), where V is the number of vertices in the graph
    Space complexity: O(V^2), where V is the number of vertices in the graph
    """
    distance = {u: {v: float('infinity') for v in graph} for u in graph}
    for u in graph:
        distance[u][u] = 0
        for v in graph[u]:
            distance[u][v] = graph[u][v]

    for k in graph:
        for u in graph:
            for v in graph:
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])

    return distance