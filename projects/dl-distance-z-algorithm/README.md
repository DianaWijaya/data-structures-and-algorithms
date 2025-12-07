# Near-Exact Pattern Matching - Z-Algorithm

A Python implementation using the Z-algorithm to find exact and near-exact pattern matches in text with Levenshtein distance of 1 (one edit operation).

## Project Overview

This project finds all occurrences of a pattern in text that match either exactly or with exactly one edit operation (insert, delete, replace, or swap). It uses the Z-algorithm for efficient string matching in linear time.

## Algorithm Approach

### Z-Algorithm Foundation

The **Z-algorithm** computes the Z-array where `z[i]` represents the length of the longest substring starting from `s[i]` that matches the prefix of `s`.

**Time Complexity**: O(n) - Linear time string matching

### Near-Exact Matching Strategy

The solution uses **bidirectional Z-arrays**:

#### Forward Z-Array
- Concatenate: `pattern + $ + text`
- Compute Z-values starting from each position
- Identifies prefix matches from left to right

#### Reverse Z-Array
- Concatenate: `reverse(pattern) + $ + reverse(text)`
- Compute Z-values in reversed strings
- Identifies suffix matches from right to left

#### Match Detection

By combining forward and reverse Z-values at each position, we can detect:

1. **Exact Match** (Distance = 0)
   - `z_forward[i] == pattern_length`
   - Full pattern match at position i

2. **Insert** (Distance = 1)
   - `z_forward[i] + z_reverse[i + pattern_length - 2] >= pattern_length - 1`
   - One character inserted in text

3. **Delete** (Distance = 1)
   - `z_forward[i] + z_reverse[i + pattern_length] >= pattern_length`
   - One character deleted from text

4. **Replace** (Distance = 1)
   - `z_forward[i] + z_reverse[i + pattern_length - 1] == pattern_length - 1`
   - One character replaced in text

5. **Swap** (Distance = 1)
   - `z_forward[i] + z_reverse[i + pattern_length - 1] == pattern_length - 2`
   - Two adjacent characters swapped
   - Requires explicit character check

### Why This Works

By using bidirectional Z-arrays:
- **O(m + n) time** instead of O(m × n) dynamic programming
- **No backtracking** needed for edit distance
- **Single pass** through concatenated strings
- **Efficient detection** of all edit operation types

## Usage

### Command Line

```bash
python pattern_matching.py test_text.txt test_pattern.txt
```

### Input Format

**text.txt**: Single line containing the text to search
```
ABCDEFGHIJKLMNOP
```

**pattern.txt**: Single line containing the pattern to find
```
ABC
```

### Output Format

**output_a1q1.txt**: Each line contains position and match type
```
1 0
5 1
12 1
```

Where:
- First column: 1-indexed position in text
- Second column: 0 = exact match, 1 = near-exact match

## Complexity Analysis

### Z-Algorithm

**Time Complexity**: O(n)
- Each character examined at most twice
- Left and right pointers move monotonically
- Amortized constant time per position

**Space Complexity**: O(n)
- Z-array storage: O(n)

### Near-Exact Pattern Matching

**Time Complexity**: O(m + n)
- m: Length of pattern
- n: Length of text
- Forward Z-array: O(m + n)
- Reverse Z-array: O(m + n)
- Match detection: O(n)
- Total: 2 × O(m + n) + O(n) = O(m + n)

**Space Complexity**: O(m + n)
- Concatenated strings: O(m + n)
- Z-arrays: O(m + n)
- Results list: O(k) where k is number of matches

## Testing

### Run test files

```bash
python test_DL_distance_1000_cases.py
python test_DL_distance_5000_cases.py
python test_edge_DL_distance_cases.py
```

### Test Cases to Verify

- Exact matches only
- Insert operations
- Delete operations
- Replace operations
- Swap operations
- Pattern longer than text
- Empty pattern/text
- No matches found
