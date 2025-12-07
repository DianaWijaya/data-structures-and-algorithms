from collections import deque

class Edge:
    def __init__(self, start_node, end_node, flow, capacity):
        """
        Function description:
        Initialize an edge with the starting node, target node, flow, and capacity. The reversed edge
        is also initialized to None initially.

        Input:
            start_node: Starting node of the edge
            end_node: Target node of the edge
            flow: Flow that passes through this edge
            capacity: Maximum flow that can pass through this edge

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only initializes the edge.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the edge.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input is constant because it only takes in constant number of inputs.
        """
        self.start_node = start_node
        self.end_node = end_node
        self.flow = flow                    # Flow that passes through this edge
        self.capacity = capacity            # Maximum flow that can pass through this edge
        self.reversed_edge = None  

    def remaining_capacity(self):
        """
        Function description:
        Calculate the remaining capacity of the edge by subtracting the flow from the capacity.

        Input:
            None

        Return:
            The remaining capacity of the edge.

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only performs a simple subtraction operation.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the remaining capacity.

        Input space complexity:
            Complexity: O(1)
            Analysis: No input is taken.
        """
        return self.capacity - self.flow

    def __str__(self):
        """
        Function description:

        Input:
            None

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only returns the string representation of 
                      the edge.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the string.

        Input space complexity:
            Complexity: O(1)
            Analysis: No input is taken.
        """
        return f"{self.start_node.id}->{self.end_node.id} | flow:{self.flow} | capacity:{self.capacity}"


class Vertex:
    def __init__(self, id):
        """
        Function description:
        Initialize a vertex with the ID, edges, visited status, and parent edge. The edges are stored in
        a list, and the visited status is initially set to False. The parent edge is used to keep track of
        the edge that leads to the current vertex. 

        Input:
            id: The ID of the vertex

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only initializes the vertex.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the vertex.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input is constant because it only takes in the ID of the vertex.
        """
        self.id = id
        self.edges = []
        self.visited = False
        self.parent_edge = None

    def add_edge(self, edge):
        """
        Function description:
        Add an edge to the vertex's list of edges.

        Input:
            edge: The edge to be added to the vertex.

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only appends a single edge to the list.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the edge.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input is constant because it only takes in a single edge.
        """
        self.edges.append(edge)


class Graph:
    def __init__(self, num_of_vertices):
        """
        Function description:

        Input:
            num_of_vertices: The number of vertices in the graph.

        Return:
            None

        Time complexity:
            Complexity: O(n), where n is the number of vertices.
            Analysis: The time complexity is linear because it iterates through the number of vertices to
                      create the vertices.

        Space complexity:
            Complexity: O(n), where n is the number of vertices.
            Analysis: The space complexity is linear because it stores the vertices in a list.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input is constant because it only takes an input of the number of vertices.
        """
        self.num_of_vertices = num_of_vertices
        self.vertices = [Vertex(i) for i in range(num_of_vertices)]

    def add_edge(self, start_node_id, end_node_id, capacity):
        """
        Function description:
        Add an edge to the graph by creating the forward and reverse edges, and linking them to the respective
        vertices. The forward edge is created from the starting node to the target node, while the reverse edge
        is created from the target node to the starting node. The capacity of the reverse edge is initially set
        to 0.

        Input:
            start_node_id: The ID of the starting node of the edge
            end_node_id: The ID of the target node of the edge
            capacity: The maximum flow that can pass through the edge

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only creates the forward and reverse edges,
                      and links them to the respective vertices.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the forward and reverse edges.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input is constant because it only takes in the IDs of the starting and target nodes,
                      and the capacity of the edge.
        """
        start_vertex = self.vertices[start_node_id]
        end_vertex = self.vertices[end_node_id]

        # Create forward and reverse edges
        forward_edge = Edge(start_vertex, end_vertex, 0, capacity)
        reverse_edge = Edge(end_vertex, start_vertex, 0, 0)

        # Link the forward and reverse edges to their respective edges
        forward_edge.reversed_edge = reverse_edge
        reverse_edge.reversed_edge = forward_edge

        # Add edges to respective vertices
        start_vertex.edges.append(forward_edge)
        end_vertex.edges.append(reverse_edge)

    def get_vertex(self, id):
        """
        Function description:
        Get the vertex with the specified ID.

        Input:
            id: The ID of the vertex to be retrieved.

        Return:
            The vertex with the specified ID that is being searched for.

        Time complexity:
            Complexity: O(1) 
            Analysis: The time complexity is constant because it only retrieves the vertex using index from
                      the adjacency list.

        Space complexity:
            Complexity: O(1)
            Analysis: Nothing is stored.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input is constant because it only takes in a value for ID of the vertex.
        """
        if 0 <= id < self.num_of_vertices:
            return self.vertices[id]
        else:
            return None
        
    def get_edge(self, start_id, end_id):
        """
        Function description:
        Get the edge between the specified start and end nodes.

        Input:
            start_id: The ID of the starting node of the edge
            end_id: The ID of the target node of the edge

        Return:
            The edge between the specified start and end nodes, if it exists. Otherwise, return None.

        Time complexity:
            Complexity: O(E), where E is the number of edges.
            Analysis: The time complexity is linear because it iterates through the edges of the starting node
                      to find the edge that leads to the target node.

        Space complexity:
            Complexity: O(1)
            Analysis: A single edge is stored.

        Input space complexity:
            Complexity: O(1)
            Analysis: It only takes in values for IDs of the starting and target nodes.
        """
        if 0 <= start_id < self.num_of_vertices and 0 <= end_id < self.num_of_vertices:
            start_vertex = self.vertices[start_id]
            for edge in start_vertex.edges:
                if edge.end_node.id == end_id:
                    return edge
        return None

    def __str__(self):
        """
        Function description:
        Return the string representation of the graph.

        Input:
            None

        Return:
            The string representation of the graph.

        Time complexity:
            Complexity: O(VE), where V is the number of vertices and E is the number of edges.
            Analysis: The time complexity is O(VE) because it iterates through all the vertices and edges
                      to get the string representation of edges in each vertex.

        Space complexity:
            Complexity: O(VE), where V is the number of vertices and E is the number of edges.
            Analysis: The space complexity is O(VE) because it stores the string representation of all the edges
                      of each vertex in the graph, so the space depends on the amount of edges in each vertex.

        Input space complexity:
            Complexity: O(1)
            Analysis: No input is taken.
        """
        result = []
        for vertex in self.vertices:
            for edge in vertex.edges:
                if edge.capacity > 0:
                    result.append(str(edge))
        return "\n".join(result)
    

# This code is based on the lecture slides from FIT2004, Lecture 8 Network Flow, and from week 9 sanity check video
# Link: https://learning.monash.edu/pluginfile.php/3397786/mod_folder/content/0/Lecture08_NetworkFlow_v20220422_2308.pdf?forcedownload=1
class ResidualNetwork:
    def __init__(self, graph):
        """
        Function description:

        Input:
            graph: The graph to be used to create the residual network.

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant because it only initializes the residual network
                      with a graph

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant because it only stores the graph.

        Input space complexity:
            Complexity: O(1)
            Analysis: The input is constant because it only takes in a graph.
        """
        self.graph = graph

    def find_augmenting_path(self, start_node, end_node):
        """
        Function description:
        This function searches for an augmenting path in a flow network from a start node to an end node using 
        the Breadth First Search (BFS) algorithm.

        Approach description (if main function):
        I used Breadth First Search (BFS) instead of Depth First Search (DFS) in this function in ford fulkerson, 
        BFS is more efficient in finding the shortest path from the source to the sink. This choice primarily 
        uses the implementation of Edmonds-Karp algorithm. BFS ensures that the shortest path in terms of the 
        number of edges is found first before the algorithm proceeds to the next path. This is important later
        when the algorithm calculates the residual capacity of the path.
        
        The algorithm starts by visiting the source node, then iterates through the edges of the current node. 
        If the node is not visited and there is remaining capacity, the node is marked as visited, and the next 
        node is added to the queue. The algorithm continues until the end node is reached, then the path is 
        reconstructed by backtracking from the end node to the start node.

        Input:
            start_node: The starting node of the augmenting path
            end_node: The target node of the augmenting path

        Return:
            The augmenting path from the start node to the end node, if it exists. Otherwise, return an empty 
            list.

        Time complexity:
            Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
            Analysis: The initialization steps, including creating the queue, initializing the visited list, 
                      and resetting parent edges, take O(V) time. During the BFS traversal, each vertex and 
                      edge is processed exactly once, contributing O(V + E) time complexity. Then, the
                      reconstruction of path takes O(E) time. The total time complexity is O(V + E) + O(E) = 
                      O(V + E).

        Space complexity:
            Complexity: O(V), where V is the number of vertices.
            Analysis: All the vertices are stored in the queue and visited list, so the space complexity is
                      linear to the number of vertices.

        Input space complexity:
            Complexity: O(1)
            Analysis: It only takes in the value of index of the starting and target nodes.
        """

        # Space complexity: O(V), where V is the number of vertices
        # Create a queue for breadth first search algorithm, and add the starting node
        queue = deque([start_node])

        # Set all nodes to be unvisited
        visited = [False] * self.graph.num_of_vertices

        # Mark the starting node as visited
        visited[start_node] = True

        # Reset parent edges at the start of each new search, for backtracking
        for vertex in self.graph.vertices:
            vertex.parent_edge = None

        # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges
        # Breadth first search algorithm (Edmons-Karp Algorithm), iterate through queue until empty
        while queue:

            # Remove the first node from the queue
            current = queue.popleft()
            current_vertex = self.graph.vertices[current]

            # Iterate through the edges of the current node
            for edge in current_vertex.edges:
                next_node = edge.end_node.id

                # If the node is not visited and there is remaining capacity, set to visit and 
                # add next node to queue, until the end node is reached
                if not visited[next_node] and edge.remaining_capacity() > 0:
                    visited[next_node] = True

                    # Set the parent edge of the next node to the current edge, for backtracking
                    self.graph.vertices[next_node].parent_edge = edge
                    queue.append(next_node)

                    # Time complexity: O(E), where E is the number of edges
                    # If the end node is reached, reconstruct the path
                    if next_node == end_node:
                        return self.reconstruct_path(end_node)
                    
        # No path found, so return an empty list
        return []

    def reconstruct_path(self, end_node):
        """
        Function description:
        This function reconstructs the augmenting path from the end node to the start node by backtracking
        through the parent edges with th

        Input:
            end_node: The target node of the augmenting path

        Return:
            path: The augmenting path from the start node to the end node. If no parent edges are set,
                  returns an empty list.

        Time complexity:
            Complexity: O(E), where E is the number of edges.
            Analysis: Tt iterates through the edges of the path to reconstruct the path.

        Space complexity:
            Complexity: O(E), where E is the number of edges.
            Analysis: The space complexity is linear to the number of edges because it stores the path 
                      of the edges in a list.

        Input space complexity:
            Complexity: O(1)
            Analysis: It only takes in the value of the target node.
        """
        path = []

        # Start with the end node
        current = end_node

        # Time complexity: O(E), where E is the number of edges
        # Iterate until the start of the path, where the node has no more parent edge
        while self.graph.vertices[current].parent_edge is not None:

            # Retrieve the parent edge and append to the path
            edge = self.graph.vertices[current].parent_edge
            path.append(edge)
            current = edge.start_node.id

        # Reverse the path to correct the ordering, and return the path
        path.reverse()
        return path

    def residual_capacity(self, path):
        """
        Function description:
        This function calculates the residual capacity of the augmenting path by finding the minimum residual
        capacity of the edges in the path.

        Input:
            path: The augmenting path to find the residual capacity.

        Return:
            The residual capacity of the path.

        Time complexity:
            Complexity: O(E), where E is the number of edges.
            Analysis: It iterates through the path to find the minimum residual capacity by comparing the
                      remaining capacity.

        Space complexity:
            Complexity: O(1)
            Analysis: It stores a single value for the residual capacity.

        Input space complexity:
            Complexity: O(E), where E is the number of edges.
            Analysis: It takes in the path as input, so the input space is linear to the number of edges.
        """
        residual_capacity = float('inf')

        # Time complexity: O(E), where E is the number of edges
        # Iterate through the path to find the minimum residual capacity by comparing the remaining capacity
        for edge in path:
            if edge.remaining_capacity() < residual_capacity:
                residual_capacity = edge.remaining_capacity()

        return residual_capacity
    
    def augment_flow(self, path, flow):
        """
        Function description:
        This function augments the flow of the edges in the augmenting path by adding the flow to the edge,
        and subtracting the flow from the reversed edge. The flow is calculated from another method created,
        residual_capacity.

        Input:
            path: The augmenting path to augment the flow
            flow: The flow to be augmented

        Return:
            None

        Time complexity:
            Complexity: O(E), where E is the number of edges
            Analysis: It updates the flow of the edges in the path by iterating through each edge in the path.

        Space complexity:
            Complexity: O(1)
            Analysis: It does not store any additional space, because it only updates the flow of the edges.

        Input space complexity:
            Complexity: O(E), where E is the number of edges
            Analysis: It takes in the path as input, so the input space is linear to the number of edges. The
                      flow is just a singular value, so it is constant.
        """

        # Time complexity: O(E), where E is the number of edges
        # Update the flow of the edge, and the reversed edge, with the flow
        for edge in path:
            edge.flow += flow
            edge.reversed_edge.flow -= flow

    def max_flow(self, source_id, sink_id):
        """
        Function description:
        This function calculates the maximum flow from the source node to the sink node in the flow network 
        using the Ford-Fulkerson algorithm. It finds the augmenting path using the find_augmenting_path method,
        then calculates the residual capacity of the path, and augments the flow of the path. The process is
        repeated until there are no more augmenting paths to be found.

        Approach description (if main function):
        Since most of the functions are already implemented in the ResidualNetwork class, the max_flow function
        is implemented to find the maximum flow from the source node to the sink node. The function uses all the
        created function to start off with finding the augmenting path, then calculating the residual capacity
        of the path, and augmenting the flow of the path. The process is repeated until there are no more augmenting
        paths to be found. The function returns the maximum flow from the source node to the sink node.

        Input:
            source_id: The ID of the source node
            sink_id: The ID of the target node

        Return:
            max_flow: The maximum flow from the source node to the sink node.

        Time complexity:
            Complexity: O(V * E^2), where V is the number of vertices and E is the number of edges.
            Analysis: The time complexity is O(V * E^2) because the time complexity needed when running the
                      augmenting path is O(V + E), while both calculating the residual capacity and augmenting
                      the flow take O(E) time complexity. Since the while loop iterates until no more augmenting 
                      paths are found, it can run up to O(VE) times in the worst case.  where each edge may be 
                      incrementally augmented up to V times. Combining these complexities, the overall time 
                      complexity for the algorithm is derived as O(V * E^2).

        Space complexity:
            Complexity: O(E), where E is the number of edges.
            Analysis: The path when finding the augmenting path is stored in a list, so the space complexity is
                      linear to the number of edges.

        Input space complexity:
            Complexity: O(1)
            Analysis: It only takes in the values of the IDs of the source and sink nodes.
        """
        max_flow = 0

        # Time complexity: O(V * E^2), where V is the number of vertices and E is the number of edges
        # Iterate until there are no more augmenting paths to be found
        while True:

            # Space complexity: O(V + E), where V is the number of vertices and E is the number of edges
            # Time complexity: 
            # Find the augmenting path from the source node to the sink node
            path = self.find_augmenting_path(source_id, sink_id)

            # If there are no more augmenting paths, break the loop
            if not path:
                return max_flow
            
            # Time complexity: O(E), where E is the number of edges
            # Calculate the residual capacity of the path
            flow = self.residual_capacity(path)

            # Time complexity: O(E), where E is the number of edges
            # Augment the flow of the path
            self.augment_flow(path, flow)

            # Add the flow to the maximum flow
            max_flow += flow
            
        return max_flow


def allocate(preferences, officers_per_org, min_shifts, max_shifts):
    """
    Scenario:
    I am the manager of a security company, and I need to assign security officers to a group of companies 
    in a certain month with 30 days. Each company requires a certain number of officers for each shift, and 
    there are 3 shifts in total. Each officer has a preference for the shifts they want to work, and they
    can only work a minimum number of shifts and a maximum number of shifts in a month. I need to allocate
    the officers to the companies in such a way that all the constraints are met. All the officers must only
    work one shift a day, and the shift must be one of the shifts that they prefer. Then, each organization
    must have the exact amount of required number of officers for each shift each day. 

    Function description:
    This function allocates security officers to companies based on their preferences and the number of officers
    needed for each shift. All the requirements and constraints must be met, such as the minimum and maximum number
    of shifts an officer can work, and the number of officers needed for each shift. If with the given amount of 
    security officers, and company demands of officers per shift, there is no way to properly allocate the officers 
    to their preferred shifts, this function will return None. If there is a valid allocation, the function will 
    return a 4D list that specifies which officer is assigned to which company, on which shift, on which day.

    Approach description (if main function): 
    To start off, I initialized fixed values for easier reference, such as the number of officers, companies,
    shifts, and days. Then, I calculated the total number of nodes needed in the graph for the flow network, based
    on the given input numbers. 1 node is added for start, end, super source, and super sink. The, the amount of 
    nodes needed for each layer of the bipartite graph is calculated as follows:
        - security officers layer: number of officers
        - days layer: number of officers * number of days
        - shifts layer: number of officers * number of days * number of shifts
        - companies layer: number of companies * number of days * number of shifts
    Then, the fixed node IDs for source, sink, super source, and super sink are set for easier reference. The total
    number of officers needed for all companies and shifts is calculated. This value is needed in early terminations,
    demands, and to check for feasibility of the allocation.

    Then, I implemented multiple early terminations to avoid running unnecessary Graph creations and run time. First, 
    if the minimum shifts is greater than the maximum shifts, the function will return None. Second, if an officer's
    preference cannot even fulfill the minimum shifts, the function will return None. Third, if the minimum shift 
    capacity of officers cannot meet company demands, the function will return None. 

    Once all the obvious constraints are checked and passed, I created the graph for the flow network. This is done 
    using the Graph class I created, initialized with the size of the total number of nodes needed. I also initialized
    lists to store the indices of the nodes for each layer of the bipartite graph, so that I can easily connect the layers 
    of the bipartite graph, and get allocations reference numbers when the allocation is feasible.

    Next, we pre-process the demands to ensure that there are no nodes with any demand, as negative demands will be 
    connected to the super source, while positive demands will be connected to the super sink. The only nodes that has 
    demands were the start and end nodes, which were connected to the source and sink respectively. Then, each security
    officer also has a demand of minimum shift. 

    After the pre-processing, I connected the layers of the bipartite graph. I started by connecting the super source to
    each officer with the value of minimum shift needed. Then, the demand of the start is calculated by subtracting the
    total officers needed from the minimum shifts needed by all officers. This is then connected to which ever node that
    fulfills the demand. The start node is connected to each officer with the value of maximum minus minimum shifts.
    This approach makes sure that each officer must work at least the minimum number of shifts, but also at the same time, 
    cannot exceed the maximum number of shifts. Then, each security officer is connected to 30 days, with the value of 1,
    to ensure that each officer works only one shift a day. Each day, is then connected to 3 shifts, if the officer prefers
    that shift. Each shift is then connected to the companies, also with the value of 1, if the company needs 1 or more
    officers for that shift, and also if the security officer prefers that shift. Finally the companies are connected to
    the sink, with the value of the number of officers needed for that shift. This connection is only if the company needs
    1 or more officers for that shift. These are done to make sure that each company gets the exact number of officers 
    that they need for each shift of each day. The demand of the super sink is then connected to a super sink, with the
    value of the total officers needed for all companies and shifts. The bipartite graph is now fully constructed with all 
    the flows set based on the given constraints and requirements.

    Then, I used the Ford-Fulkerson algorithm that I created to to find the maximum flow from the source to the sink in the 
    flow network. The maximum flow is the maximum number of officers that can be allocated to the companies based on the
    constraints and requirements. The result is then compared to the total officers needed for all companies and shifts.
    If the result is equal to the total officers needed, then the allocation is feasible, or else the function will return
    None immediately, showing that allocation is not possible with the given constraints.

    If the allocation is feasible, the function will then create a 4D list to store the allocation of officers to companies.
    The 4D list will specify which officer is assigned to which company, on which shift, on which day. The allocation is
    done by iterating through the edges from the shifts layer to the companies layer, and checking if the flow is 1, which
    means that the officer is assigned to the company for that shift on that day. The allocation is then stored in the 4D
    list, and the list is returned as the final result.

    Graph Representation:
    https://drive.google.com/file/d/1hS3VYoRm9k-pKsctdW1SN8gkjE84dROz/view?usp=sharing

    Input:
        preferences: A list of lists where preferences[i][k] is 1 if security officer SOi prefers shift Sk.
        officers_per_org: A list of lists where officers_per_org[j][k] specifies how many officers need for 
                          shift Sk each day.
        min_shifts: The minimum number of shifts an officer can be assigned to in 30 days
        max_shifts: The maximum number of shifts an officer can be assigned to in 30 days

    Return:
        allocation: A 4D list that specifies which officer is assigned to which company, on which shift, on
                    which day. If no valid allocation exists, return None.

    Time complexity:
        Complexity: O(M * N * N), where M is the number of companies, and N is the number of security officers.
        Analysis: This complexity is derived from the Ford-Fulkerson algorithm, which has a time complexity of
                  O(V * E^2), when the maximum flow is calculated. In this scenario, the vertices represent security 
                  officers, days, shifts, companies, and the source and sink nodes, resulting in a total of 
                  V = N + M + 2. The number of edges E corresponds to the connections between these vertices. Given the 
                  structure of the bipartite graph, the number of edges is proportional to the number of companies M
                  and the number of security officers N, resulting in E = O(M * N * N). This is because because each company 
                  can potentially be connected to every officer in multiple shifts or days. Therefore, the overall time 
                  complexity for calculating the maximum flow in this context is O(M * N * N), reflecting the product of 
                  the number of companies and the square of the number of security officers. Do note that in this context,
                  the number of days and shifts are constant values, and the number of officers and companies are the
                  primary factors that influence the time complexity, and the dominating factor is the ford fulkerson
                  algorithm.

    Space complexity:
        Complexity: O(N * M), where N is the number of security officers, and M is the number of companies. 
        Analysis: The space complexity is derived from the creation of the graph for the flow network, which requires
                  the allocation of memory for the vertices and edges. The vertices are created for each security officer,
                  day, shift, company, and the source and sink nodes, resulting in a total of N + M + 2 vertices. The
                  edges are created to connect these vertices, with the number of edges being proportional to the number
                  of companies M and the number of security officers N, resulting in O(M * N) edges. Therefore, the overall
                  space complexity for the graph representation is O(N * M), reflecting the product of the number of security
                  officers and companies. Additionally, the space complexity for the allocation list is O(N * M * 30 * 3),
                  which represents the allocation of each security officer to each company, shift, and day. in this context,
                  the number of days and shifts are constant values, and the number of officers and companies are the primary
                  factors that influence the space complexity. The dominating factor is the allocation list, which stores the
                  allocation of each security officer to each company, shift, and day.

    Input space complexity:
        Complexity: O(N + M), where N is the number of security officers, and M is the number of companies.
        Analysis: The input space complexity is derived from the input parameters, which consist of the preferences of
                  security officers and the number of officers needed for each shift by the companies. The preferences
                  of security officers are represented by a list of lists, the inner list has a constant size of 3, while the
                  outer list has a size of N, representing the number of security officers. The number of officers needed
                  for each shift by the companies is represented by a list of lists, the inner list has a constant size of 3,
                  while the outer list has a size of M, representing the number of companies. The minimum and maximum shifts
                  are constant values, and do not contribute to the input space complexity. Therefore, the overall input
                  space complexity is O(N + M), reflecting the sum of the number of security officers and companies.
    """

    ###################### Initialization ######################

    # Initialize fixed values for easier reference
    no_of_officers = len(preferences)                       # number of officers 
    no_of_companies = len(officers_per_org)                 # number of companies
    no_of_shifts = 3                                        # fixed number of shifts per day
    no_of_days = 30                                         # fixed number of days in the month

    # Calculate the total number of nodes needed in the graph for the flow network
    # 4 nodes are added for start, end, super source, and super sink
    # Calculated nodes needed for each layer of the bipartite graph is also calculated
    total_nodes_needed = (1 + 
                          no_of_officers + 
                          (no_of_officers * no_of_days) + 
                          (no_of_officers * (no_of_days * no_of_shifts)) + 
                          ((no_of_companies * (no_of_days * no_of_shifts))) + 
                          1 + 
                          2)

    # Fixed node IDs for source, sink, super source, and super sink, for easier reference
    source_id = 0
    sink_id = total_nodes_needed - 3
    super_source_id = total_nodes_needed - 2
    super_sink_id = total_nodes_needed - 1

    # Time complexity: O(M), where M is the number of companies, shift is a constant value of 3
    # Find the total number of officers needed for all companies and shifts
    total_officers_needed = 0
    for each_company in officers_per_org:
        for each_shift in each_company:
            total_officers_needed += each_shift * 30


    ###################### Early termination checks ######################

    # Early termination: if the minimum shifts is greater than the maximum shifts, return None
    if min_shifts > max_shifts:
        return None
    
    # Time complexity: O(N), where N is the number of security officers, shifts is a constant value of 3
    # Early termination: if an officer's preference cannot even fulfill the minimum shifts, return None
    for i in range(no_of_officers):
        total = 0
        for j in range(no_of_shifts):
            total += preferences[i][j]
        total = total * 30

        if total < min_shifts:
            return None
        
    # Early termination: if the minimum shift capacity of officers cannot meet company demands, return None
    min_shift_all_officers = min_shifts * no_of_officers
    if min_shift_all_officers > total_officers_needed:
        return None
    

    ###################### Graph creation ######################

    # Time complexity: O(NM), where N is the number of officers, M is the number of companies, shift and day are constant values
    # and addtitional constant value of 4 nodes is added for start, end, super source, and super sink
    # Create the graph for the flow network
    graph = Graph(total_nodes_needed)

    # Space complexity: O(NM), where N is the number of officers, M is the number of companies, shift and day are constant values
    # that depends on the number of officers and companies. 
    # Initialize lists to store the indices of the nodes for each layer of the bipartite graph, for easier reference
    indices_for_officers = []
    indices_for_days = []
    indices_for_shifts = []
    indices_for_companies = []

    ###################### Connecting the layers of the bipartite graph ######################
    
    # Layer 1
    # Connection between super source, start, and officers layer

    # Connect source ID to either super source or super sink, depending on the demand
    demand_for_super_source = - total_officers_needed + (min_shifts * no_of_officers)

    # This edge is only needed when the demand is not 0, because the pre-processing should remove all demands
    # If demand is negative, connect super source to source, else connect source to super sink instead
    if demand_for_super_source != 0:
        if demand_for_super_source < 0:
            graph.add_edge(super_source_id, source_id, abs(demand_for_super_source))
        else:
            graph.add_edge(source_id, super_sink_id, abs(demand_for_super_source))

    # Connect super source to officers layer, with value of minimum shifts, if minimum shifts is more than 0
    if min_shifts > 0:

        # Time complexity: O(N), where N is the number of security officers
        # Iterate through the number of officers to add edge from super source to each officer
        for i in range(no_of_officers):
            officer_node = i + 1
            graph.add_edge(super_source_id, officer_node, min_shifts)

    # Previous ID - placeholder for the previous node ID to track the last node added
    previous_id = 0

    # Time complexity: O(N), where N is the number of security officers
    # Connect start to officers layer, with value of maximum minus minimum shifts
    max_min_shifts = max_shifts - min_shifts
    for i in range(no_of_officers):
        officer_node = i + 1
        graph.add_edge(source_id, officer_node, max_min_shifts)
        indices_for_officers.append(officer_node)
        previous_id = officer_node
    
    # Layer 2
    # Connect officers layer to days layer, with value of 1, each officer to 30 days
        
    # Time complexity: O(N), where N is the number of security officers, days is a constant value of 30
    # Iterate through the number of officers and days to add edge from officer to each day
    for i in range(no_of_officers):
        officer_node = i + 1
        for d in range(no_of_days):
            day_node = previous_id + 1
            graph.add_edge(officer_node, day_node, 1)
            indices_for_days.append(day_node)
            previous_id = day_node

    # Layer 3
    # Connect days layer to shifts layer, each day to 3 shifts. The capacity is based on the officer's preference
            
    # Start with index 0 for the day node to get the first day node from the list
    get_day_node_index = 0

    # Time complexity: O(N), where N is the number of officers, days is a constant value of 30, shifts is a constant value of 3
    # Iterate through officers, days, and shifts to create all the edges corresponding to the preferences
    for i in range(no_of_officers):
        for d in range(no_of_days):
            day_node = indices_for_days[get_day_node_index]
            for s in range(no_of_shifts):

                # If officer prefers the shift, add edge with
                if preferences[i][s] == 1:
                    shift_node = previous_id + 1
                    graph.add_edge(day_node, shift_node, 1)
                    indices_for_shifts.append(shift_node)
                    previous_id = shift_node

                # Else, edge is not needed when officer does not prefer shift, but the indexing is still recorded for index conservation
                else:
                    shift_node = previous_id + 1
                    indices_for_shifts.append(shift_node)
                    previous_id = shift_node
            
            # Increment the index for the day node to get the next day node
            get_day_node_index += 1

    # Layer 4
    # Connect days layer to companies layer, each day to 3 shifts. The capacity is based on the company's demand 
    # The company layer is based on the amount of companies, days, and shifts
            
    # Time complexity: O(M), where M is the number of companies, days is a constant value of 30, shifts is a constant value of 3
    # Create the indices for company nodes, for index retrieval in creating the edges
    # Iterate through companies, days, and shifts to get the company node indices
    for i in range(no_of_companies):
        for d in range(no_of_days):
            for s in range(no_of_shifts):
                company_node = previous_id + 1
                indices_for_companies.append(company_node)
                previous_id = company_node

    # Time complexity: O(NM), where N is the number of officers, M is the number of companies, days is a constant value of 30, 
    # shifts is a constant value of 3.
    # Connect the shifts layer to the companies layer, with all the constraints and index calculations
    # Iterate through officers, companies, days, and shifts to create the edges corresponding to the preferences
    for i in range(no_of_officers):
        for j in range(no_of_companies):
            for d in range(no_of_days):
                for s in range(no_of_shifts):

                    # Calculations for the index for the current shift node working with, retrieve the index from the list
                    shift_index = (i * no_of_days * no_of_shifts) + (d * no_of_shifts) + s
                    shift_node = indices_for_shifts[shift_index]

                    # Calculations for the index for the current company node working with, retrieve the index from the list
                    company_index = (j * no_of_days * no_of_shifts) + (d * no_of_shifts) + s
                    company_node = indices_for_companies[company_index]

                    # Only add the edge if there is a demand for this shift at this company, and if the officer prefers this shift
                    if officers_per_org[j][s] > 0:
                        if preferences[i][s] == 1:
                            graph.add_edge(shift_node, company_node, 1)

    # Layer 5
    # Connect companies layer to final node, with value of demand for each company, days, and shifts
    # The connection from the final node to the super sink is also added here
    
    # Start with index 0 for the company node to get the first company node from the list
    get_company_node_index = 0

    # Time complexity: O(M), where M is the number of companies, days is a constant value of 30, shifts is a constant value of 3
    # Iterate through companies, days, and shifts to create all the edges corresponding to the preferences
    for c in range(no_of_companies):
        for d in range(no_of_days):
            for s in range(no_of_shifts):

                # If the company has a demand for the shift, add edge with the value of the preferenced demand
                if officers_per_org[c][s] > 0:
                    company_node = indices_for_companies[get_company_node_index]
                    graph.add_edge(company_node, sink_id, officers_per_org[c][s])
                    previous_id = company_node

                # Increment the index for the company node to get the next company node
                get_company_node_index += 1

    # Adding super sink to graph, connecting from final node to super sink, with maximum demand of how much officers can work
    demand_for_super_sink = no_of_officers * no_of_days
    graph.add_edge(sink_id, super_sink_id, demand_for_super_sink)


    ###################### Checking feasibility of the allocation ######################

    # Time complexity: O(1), initialization takes constant time
    # Create the residual network from the graph
    network = ResidualNetwork(graph)

    # Time complexity: O(M * N * N), where M is the number of companies, N is the number of officers
    # This is derived from the Ford-Fulkerson algorithm, which has a time complexity of O(V * E^2), where each flow can be 
    # represented as the allocation for each officer to each company, day, and shift.
    # Find the maximum flow from the source to the sink using the Ford-Fulkerson algorithm with Breadth First Search
    max_flow = network.max_flow(super_source_id, super_sink_id)

    # Check feasibility of the allocation through the maximum flow, if it does not meet the total officers needed, no valid allocation
    if max_flow != total_officers_needed:
        return None
    

    ###################### Allocation of officers to companies ######################

    # Space complexity: O(NM), where N is the number of officers, M is the number of companies, the day and shift are constant values
    # Initialize the allocation list to store the allocation of officers to companies, days, and shifts, with initial value of 0 for all allocations
    allocation = [[[[0 for _ in range(no_of_shifts)] for _ in range(no_of_days)] for _ in range(no_of_companies)] for _ in range(no_of_officers)]

    # Space complexity: O(NM), where N is the number of officers, M is the number of companies, the day and shift are constant values
    # Iterate through indices for shifts and companies
    for s in range(len(indices_for_shifts)):
        for c in range(len(indices_for_companies)):

            # Retrieve the company and shift indices from the lists based on the iteration index
            company_index = indices_for_companies[c]
            shift_index = indices_for_shifts[s]

            # Get the edge between the shift and company nodes and retrieve the flow
            edge = graph.get_edge(shift_index, company_index)
            if edge != None:

                # If flow is 1, calculate the company, day, shift, and officer indices
                if edge.flow == 1:
                    officer = s // (no_of_days * no_of_shifts)
                    company = c // (no_of_days * no_of_shifts)
                    day = (c % (no_of_days * no_of_shifts)) // no_of_shifts
                    shift = (c % (no_of_days * no_of_shifts)) % no_of_shifts

                    # Allocate the officer to the company, day, and shift based on the index calculated
                    allocation[officer][company][day][shift] = 1

    # Return the allocation when allocation is feasible
    return allocation