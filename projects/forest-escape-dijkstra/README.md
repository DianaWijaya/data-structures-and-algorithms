# Forest Escape - Dijkstra

A Python implementation of shortest path algorithms using Dijkstra's algorithm to find optimal escape routes through a magical forest with teleporting trees (Solulu trees) and destruction mechanics.

## Project Overview

This project solves the Delulu Forest escape problem, where you must navigate through a forest represented as a weighted directed graph, destroy special Solulu trees that teleport you to different locations, and find the shortest path to safety.

## Algorithm Approach

### Bidirectional Dijkstra with Graph Reversal

The solution uses an innovative **two-phase approach**:

#### Phase 1: Forward Dijkstra
1. Run Dijkstra from the starting tree
2. Calculate distance to each Solulu tree
3. Add destruction time to get total time at Solulu trees

#### Phase 2: Reverse Dijkstra
1. **Reverse all edges** in the graph (u,v) → (v,u)
2. Create a **virtual exit node** connecting all real exits
3. Run Dijkstra from the virtual exit (backwards through the graph)
4. Calculate distance from teleport destinations back to exits

#### Phase 3: Combination
- Combine forward distances to Solulu trees with reverse distances from teleport destinations
- Find minimum total distance across all Solulu trees
- Backtrack to reconstruct the complete path

## Usage

### Basic Example

```python
from forest_escape import TreeMap

# Define roads: (from_tree, to_tree, time)
roads = [
    (0, 1, 10),   # Road from tree 0 to tree 1, takes 10 time
    (1, 2, 5),    # Road from tree 1 to tree 2, takes 5 time
    (2, 3, 8),    # Road from tree 2 to tree 3, takes 8 time
    (1, 3, 20)    # Alternative road from tree 1 to tree 3
]

# Define Solulu trees: (tree_id, destroy_time, teleport_to)
solulus = [
    (1, 3, 3)     # Tree 1: takes 3 time to destroy, teleports to tree 3
]

# Create the forest map
forest = TreeMap(roads, solulus)

# Find escape route
start = 0
exits = [3]  # Tree 3 is an exit
result = forest.escape(start, exits)

if result:
    min_time, path = result
    print(f"Minimum escape time: {min_time}")
    print(f"Escape path: {' -> '.join(map(str, path))}")
else:
    print("No escape route exists!")
```

### Input Format

**Roads**: List of tuples `(u, v, w)`
```python
roads = [
    (from_tree, to_tree, travel_time),
    # ... more roads
]
```

**Solulus**: List of tuples `(x, y, z)`
```python
solulus = [
    (tree_id, destroy_time, teleport_destination),
    # ... more Solulu trees
]
```

### Output Format

Returns a tuple or None:
```python
(min_time, path)  # Success
None              # No valid escape route
```

Where:
- `min_time`: Integer representing minimum escape time
- `path`: List of tree IDs showing the complete route

## Complexity Analysis

### TreeMap Initialization

**Time Complexity**: O(|T| + |R|)
- T: Number of trees (vertices)
- R: Number of roads (edges)
- Finding max vertex: O(R)
- Creating vertices: O(T)
- Adding edges: O(R)

**Space Complexity**: O(|T| + |R|)
- Vertex storage: O(T)
- Edge storage: O(R)

### Escape Function

**Time Complexity**: O(|R| log |T|)
- Forward Dijkstra: O(R log T)
- Graph reversal: O(R)
- Reverse Dijkstra: O(R log T)
- Path reconstruction: O(T)
- **Dominated by**: 2 × O(R log T) = O(R log T)

**Space Complexity**: O(|T| + |R|)
- Distance arrays: O(T)
- Predecessor arrays: O(T)
- Reversed graph: O(R)
- Min heap: O(R) maximum size

### Dijkstra's Algorithm

**Time Complexity**: O(|E| log |V|)
- Each edge processed once: O(E)
- Heap operations: O(log V)
- Total: O(E log V)

**Space Complexity**: O(|V| + |E|)
- Distance array: O(V)
- Predecessor array: O(V)
- Min heap: O(E) worst case



## Testing

```bash
python test_forest_escape.py
```

Test cases should verify:
- Simple paths without Solulu trees
- Paths requiring Solulu tree destruction
- Multiple exit points
- No valid path scenarios
- Complex graphs with multiple Solulu trees