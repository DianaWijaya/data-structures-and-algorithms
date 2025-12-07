def breadth_first_search(graph, start):
    """
    Breadth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root
    node and explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

    Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph
    Space complexity: O(V), where V is the number of vertices in the graph
    """
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))

    return visited