def depth_first_search(graph, start):
    """
    Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root
    node and explores as far as possible along each branch before backtracking.

    Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph
    Space complexity: O(V), where V is the number of vertices in the graph
    """
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited