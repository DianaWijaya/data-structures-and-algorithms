# ORF Finder - Trie Data Structure

A Python implementation using Trie (prefix tree) data structures to efficiently find Open Reading Frames (ORFs) in DNA sequences by matching start and end patterns.

## Project Overview

This project solves the ORF (Open Reading Frame) finding problem in genomic sequences. Given a DNA string and start/end sequences, it identifies all valid substrings that begin with the start pattern and end with the end pattern without overlap.

## Algorithm Approach

### Dual Trie Strategy

The solution uses an innovative **two-trie approach**:

#### Forward Trie
- Stores all DNA subsequences starting from each position
- Used to find indices where start sequences end
- Each node stores `end_indices` - positions where sequences terminate

#### Reverse Trie
- Stores reversed DNA subsequences
- Used to find indices where end sequences begin (in reverse)
- Enables efficient backward pattern matching

#### Search and Construction
1. Search for start pattern in forward trie → get ending indices
2. Search for end pattern in reverse trie → get starting indices (reversed)
3. Check for overlaps between start and end indices
4. Construct valid ORFs by iterating between non-overlapping indices

## Usage

### Basic Example

```python
from orf_finder import OrfFinder

# DNA sequence (only characters A, B, C, D allowed)
dna = "AABCDABCDABCD"

# Create ORF finder
finder = OrfFinder(dna)

# Find ORFs with specific start and end patterns
start_pattern = "AA"
end_pattern = "CD"

# Get all valid ORFs
orfs = finder.find(start_pattern, end_pattern)

for orf in orfs:
    print(orf)
# Output: ["AABCD", "AABCDABCD", "AABCDABCDABCD"]
```

### Input Format

**DNA Sequence**: String containing only characters A, B, C, D
```python
dna = "AABCDABCD"
```

**Start/End Patterns**: Strings containing only characters A, B, C, D
```python
start = "AA"
end = "CD"
```

### Output Format

Returns a list of strings:
```python
["AABCD", "AABCDABCD"]  # Valid ORFs
[]                       # No valid ORFs found
```

## Complexity Analysis

### OrfFinder Initialization

**Time Complexity**: O(n²)
- n: Length of DNA sequence
- For each position i (n iterations)
  - Insert substring from i to end (O(n))
- Total: O(n²) for building both tries

**Space Complexity**: O(n²)
- Each node stores position indices
- Total nodes across all insertions: O(n²)

### Find Function

**Time Complexity**: O(T + U + V)
- T: Length of start sequence (forward trie search)
- U: Length of end sequence (reverse trie search)
- V: Number of characters in all output ORFs
- Best case: O(1) when patterns don't exist
- Worst case: O(n²) when many ORFs span entire sequence

**Space Complexity**: O(V)
- V: Total characters in all output ORFs
- Result list stores all found ORFs
- Temporary substring construction not counted (immediately converted)

## Testing

```bash
python test_orf_finder_1.py
python test_orf_finder_2.py
python test_orf_finder_3.py
```

Test cases should verify:
- Simple start-end patterns
- Multiple occurrences of patterns
- Overlapping patterns (should be excluded)
- Non-existent patterns
- Edge cases (empty sequences, single character)