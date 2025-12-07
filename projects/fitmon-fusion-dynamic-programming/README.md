# Fitmon Fusion - Dynamic Programming

A Python implementation that calculates the optimal fusion sequence for Fitmon creatures to maximize their cuteness score using dynamic programming and matrix chain multiplication.

## Project Overview

This project solves the Fitmon fusion optimization problem, where multiple Fitmon creatures must be fused together in a specific sequence to achieve the maximum possible cuteness score. Each Fitmon has affinity values that affect fusion outcomes, making the order of fusion critical.

### Goal

Find the fusion sequence that produces the **maximum possible cuteness score**.

## Algorithm Approach

### Matrix Chain Multiplication (Dynamic Programming)

The solution uses a **bottom-up dynamic programming** approach inspired by matrix chain multiplication:

1. **Base Case**: Store initial cuteness scores in a 2D DP table diagonal
2. **Build Up**: Process chains of increasing length
3. **Optimization**: For each subchain, try all possible partition points
4. **Memoization**: Store optimal scores to avoid recalculation

## Usage

### Basic Example

```python
from fitmon_fusion import fuse

# Define Fitmons: [affinity_left, cuteness_score, affinity_right]
fitmons = [
    [0, 10, 5],   # Fitmon 0: left=0, cuteness=10, right=5
    [5, 20, 3],   # Fitmon 1: left=5, cuteness=20, right=3
    [3, 15, 0]    # Fitmon 2: left=3, cuteness=15, right=0
]

# Calculate maximum cuteness score
max_cuteness = fuse(fitmons)
print(f"Maximum cuteness score: {max_cuteness}")
```

### Input Format

```python
fitmons = [
    [affinity_left_0, cuteness_0, affinity_right_0],
    [affinity_left_1, cuteness_1, affinity_right_1],
    # ... more fitmons
]
```

### Output

Returns an integer representing the maximum achievable cuteness score.

## Complexity Analysis

### Time Complexity: O(N³)

Where N is the number of Fitmons:
- **Outer loop**: Iterates over chain lengths (2 to N)
- **Middle loop**: Iterates over starting positions
- **Inner loop**: Iterates over partition points

```
Total iterations ≈ N × N × N = O(N³)
```

### Space Complexity: O(N²)

- **DP Table**: N × N 2D array for memoization
- **Input Space**: O(N) for the fitmons list
- **Auxiliary Space**: O(N²) for the DP table

### Why O(N³) is Acceptable

For typical problem sizes (N < 1000), cubic time complexity is efficient enough. The dynamic programming approach avoids the exponential time complexity of trying all possible fusion orders.

## Testing

```bash
python test_forest_escape.py
```

Test cases should verify:
- Single Fitmon (base case)
- Two Fitmons (simple fusion)
- Multiple Fitmons (complex sequences)
- Edge cases (minimum values, large numbers)