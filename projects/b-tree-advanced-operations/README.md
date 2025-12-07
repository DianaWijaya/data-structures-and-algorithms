# B-Tree with Range Queries - Advanced Operations

A Python implementation of B-trees with augmented nodes for efficient order statistics (select, rank) and range queries (keysInRange, primesInRange). Includes Miller-Rabin primality testing for prime number filtering.

## Project Overview

This project implements a fully functional B-tree with minimum degree `t` that supports insertion, deletion, and advanced query operations. Each node is augmented with subtree sizes, minimum keys, and maximum keys to enable O(log n) order statistics and efficient range queries with subtree pruning.

## Algorithm Approach

### B-Tree Properties

A B-tree of minimum degree `t` satisfies:
1. Every node has at most `2t - 1` keys
2. Every non-root node has at least `t - 1` keys
3. All leaves are at the same depth
4. Internal nodes with k keys have k+1 children

### Augmented Node Structure

Each node stores:
- **Keys**: Sorted array of values
- **Children**: Pointers to child nodes
- **Subtree Sizes**: Number of keys in each child subtree
- **Min Keys**: Minimum key in each child subtree
- **Max Keys**: Maximum key in each child subtree

### Core Operations

#### Insert (O(log n))
1. Search for insertion position
2. Split nodes when full (2t - 1 keys)
3. Propagate splits upward
4. Update subtree sizes

#### Delete (O(log n))
Three main cases:
- **Case 1**: Key in leaf → remove directly
- **Case 2**: Key in internal node:
  - 2a: Replace with predecessor if left child has ≥ t keys
  - 2b: Replace with successor if right child has ≥ t keys
  - 2c: Merge children if both have t-1 keys
- **Case 3**: Key not in current node:
  - Ensure child has ≥ t keys
  - Borrow from sibling or merge

#### Select (O(log n))
Find k-th smallest key:
1. Navigate using subtree sizes
2. Compare k with left subtree size
3. Recurse left, return current, or recurse right

#### Rank (O(log n))
Find position of key x:
1. Count keys less than x while searching
2. Add subtree sizes for skipped children
3. Return accumulated count

#### keysInRange (O(log n + k))
Find all keys in [x, y]:
1. Use min_key and max_key to prune subtrees
2. Skip subtrees entirely outside range
3. Collect keys within range

#### primesInRange (O(log n + k × p))
Find prime keys in [x, y]:
1. Get all keys in range
2. Test each with Miller-Rabin (p iterations)
3. Return prime keys only

## Usage

### Command Line

```bash
python btree.py <t> <keystoinsert.txt> <keystodelete.txt> <commands.txt>
```

Where:
- `t`: Minimum degree (integer ≥ 2)
- `keystoinsert.txt`: Keys to insert (one per line)
- `keystodelete.txt`: Keys to delete (one per line)
- `commands.txt`: Query commands (one per line)

### Input Format

**keystoinsert.txt**:
```
12739121
58219403
45620117
10018273
34567890
98765432
123456789
10000019
999983
50000000
43219876
87654321
100000007
9999999967
76543210
314159265
271828183
99999959
88888888
1234567890
```

**keystodelete.txt**:
```
99999959
88888888
1234567
98765432
50000000
58219403
```

**commands.txt**:
```
primesInRange 1 100
keysInRange 50000000 100000000
select 7
select 16
rank 1234567890
primesInRange 1 12345678
keysInRange 1 10
rank 42
```

### Output Format

**output_a3.txt**: Each line contains the result of one command
```
-1
76543210 87654321
45620117
-1
14
999983 10000019 10018273
-1
-1
```

## Testing

### Run Test Cases

```bash
python test_btree_delete.py
python test_btree_insert.py
python test_btree_keysInRange.py
python test_btree_primesInRange.py
python test_btree_rank.py
python test_btree_select.py
python test_btree_more.py
python test_primes.py
```
