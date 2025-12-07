import math
from typing import TypeVar, Generic
from ctypes import py_object

class Edge:
    def __init__(self, u, v, w):
        """
        Function description:
        Initialises an edge with the starting vertex, ending vertex, and weight of the edge.

        Input:
            u: The starting vertex
            v: The ending vertex
            w: The weight of the edge from u to v

        Return:
            None

        Time complexity: 
            Complexity: O(1)
            Analysis: The time complexity is constant as it only initialises the values of the edge.

        Space complexity: 
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the values of the edge.

        Input space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the values of the edge.
        """
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        """
        Function description:
        Returns the string representation of the edge in a readable format, for testing purposes.

        Input:
            None

        Return:
            str_rep: The string representation of the edge in the format (u,v,w)

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant as it only concatenates the values of the edge.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the string representation 
                      of the edge.

        Input space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the string representation 
                      of the edge.
        """
        str_rep = "(" + str(self.u) + "," + str(self.v) + "," + str(self.w) + ")"
        return str_rep
    

# This code is based on the lecture video from FIT2004, Lecture04 P1 Graph BFS DFS Lecture05 P1 Dijkstra
# Link: https://www.youtube.com/watch?v=8S2jKSNC0BQ
class Vertex:
    def __init__(self, id):
        """
        Function description:
        Initialises a vertex with the vertex ID and an empty list of edges.

        Input:
            id: The ID of the vertex

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant as it only initialises the values of the vertex.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the values of the vertex.

        Input space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the values of the vertex.
        """
        self.id = id
        self.edges = []

    def add_edge(self, edge):
        """
        Function description:
        Adds an edge to the list of edges of the vertex.

        Input:
            edge: The edge to be added to the list of edges of the vertex

        Return:
            None

        Time complexity:
            Complexity: O(1)
            Analysis: The time complexity is constant as it only appends the edge to the list of edges.

        Space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the edge in the list of edges.

        Input space complexity:
            Complexity: O(1)
            Analysis: The space complexity is constant as it only stores the edge in the list of edges.
        """
        self.edges.append(edge)

    def __str__(self):
        """
        Function description:
        Returns the string representation of the vertex in a readable format, for testing purposes.

        Input:
            None

        Return:
            str_rep: The string representation of the vertex in the format ID: id, Edges: [edges]

        Time complexity:
            Complexity: O(E), where E is the number of edges in the list of edges of the vertex
            Analysis: E is the number of edges in the list of edges of the vertex. This iterates over
                      the edges to concatenate the string representation of each edge.

        Space complexity:
            Complexity: O(N), where N is the number of edges in the list of edges of the vertex
            Analysis: N is the number of edges in the list of edges of the vertex. This stores the
                      string representation of each edge in the list of edges.

        Input space complexity:
            Complexity: O(N), where N is the number of edges in the list of edges of the vertex
            Analysis: N is the number of edges in the list of edges of the vertex. This stores the
                      string representation of each edge in the list of edges.
        """
        edge_str = ', '.join(str(edge) for edge in self.edges)
        str_rep = f"ID: {self.id}, Edges: [{edge_str}]"
        return str_rep


# This code is based on the given data structure, ArrayR, from FIT1008, assignment 3.
# Link: https://github.com/DianaWijaya/A3_PAIN.git
# The github repository to my assignment is private, because github link to the assignment 
# can no longer be found. Please let me know if you would like to access the repository.
T = TypeVar('T')
class ArrayR(Generic[T]):
    def __init__(self, length: int) -> None:
        """ Creates an array of references to objects of the given length
        :complexity: O(length) for best/worst case to initialise to None
        :pre: length > 0
        """
        if length <= 0:
            raise ValueError("Array length should be larger than 0.")
        self.array = (length * py_object)() # initialises the space
        self.array[:] =  [None for _ in range(length)]

    def __len__(self) -> int:
        """ Returns the length of the array
        :complexity: O(1)
        """
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """ Returns the object in position index.
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the object in position index to value
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        self.array[index] = value


# This code is based on the given data structure, max heap from FIT1008, assignment 3.
# However, the code was modified into a min heap, instead of a max heap.
# Link: https://github.com/DianaWijaya/A3_PAIN.git
# The github repository to my assignment is private, because github link to the assignment 
# can no longer be found. Do let me know if you would like to access the repository.
class MinHeap(Generic[T]) :
    MIN_CAPACITY = 1

    def __init__(self, max_size: int, an_array: ArrayR[T] = None) -> None:
        """
        If an_array is specified then the elements of the future 
        heap are known in advance.
        Assume that max_size=len(an_array) if given.

        O(1): initialization
        """
        if an_array is None:
            self.length = 0 
        else:
            self.length = max_size = len(an_array) 
        
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self) -> int:
        """
        O(1): calculates the length of the ArrayR
        """
        return self.length

    def is_full(self) -> bool:
        """
        O(1): calculates the length added by 1 and compared to the length of the ArrayR
        """
        return self.length + 1 == len(self.the_array)
    
    def is_empty(self) -> bool:
        """
        O(1): checks if the heap is empty, by comparing the length to 0
        """
        return self.length == 0

    def rise(self, k: int) -> None:
        """
        This function was modified to rise the element at index k to its correct position using 
        the min heap property, where the parent is smaller than the children.
        
        Rise element at index k to its correct position
        :pre: 1 <= k <= self.length

        BCS: O(1): when element k is at the correct position, no swaps are done
        WCS: O(log n): where n is the number of elements in the heap, occurs when the element at 
             index k is swapped
        """
        item = self.the_array[k]
        while k > 1 and item < self.the_array[k // 2]:  # Changed from '>' to '<'
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, element: T) -> bool:
        """
        Swaps elements while rising

        BCS: O(1), when the element is added to the end of the heap, and no swap is needed in rise
        WCS: O(log n), where n is the number of elements in the heap, occurs when the element at
             index k is swapped, due to the wrong position of the element
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        self.rise(self.length)

    def smallest_child(self, k: int) -> int:
        """
        This function was modified from largest_child to smallest_child, to return the index of the
        child with the smallest value instead of the largest value.

        Returns the index of k's child with smallest value.
        :pre: 1 <= k <= self.length // 2

        O(1): compares the two children of k and returns the index of the smallest child
        """
        
        if 2 * k == self.length or \
                self.the_array[2 * k] < self.the_array[2 * k + 1]:  # Change from '>' to '<'
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ 
        This function was modified so that the element at index k is sunk to the correct position 
        using the min heap property, where the parent is smaller than the children.

        Make the element at index k sink to the correct position.
        :pre: 1 <= k <= self.length

        BCS: O(1), when the element at index k is at the correct position, no swaps are done
        WCS: O(log n), where n is the number of elements in the heap, occurs when the element at
             index k is swapped, due to the wrong position of the element
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k) 
            if self.the_array[min_child] >= item:  # Change from '<=' to '>='
                break
            self.the_array[k] = self.the_array[min_child]
            k = min_child

        self.the_array[k] = item
        
    def get_min(self):
        """ 
        This function was modified to return the minimum element in the heap, instead of the maximum 
        element.

        Remove (and return) the minimum element from the heap. 

        BCS: O(1), when the element at index 1 is the minimum element, and no swaps are done in sink
        WCS: O(log n), where n is the number of elements in the heap, occurs when the element at index 
             1 needs to sink down to maintain the heap property.
        """
        if self.length == 0:
            raise IndexError

        min_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return min_elt

class TreeMap:
    def __init__(self, roads, solulus):
        """
        Function description:
        This function initialises the TreeMap object with the roads and solulus. The roads are
        represented as a list of tuples (u, v, w), and the solulus are represented as a list of
        tuples (x, y, z). The vertices are initialised with the vertex ID, and the edges are added
        to the vertices. The solulus values are added to their respective vertices. 

        Precondition:
            - The roads and solulus are valid lists of tuples
        Postcondition:
            - None

        Input:
            roads: The roads represented as a list of tuples (u, v, w), where u is the starting 
                   vertex, v is the ending vertex, and w is the weight of the edge.
            solulus: The solulus represented as a list of tuples (x, y, z), where x is the vertex 
                     ID, y is the time taken to destroy the tree, and z is the teleported vertex.

        Return:
            None

        Time complexity:
            Complexity: O(|T| + |R|), where T is the number of trees and R is the number of roads.
            Analysis: The time complexity T is from the initialisation of the vertices with the 
                    vertex ID, and R is from the addition of the edges to the vertices, and the 
                    operation of finding the index of the last vertex. The time complexity of 
                    O(S) can be ignored because the number of solulus is always less than the 
                    number of roads.

        Space complexity:
            Complexity: O(|T| + |R|), where T is the number of trees and R is the number of roads.
            Analysis: The space complexity T is from the initialisation of the vertices with the
                    vertex ID, and R is from the addition of the edges to the vertices. The space
                    complexity of O(S) for the solulus can be ignored because the number of solulus 
                    is always less than the number of roads.

        Input space complexity:
            Complexity: O(|R| + |S|), where R is the number of roads and S is the number of solulus.
            Analysis: The space complexity R is from the roads, and S is from the solulus. The input
                      space complexity of O(T) can be ignored because the number of trees is always
                      less than the number of roads.
        """
        
        # Space complexity: O(R), where R is the number of roads
        # Initialise the roads and solulus
        self.roads = roads
        self.solulus = solulus

        # Time complexity: O(R), where R is the number of roads
        # Find the index of the last vertex
        max_vertex = 0
        for each_edge in self.roads:
            if each_edge[0] > max_vertex:
                max_vertex = each_edge[0]
            if each_edge[1] > max_vertex:
                max_vertex = each_edge[1]

        # Space complexity: O(T), where T is the number of trees 
        self.vertices = [0] * (max_vertex+1)

        # Time complexity: O(T), where T is the number of trees
        # Initialise the vertices with the vertex ID
        for i in range(max_vertex+1):
            self.vertices[i] = Vertex(i)

        # Time complexity: O(S), where S is the number of solulus
        # Add the solulu's values to their respective vertices
        for x, y, z in self.solulus:
            self.vertices[x].destroy_time = y
            self.vertices[x].teleport_tree = z
            
        # Time complexity: O(R), where R is the number of roads
        # Add the edges to the vertices
        for u, v, w in roads:
            edge = Edge(u, v, w)
            self.vertices[u].add_edge(edge)

    def escape(self, start, exits):
        """
        Function description:
        This function is used to find the minimum distance to escape the Delulu forest, and the
        entire path from the starting tree to the exit point with the minimum distance. In the traversal,
        there are solulu trees that must be destroyed, and teleported to another vertex, in order to
        escape the forest.

        Approach description (if main function):
        The function uses Dijkstra's algorithm created to find the minimum distance to each destination.
        Backtracking was also used to find the path from the starting tree to the exit point with the
        minimum distance. 
        
        I used the reverse method to calculate the minimum distance from the start to the exit. For the
        first operation, I used Dijkstra's algorithm to find the minimum distance to all the trees in the
        forest. However, I only calculated and updated the distance to the solulu trees. The calculation
        done here includes adding the time taken to reach the solulu tree and the time taken to destroy
        the tree. 

        For the second operation, I reversed the graph by reversing the edges. Followed by that, I created
        a new temporary vertex, acting as the singular exit point that connects all the exit points. This
        temporary vertex has a weight of 1, so that it would not affect the minimum distance. I then
        added the edges from the exit points to the temporary exit point. Now, this temporary exit point acts
        as the starting vertex in the reversed graph. Next, I created a new TreeMap object with the reversed
        graph. Then, I used Dijkstra's algorithm to find the minimum distance for the reversed graph. From 
        this operation, the teleported solulu tree was the exit points, and the total distance from the temporary
        exit point to the teleported solulu tree was calculated, and added to the distance to the solulu tree
        consecutively. This way, the total distance from the starting tree, up to the solulu tree, continuing
        to the teleported tree, and finally to the exit point was calculated.

        I calculated the minimum distance and the index to the exit points through the distances list that now
        stores the total distance to each vertex. 
        
        Lastly, backtracking was done in order to find the path from the starting tree to the exit point with
        the minimum distance. The normal path was found by backtracking the forward path. This uses the 
        predecessor list from the Dijsktra's algorithm. The reversed path was found by backtracking the reversed
        path. This uses the reversed predecessor list from the Dijsktra's algorithm. The final path was found by
        combining the normal path and the reversed path. The minimum distance and the final path were then returned.

        Through all these, the minimum distance to escape the Delulu forest, and the entire path from the starting
        tree to the exit point with the minimum distance was calculated, and returned.

        Precondition:
            - There exist a starting vertex, and is a valid tree vertex in the forest
            - There exist exit vertex and they are valid exit points in the forest
        Postcondition:
            - If there is no path to the exit point, return None

        Input:
            start: The starting tree vertex in the forest
            exits: The list of exit points in the forest

        Return:
            min_distance: The minimum distance to the exit the forest
            final_path: The entire path from the starting tree to the exit point with the minimum 
                        distance

        Time complexity:
            Complexity: O(|R| log |T|), where R is the number of roads, and T is the number of trees
                        in the forest.
            Analysis: The time complexity is O(R log T) because the dijkstra's algorithm is used to
                      find the minimum distance to all the trees in the forest. 

        Space complexity:
            Complexity: O(|T| + |R|), where T is the number of trees and R is the number of roads in
                        the forest.
            Analysis: The space complexity is O(T + R) because the distances to each vertex are stored
                      and the predecessor of each destination vertex is stored in lists, from the
                      dijkstra's algorithm used.

        Input space complexity:
            Complexity: O(E), where E is the number of exits in the graph
            Analysis: The space complexity is O(E) because the exit points are stored in a list. The 
                      start is not stored because it is a single vertex.
        """

        # Get the roads and solulus from the TreeMap object
        roads = self.roads
        solulus = self.solulus

        # Create a list to store the distances to each vertex
        # Space complexity: O(T), where T is the number of trees
        distances = [math.inf] * len(self.vertices) 

        # Operation 1 - Find the minimum distance to all the solulu trees in the forest

        # Time complexity: O(R log T), where R is the number of roads, and T is the number of trees in the forest
        # Space complexity: O(T + R), where T is the number of trees and R is the number of roads in the forest
        # Perform dijkstra's algorithm to find the minimum distance to all the trees in the forest
        dijkstra_distance, predecessor = dijkstra(self, start)  

        # Time complexity: O(S), where S is the number of solulus
        # Add the time taken to reach the each solulu tree and time taken to destroy the tree
        for each_solulu in solulus:
            distances[each_solulu[0]] = dijkstra_distance[each_solulu[0]] + each_solulu[1]

        # Operation 2 - Reverse the graph and find minimum distance from exit to each teleported tree
            
        # Time complexity: O(R), where R is the number of roads in the graph
        # Reverse the graph by reversing the edges (switch u and v)
        reversed_graph = []
        for each_road in roads:
            reversed_graph.append((each_road[1], each_road[0], each_road[2]))

        # Create a temporary exit used to link all the exit points to a single exit point
        # This is then used as the starting vertex in the reversed graph
        temp_exit = len(self.vertices) 

        # Time complexity: O(E), where E is the number of exits in the graph
        # Add the edges from the exit points to the temporary exit point
        for each_exit in exits:
            reversed_graph.append((temp_exit, each_exit, 0))

        # Time complexity: O(|T| + |R|), where T is the number of trees and R is the number of roads
        # Space complexity: O(|T| + |R|), where T is the number of trees and R is the number of roads
        # Creating the reversed tree map
        reversed_tree_map = TreeMap(reversed_graph, solulus)

        # Time complexity: O(R log T), where R is the number of roads, and T is the number of trees in the forest
        # Space complexity: O(T + R), where T is the number of trees and R is the number of roads in the forest
        # Perform dijkstra's algorithm to find the minimum distance for the reversed graph
        reversed_dijkstra_distance, reversed_predecessor = dijkstra(reversed_tree_map, temp_exit)

        # Time complexity: O(S), where S is the number of solulus
        # Add the distance to the temporary exit point to the distance to the teleported tree
        for each_solulu in solulus:
            distances[each_solulu[0]] += reversed_dijkstra_distance[each_solulu[2]]

        # This is used to calculate minimum distance and path to the exit points
        min_distance = math.inf
        min_distance_index = -1

        # Time complexity: O(T), where T is the number of trees in the forest
        # Find the minimum distance to the exit points
        for each_distance in range(len(distances)) :
            current = distances[each_distance]
            if current < min_distance:
                min_distance = current
                min_distance_index = each_distance

        # If the minimum distance is infinity, return None (no such route exists)
        if min_distance_index == -1:
            return None

        # Backtrack to find the path from the start to the exit point with the minimum distance

        # Backtracking the forward path
        # If the start is not the minimum distance index, backtrack to find the path
        if start != min_distance_index:
            normal_path = [min_distance_index]
            current = predecessor[min_distance_index]

            # Time complexity: O(P), where P is the number of vertices traversed in the path
            while current != start:
                normal_path.append(current)
                current = predecessor[current]

            # Add the starting vertex to the path
            normal_path.append(start)

        # If the start is the minimum distance index, the path is the start
        else:
            normal_path = [min_distance_index]

        # Time complexity: O(P), where P is the number of vertices traversed in the path
        # Reverse the path so that it is from the start to the solulu tree
        normal_path.reverse()

        # Time complexity: O(S), where S is the number of solulus
        # Find the teleported solulu tree and the vertex it was teleported from
        for each_solulu in solulus:
            if each_solulu[0] == min_distance_index:
                teleported_solulu = each_solulu[2]
                from_solulu = each_solulu[0]
                break

        # Backtracking the reversed path
        reversed_path = []
        
        # Set the current vertex to the teleported solulu tree
        current = reversed_predecessor[teleported_solulu]

        # If the teleported solulu tree is not the vertex it was teleported from, append to
        # the reversed path. If it is, appending will result in two of the same vertex in the path.
        if teleported_solulu != from_solulu:
            reversed_path.append(teleported_solulu)

        # Time complexity: O(P), where P is the number of vertices traversed in the path
        # Backtrack to find the path from the teleported solulu tree to the temporary exit point
        while current != temp_exit:
            reversed_path.append(current)
            current = reversed_predecessor[current]

        # Combine the normal path and the reversed path to get the overall traversed path
        final_path = normal_path + reversed_path

        # Return the minimum distance and the final path
        return (min_distance, final_path)
        
def dijkstra(graph: TreeMap, start: int):
    """
    Function description:
    This dijkstra function is used to find the minimum distance to each destination vertex 
    from the starting vertex, and the predecessor of each destination vertex. 

    Approach description (if main function):
    The function uses Dijkstra's algorithm to find the minimum distance to each destination
    vertex from the starting vertex, and the predecessor of each destination vertex.

    Firstly, the function initialises a list for the minimum distance and predecessor of each
    destination vertex. The length of these lists are set to the number of vertices in the 
    graph. Then, the starting vertex distance is set to 0, because the starting point is always 
    0. Following this, a min heap is created and the starting vertex is added to the minimum
    heap created previously. The starting vertex is added with a distance of 0, into the heap.

    Afterwards, the function iterates until the heap is empty. During each iteration, it 
    retrieves the vertex with the smallest distance from the heap. If the vertex has already been 
    processed, it will be ignored and not processed, as its key will be greater than the current 
    minimum distance. The function then examines all the edges of the current vertex. If the 
    new distance calculated is smaller than the current stored distance, it updates the minimum 
    distance and predecessor of the destination vertex. Subsequently, the minimum distance and 
    predecessor of the destination vertex are added to the heap. This process repeats for all 
    edges of the current vertex, ensuring that the minimum distance and predecessor are updated if 
    necessary, and then adding them to the heap. 
    
    This results in the minimum distance and predecessor of each destination vertex being calculated
    and stored in lists and, are returned by the function.

    Precondition:
        - The graph is a valid TreeMap object
        - The start is a valid starting vertex in the graph
    Postcondition:
        - Returns the minimum distance and predecessor of each destination vertex
        - If there is no path to the destination vertex, the distance is infinity

    Input:
        graph: The graph represented as a TreeMap
        start: The starting vertex

    Return:
        min_distance: The minimum distance to each destination vertex as a list
        predecessor: The predecessor of each destination vertex as a list

    Time complexity:
        Complexity: O(E log V), where E is the number of edges in the graph, and V is the 
                    number of vertices
        Analysis: This is because each edge is iterated over once, and adding the vertex to
                  the heap takes log V time.

    Space complexity:
        Complexity: O(V + E), where T is the set of vertices and E is the set of edges in 
                    the graph
        Analysis: This is because the minimum distance and predecessor of each destination
                  vertex are stored in lists, with auxiliary space complexity of O(V), and 
                  the heap stores the minimum distance and destination vertex with auxiliary 
                  space complexity of O(E).

    Input space complexity:
        Complexity: O(R), where R is the number of roads in the graph
        Analysis: The space complexity is O(R) because the graph is stored in the TreeMap object.
                  The initialisation of the start is not stored because it is a single vertex.
    """

    # Auxiliary space complexity: O(V), where V is the number of vertices in the graph
    # Create a list for the minimum distance and predecessor of each destination vertex
    min_distance = [math.inf] * len(graph.vertices)
    predecessor = [0] * len(graph.vertices)

    # Set the starting vertex distance to 0, because the starting point is always 0
    min_distance[start] = 0

    # Auxiliary space complexity: O(E), where E is the number of edges in the graph
    # Create a min heap and add the starting vertex
    heap = MinHeap(len(graph.roads))
    heap.add((0, start))

    # Time complexity: O(E log V), where E is the number of edges in the graph, and V 
    # is the number of vertices. This is because each edge is iterated over once, and
    # adding the vertex to the heap takes log V time.
    # This loops through until the heap is empty
    while not heap.is_empty():

        # Get the vertex with the smallest distance
        id, vertex = heap.get_min()

        # If the vertex is already processed, it is popped from the queue. So, they key
        # will be greater than the current minimum distance, thus we can ignore it.
        # Do not process an out-of-date entry
        if min_distance[vertex] == id :

            # Time complexity: O(E), where E is the number of edges in the graph
            # This loops through all the edges of the current vertex
            for edge in graph.vertices[vertex].edges:

                # Update the minimum distance and predecessor of the destination vertex if the 
                # new distance is smaller than the current distance stored.
                if min_distance[edge.v] > min_distance[edge.u] + edge.w:

                    # Update the minimum distance and predecessor of the destination vertex
                    min_distance[edge.v] = min_distance[edge.u] + edge.w
                    predecessor[edge.v] = edge.u

                    # Time complexity: O(log V), where V is the number of vertices in the graph
                    # Add the minimum distance and destination vertex to the heap 
                    heap.add((min_distance[edge.v], edge.v))

    # Return the minimum distance and predecessor of each destination vertex in lists
    return min_distance, predecessor