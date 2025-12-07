# Boyer-Moore for Binary Strings - Optimized Pattern Matching

A Python implementation of an optimized Boyer-Moore algorithm specifically designed for binary strings, featuring block-based bad character rules, Galil's optimization, and rolling hash techniques.

## Project Overview

This project implements an enhanced Boyer-Moore string matching algorithm optimized for binary strings (sequences of 0s and 1s). Traditional Boyer-Moore struggles with binary alphabets due to limited character variety, so this implementation uses block-based matching and advanced optimizations.

## Algorithm Approach

### Enhanced Boyer-Moore Strategy

Traditional Boyer-Moore uses two rules:
1. **Bad Character Rule**: Skip based on mismatched character
2. **Good Suffix Rule**: Skip based on matched suffix

This implementation adds:
3. **Block-Based Bad Character**: Groups bits into blocks for better skipping
4. **Galil's Optimization**: Skip redundant comparisons in matched regions
5. **Rolling Hash**: Efficient block computation

### Why Optimize for Binary?

**Problem**: Binary strings have only 2 characters (0, 1)
- Bad character rule becomes ineffective
- Small alphabet → frequent character occurrences
- Poor skip distances → more comparisons

**Solution**: Block-based matching
- Treat groups of bits as units
- Larger "alphabet" (2^k possibilities for k-bit blocks)
- Better skip distances
- Fewer comparisons

## Usage

### Command Line

```bash
python boyer_moore_binary.py test_text.txt test_pattern.txt
```

### Input Format

**text.txt**: Single line of binary string
```
10101010101010101010
```

**pattern.txt**: Single line of binary pattern
```
101
```

### Output Format

**output_a1q2.txt**: Each line contains 1-indexed position
```
1
3
5
7
```

## Complexity Analysis

### Preprocessing Phase

**Time Complexity**: O(m)
- Bad character table: O(m)
- Block bad character table: O(m)
- Good suffix array: O(m) - Z-algorithm on reverse
- Matched prefix array: O(m) - Z-algorithm

**Space Complexity**: O(m × 2^k)
- Normal bad character: O(m)
- Block bad character: O(m × 2^k) where k = block size
- Good suffix: O(m)
- Matched prefix: O(m)
- For k=5: O(32m) = O(m)

### Search Phase

**Time Complexity**:
- **Best Case**: O(m + n/m)
  - Large skips due to block-based bad character
  - Pattern rarely appears
  - Skip approximately m positions each time
  
- **Worst Case**: O(mn)
  - Pattern occurs frequently
  - Many partial matches requiring full comparisons
  - Example: text="000000000", pattern="000"

**Space Complexity**: O(1)
- Only uses constant extra space during search
- Galil variables: O(1)

### With Galil's Optimization

**Amortized**: O(m + n)
- Each character compared at most once
- Matched regions skipped
- Total comparisons ≤ n

## Optimization Comparison

| Technique | Benefit | Cost |
|-----------|---------|------|
| Traditional BC | O(σ) shift | Ineffective for small σ |
| Block-based BC | O(m) shift | O(2^k × m) space |
| Good Suffix | O(m) shift | O(m) preprocessing |
| Matched Prefix | O(m) shift | O(m) preprocessing |
| Galil's Rule | Skip comparisons | O(1) overhead |

## Testing

### Run Test Cases

```bash
python test_binary_boyer_moore_cases.py
python test_binary_boyer_moore_high_matches.py
python test_boyer_moore_binary_long_patterns.py
python test_boyer_moore_binary.py
```

### Test Cases to Verify

- Exact single match
- Multiple matches
- Overlapping matches
- Pattern not found
- Pattern at boundaries
- Pattern longer than text
- Highly repetitive patterns (worst case)