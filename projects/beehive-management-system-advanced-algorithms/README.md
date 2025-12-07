# Beehive Management System - Advanced Data Structures

A Python-based beehive management system utilizing advanced data structures including 3D Binary Space Partitioning Trees (3DBeeTree), Binary Search Trees, Max Heaps, and Percentile tracking for efficient spatial organization and resource optimization.

## Overview

This project implements a sophisticated beehive management system designed to efficiently store, query, and harvest beehives in 3D space. The system uses custom data structures to optimize operations like spatial queries, resource selection, and balanced tree construction.

## Features

- **3D Spatial Indexing**: Store and query beehives in 3-dimensional space using an octree-based structure (3DBeeTree)
- **Optimal Beehive Selection**: Use max-heap data structure to efficiently select the best beehive for harvesting based on nutrient factor and capacity
- **Balanced Tree Construction**: Generate optimal insertion orders to create balanced 3D trees with minimal depth
- **Percentile Tracking**: Efficiently track and query data percentiles using Binary Search Trees
- **Resource Management**: Calculate emerald yields from beehive harvesting with volume and capacity tracking

## Setup

Note: For all of these you may need to replace `python` with `py` or `python3` depending on your operating system and python version.

```bash
python -m pip install virtualenv
python -m venv venv
```

Next, activate your virtual environment (Must be done every time you open the terminal)

**Windows Bash**
```bash
source venv/Scripts/activate
```

**Windows CMD**
```cmd
venv/Scripts/activate
```

**Windows Powershell**
```powershell
venv/Scripts/activate.ps1
```

**Mac / Linux bash**
```bash
source venv/bin/activate
```

Then install the requirements (if any)!
```bash
python -m pip install -r requirements.txt
```

## Running Tests

Run the complete test suite:
```bash
python run_tests.py
```

Run specific test groups:
```bash
python run_tests.py 1
```
This will run all tests marked with `@number("1.x")`.


## Complexity Analysis

### 3DBeeTree Operations
- **Insert**: O(log n) average, O(n) worst case
- **Search**: O(log n) average, O(n) worst case
- **Balanced Insert** (with make_ordering): O(log n) guaranteed

### BeehiveSelector Operations
- **set_all_beehives**: O(n) using heapify
- **add_beehive**: O(log n)
- **harvest_best_beehive**: O(log n)

### Percentiles Operations
- **add_point**: O(log n)
- **remove_point**: O(log n)
- **ratio**: O(log n + k) where k is the number of results

## Time Complexity Summary
| Operation | Data Structure | Best Case | Worst Case |
|-----------|---------------|-----------|------------|
| Insert | 3DBeeTree | O(log n) | O(n) |
| Search | 3DBeeTree | O(log n) | O(n) |
| Insert | BST | O(log n) | O(n) |
| Delete | BST | O(log n) | O(n) |
| Add | Max Heap | O(1) | O(log n) |
| Extract Max | Max Heap | O(log n) | O(log n) |
| Heapify | Max Heap | O(n) | O(n) |
| Ratio Query | Percentiles | O(log n + k) | O(log n + k) |
| Balanced Ordering | make_ordering | O(n log n) | O(n log n) |