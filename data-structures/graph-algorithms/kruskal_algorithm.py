def kruskal_algorithm(graph):
    """
    Kruskal's algorithm is a minimum spanning tree algorithm that finds an edge of the least possible weight that connects any two
    trees in the forest. It is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph.

    Time complexity: O(E log V), where V is the number of vertices and E is the number of edges in the graph
    Space complexity: O(V), where V is the number of vertices in the graph
    """
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    result = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []

    for node in range(len(graph)):
        parent.append(node)
        rank.append(0)

    while e < len(graph) - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    return result