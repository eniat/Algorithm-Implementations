# Algorithms and Data Structures Problem Set

This repository contains a compact set of algorithm implementations and written answers.
It focuses on sorting, graph algorithms, linked lists, binary search trees, heaps and asymptotic reasoning.

The work demonstrates core data-structure implementation and algorithmic problem solving across Python and C.

## Contents

```text
.
├── q3-radixsort.c
├── q4-prop-stat.py
├── q5b-linked-list-quicksort.py
├── q5c-linked-list-to-balanced-tree.py
├── q6b-robot-tournament.py
└── textual-answers.txt
```

## Implemented Work

### Radix Sort in C

`q3-radixsort.c` implements radix sort for integer arrays.
It uses counting sort as the stable subroutine, applies digit passes from least significant to most significant digit, and includes an example `main()` function that prints the sorted output.
This demonstrates a non-comparison sorting algorithm implemented directly in C.

### 2-SAT Satisfiability Checker

`q4-prop-stat.py` implements a satisfiability checker for formulas in 2-CNF form.
It constructs an implication graph, builds the reverse graph and applies Kosaraju's algorithm using two depth-first search passes.
A formula is unsatisfiable if a variable and its negation appear in the same strongly connected component.
The script includes several example formulas and prints whether each one is satisfiable.

### Linked List Quicksort

`q5b-linked-list-quicksort.py` implements quicksort over a singly linked list.
It uses a `ListNode` class, tail detection, Lomuto-style partitioning and recursive linked-list sorting.
The implementation swaps node values rather than relying on array indexing.
The script builds an example linked list, sorts it and prints the sorted values.

### Linked List to Balanced Binary Search Tree

`q5c-linked-list-to-balanced-tree.py` converts an unsorted linked list into a balanced binary search tree.
The list is first sorted using quicksort.
The middle node of the sorted list is selected as the root, with the left and right halves used recursively to build the subtrees.
The resulting tree is printed using preorder traversal.

### Robot Tournament Using a Max Heap

`q6b-robot-tournament.py` solves a tournament problem where the two strongest robots fight repeatedly until one or none remains.
It uses max-heap construction, heapify-down, heapify-up, repeated extraction of the two largest values and reinsertion of the remaining health difference.
The file includes test cases for normal input, empty input, equal values, a single robot and large health differences.

### Written Algorithm Answers

`textual-answers.txt` contains written answers covering duplicate removal, closest fixed-point measurements, 2-SAT runtime, full vs complete binary trees and heap properties.
These answers support the code by explaining algorithm design choices and complexity.

## Technologies Used

- Python 3
- C
- GCC or another C compiler
- Standard Python runtime only

No external Python packages are required.

## Running the Python Files

Run each Python script directly:

```bash
python q4-prop-stat.py
python q5b-linked-list-quicksort.py
python q5c-linked-list-to-balanced-tree.py
python q6b-robot-tournament.py
```

Each script contains built-in example inputs, so no command-line arguments are required.

## Compiling and Running the C File

Compile the radix sort implementation with GCC:

```bash
gcc q3-radixsort.c -o radixsort
./radixsort
```

On Windows with MinGW:

```bash
gcc q3-radixsort.c -o radixsort.exe
radixsort.exe
```

## Expected Outputs

The scripts demonstrate sorted integer arrays, satisfiable and unsatisfiable 2-CNF formulas, sorted linked-list values, preorder traversal of a balanced binary search tree and final robot health values after heap-based battles.

## Skills Demonstrated

- Algorithm implementation
- Complexity analysis
- Recursive programming
- Linked-list manipulation
- Graph traversal
- Strongly connected components
- Heap operations
- C array programming
- Python scripting

## Limitations

These are standalone problem-set solutions rather than a packaged application.
The scripts use hard-coded examples instead of command-line arguments or automated unit tests.
The implementations prioritise showing the algorithms clearly over production-level error handling.
