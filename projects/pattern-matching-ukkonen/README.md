# Suffix Tree Pattern Matching - Ukkonen's Algorithm

A Python implementation of near-exact pattern matching using suffix trees built with Ukkonen's algorithm. Efficiently finds exact and approximate matches (Levenshtein distance ≤ 1) across multiple texts and patterns.

## Project Overview

This project implements a Generalized Suffix Tree (GST) for multi-string pattern matching with edit distance support. It uses Ukkonen's linear-time algorithm to construct suffix trees and leverages bidirectional matching for detecting insertions, deletions, replacements, and swaps.

## Algorithm Approach

### Ukkonen's Suffix Tree Construction

**Ukkonen's algorithm** builds a suffix tree in O(n) time using online construction:

1. **Global End**: All leaf edges share a global end pointer
2. **Active Point**: Tracks where new suffixes should be inserted
3. **Suffix Links**: Allow quick navigation between related suffixes
4. **Three Tricks**:
   - Trick 1: Active point tracking
   - Trick 2: Fast-forward along edges
   - Trick 3: Show-stopper rule

### Near-Exact Matching Strategy

Uses **bidirectional suffix tree matching**:

#### Forward Suffix Tree
- Built on original text
- Computes longest common prefix (LCP) from each position

#### Reverse Suffix Tree
- Built on reversed text
- Computes LCP from reverse direction

#### Combined Analysis

For each position i in text, compute:
- **Forward LCP**: Match length going forward
- **Backward LCP**: Match length going backward (with appropriate offsets)

### Why Suffix Trees?

**Advantages over Z-algorithm**:
- O(n) construction, O(m) per query
- Handles multiple patterns efficiently
- Supports generalized suffix trees (multiple texts)
- Enables advanced queries (longest repeats, LCP)

**Trade-offs**:
- Higher memory usage: O(n) nodes and edges
- More complex implementation
- Better for multiple queries over same text

## Usage

### Configuration File Format

**config.txt**:
```
N M
text_id1 text_file1.txt
text_id2 text_file2.txt
...
pattern_id1 pattern_file1.txt
pattern_id2 pattern_file2.txt
...
```

Where:
- N: Number of text files
- M: Number of pattern files
- text_id: Integer identifier for each text
- pattern_id: Integer identifier for each pattern

### Example Configuration

```
2 2
1 text1.txt
2 text2.txt
1 pattern1.txt
2 pattern2.txt
```

### Running

```bash
python suffix_tree_matching.py config.txt
```

### Output Format

**output_a2.txt**: Each line contains pattern_id, text_id, position, edit_distance
```
1 1 5 0
1 1 12 1
1 2 3 1
2 1 8 0
```

Where:
- Column 1: Pattern identifier
- Column 2: Text identifier
- Column 3: 1-indexed position in text
- Column 4: 0 = exact match, 1 = near-exact match

## Complexity Analysis

### Suffix Tree Construction (Ukkonen's Algorithm)

**Time Complexity**: O(n)
- Each character inserted exactly once
- Active point updates: amortized O(1) per character
- Suffix link traversals: amortized O(1)
- Total: Linear in text length

**Space Complexity**: O(n)
- At most 2n nodes for text of length n
- Each node has fixed-size array (119 entries for ASCII 8-126)
- Total: O(n × σ) where σ is alphabet size

### Pattern Matching

**Time Complexity**: O(n + m) per pattern-text pair
- n: Length of text
- m: Length of pattern
- Forward tree construction: O(n)
- Reverse tree construction: O(n)
- Matching all positions: O(n × m) worst case
  - Each position: O(m) for LCP computation
  - n positions to check
- Total: O(n + n × m) = O(nm) worst case

**Best Case**: O(n + m)
- When pattern doesn't exist or matches are rare
- LCP computation terminates early

**Space Complexity**: O(n)
- Forward suffix tree: O(n)
- Reverse suffix tree: O(n)
- Pattern storage: O(m)
- Total: O(2n + m) = O(n)

### Multiple Patterns and Texts

**Time Complexity**: O(N × M × (n × m))
- N: Number of texts
- M: Number of patterns
- Each pattern-text pair: O(nm)

**Space Complexity**: O(max(n₁, n₂, ..., nₙ))
- Suffix trees built one at a time
- Only largest text in memory simultaneously

## Testing

### Run Test Cases

```bash
python test_dense_match_cases.py
python test_DL_distance_5000_cases.py
python test_generated_lowercase_cases.py
python test_min5_overlap_cases.py
python test_ukkonen_DL_ascii_ctrl_mixed
python test_ukkonen_DL_ascii_ctrl.py
python test_ukkonen_DL_dense_strict.py
python test_ukkonen_DL_generated.py
```
