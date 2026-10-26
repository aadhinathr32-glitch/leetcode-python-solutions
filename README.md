# LeetCode Python Solutions

A collection of Python solutions to LeetCode problems, with explanations, complexity analysis, and example tests.

## Problems

| # | Problem | Difficulty | Solution |
|---|---|---|---|
| 3458 | Select K Disjoint Special Substrings | Medium | [Python](3458-select-k-disjoint-special-substrings.py) |
| 2289 | Steps to Make Array Non-decreasing | Medium | [Python](2289-steps-to-make-array-non-decreasing.py) |
| 449 | Serialize and Deserialize BST | Medium | [Python](449-serialize-and-deserialize-bst.py) |
| 1155 | Number of Dice Rolls With Target Sum | Medium | [Python](1155-number-of-dice-rolls-with-target-sum.py) |
| 2391 | Minimum Amount of Time to Collect Garbage | Medium | [Python](2391-minimum-amount-of-time-to-collect-garbage.py) |
| 1685 | Sum of Absolute Differences in a Sorted Array | Medium | [Python](1685-sum-of-absolute-differences-in-a-sorted-array.py) |
| 1472 | Design Browser History | Medium | [Python](1472-design-browser-history.py) |
| 1105 | Filling Bookcase Shelves | Medium | [Python](1105-filling-bookcase-shelves.py) |
| 1029 | Two City Scheduling | Medium | [Python](1029-two-city-scheduling.py) |
| 841 | Keys and Rooms | Medium | [Python](841-keys-and-rooms.py) |
| — | Minimum Cost to Make Arrays Identical | Medium | [Python](minimum-cost-to-make-arrays-identical.py) |
| 3868 | Minimum Cost to Equalize Arrays Using Swaps | Medium | [Python](3868-minimum-cost-to-equalize-arrays-using-swaps.py) |
| 779 | K-th Symbol in Grammar | Medium | [Python](779-k-th-symbol-in-grammar.py) |
| 78 | Subsets | Medium | [Python](78-subsets.py) |

## How to run

Requires Python 3.9 or newer.

Run standalone solutions from the repository directory:

```bash
python 3458-select-k-disjoint-special-substrings.py
python 2289-steps-to-make-array-non-decreasing.py
python 1155-number-of-dice-rolls-with-target-sum.py
python 2391-minimum-amount-of-time-to-collect-garbage.py
python 1685-sum-of-absolute-differences-in-a-sorted-array.py
python 1472-design-browser-history.py
python 1105-filling-bookcase-shelves.py
python 1029-two-city-scheduling.py
python 841-keys-and-rooms.py
python minimum-cost-to-make-arrays-identical.py
python 3868-minimum-cost-to-equalize-arrays-using-swaps.py
python 779-k-th-symbol-in-grammar.py
python 78-subsets.py
```

The standalone scripts include sample assertions and print `All sample tests passed.` when those assertions succeed. The LeetCode 449 solution is a `Codec` class and relies on LeetCode's provided `TreeNode` definition.

## Approaches

### 3458 — Select K Disjoint Special Substrings

Build candidate intervals from each character's first occurrence, expanding an interval until it contains every occurrence of each character inside it. Exclude the whole string, sort intervals by ending position, and greedily choose non-overlapping intervals. If `k == 0`, return `True`.

- **Time:** O(26 × n + 26 log 26), effectively O(n) for lowercase English letters
- **Auxiliary space:** O(26), effectively O(1)

### 2289 — Steps to Make Array Non-decreasing

Use a monotonic stack storing each value and the number of steps needed for its removal. Each element is pushed and popped at most once.

- **Time:** O(n)
- **Auxiliary space:** O(n)

### 449 — Serialize and Deserialize BST

Serialize using preorder traversal (root, left, right). Because the input is a BST, deserialize by reading preorder values with lower and upper bounds; null-child markers are unnecessary.

- **Serialization time:** O(n)
- **Deserialization time:** O(n)
- **Encoded space:** O(n); recursion stack: O(h)

### 1155 — Number of Dice Rolls With Target Sum

Dynamic programming: `dp[s]` stores the number of ways to make sum `s` using the dice processed so far. For each die, try every face from 1 through `k`, keeping counts modulo `10^9 + 7`.

- **Time:** O(n × target × k)
- **Auxiliary space:** O(target)

### 2391 — Minimum Amount of Time to Collect Garbage

Count the pickup time for every unit of garbage. For each truck type, add the travel time needed to reach the last house containing that type.

- **Time:** O(n + total garbage characters), with only three garbage types
- **Auxiliary space:** O(1) auxiliary space, excluding input and temporary travel slices

### 1685 — Sum of Absolute Differences in a Sorted Array

Use a running prefix sum and the total sum. Since the array is sorted, calculate the sum of differences to the left and right of each element in constant time per index.

- **Time:** O(n)
- **Auxiliary space:** O(n) for the result

### 1472 — Design Browser History

Store visited URLs in a list and track the current page using an index. Visiting a URL truncates forward history, while back and forward clamp the index to valid bounds.

- **visit:** O(n) due to slicing the forward history
- **back / forward:** O(1)

### 1105 — Filling Bookcase Shelves

Use dynamic programming where `dp[i]` is the minimum height needed for the first `i` books. For each position, try placing every valid consecutive group of books on the final shelf and combine its maximum height with the best height for the preceding books.

- **Time:** O(n²)
- **Auxiliary space:** O(n)

### 1029 — Two City Scheduling

Sort people by the difference between their city A and city B costs. Assign the first half to city A and the remaining half to city B, ensuring exactly half go to each city at minimum total cost.

- **Time:** O(n log n)
- **Auxiliary space:** O(n) for the sorted copy

### 841 — Keys and Rooms

Use an iterative depth-first search starting from room 0. Track visited rooms in a set and push each newly discovered room onto a stack. All rooms are reachable if every room is visited.

- **Time:** O(n + k), where n is the number of rooms and k is the total number of keys
- **Auxiliary space:** O(n) for the stack and visited set

### 779 — K-th Symbol in Grammar

Use recursion to trace the symbol back to the previous row. Its parent position is `(k + 1) // 2`; odd positions preserve the parent's value, while even positions flip it.

- **Time:** O(n)
- **Auxiliary space:** O(n) for the recursion stack

### 78 — Subsets

Start with the empty subset. For each number, create new subsets by adding that number to every subset already collected. Since the input values are unique, this generates every subset exactly once.

- **Time:** O(n × 2ⁿ), because there are 2ⁿ subsets and copying each subset takes up to O(n)
- **Auxiliary space:** O(n × 2ⁿ) to store all subsets

### Minimum Cost to Make Arrays Identical

Count each value in both arrays together. Every combined frequency must be even, because the final arrays must contain the same number of each value. If any frequency is odd, return `-1`. Otherwise, the target count for each array is half the combined frequency; count the surplus occurrences in `nums1` to get the minimum number of paid cross-array swaps.

- **Time:** O(n)
- **Auxiliary space:** O(u), where u is the number of distinct values

### 3868 — Minimum Cost to Equalize Arrays Using Swaps

Count the combined frequency of every value. If any frequency is odd, equal arrays are impossible. Otherwise, each array must contain half of each value's combined frequency; sum the surplus occurrences in `nums1` to get the minimum number of paid swaps.

- **Time:** O(n)
- **Auxiliary space:** O(u), where u is the number of distinct values

## Goal

Keep adding solutions as I practice algorithms, problem-solving, and Python.
