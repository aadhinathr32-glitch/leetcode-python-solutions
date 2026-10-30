# LeetCode Solutions

A collection of LeetCode solutions in Python and SQL, with explanations, complexity analysis, and example tests.

## Problems

| # | Problem | Difficulty | Solution |
|---|---|---|---|
| 3649 | Number of Perfect Pairs | Medium | [Python](3649-number-of-perfect-pairs.py) |
| 3521 | Find Product Recommendation Pairs | Medium | [SQL](sql/3521-find-product-recommendation-pairs.sql) |
| 2947 | Count Beautiful Substrings I | Medium | [Python](2947-count-beautiful-substrings-i.py) |
| 2139 | Minimum Moves to Reach Target Score | Medium | [Python](2139-minimum-moves-to-reach-target-score.py) |
| 310 | Minimum Height Trees | Medium | [Python](310-minimum-height-trees.py) |
| 1305 | All Elements in Two Binary Search Trees | Medium | [Python](1305-all-elements-in-two-binary-search-trees.py) |
| 1642 | Furthest Building You Can Reach | Medium | [Python](1642-furthest-building-you-can-reach.py) |
| 3918 | Sum of Primes Between Number and Its Reverse | Medium | [Python](3918-sum-of-primes-between-number-and-its-reverse.py) |
| 3071 | Minimum Operations to Write the Letter Y on a Grid | Medium | [Python](3071-minimum-operations-to-write-the-letter-y-on-a-grid.py) |
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
| 368 | Largest Divisible Subset | Medium | [Python](368-largest-divisible-subset.py) |
| 791 | Custom Sort String | Medium | [Python](791-custom-sort-string.py) |
| 2095 | Delete the Middle Node of a Linked List | Medium | [Python](2095-delete-the-middle-node-of-a-linked-list.py) |
| 1621 | Number of Sets of K Non-Overlapping Line Segments | Hard | [Python](1621-number-of-sets-of-k-non-overlapping-line-segments.py) |
| 3271 | Hash Divided String | Easy | [Python](3271-hash-divided-string.py) |
| 1010 | Pairs of Songs With Total Durations Divisible by 60 | Medium | [Python](1010-pairs-of-songs-with-total-durations-divisible-by-60.py) |
| 3462 | Maximum Sum With at Most K Elements | Medium | [Python](3462-maximum-sum-with-at-most-k-elements.py) |
| 1124 | Longest Well-Performing Interval | Medium | [Python](1124-longest-well-performing-interval.py) |
| — | Minimum Cost to Make Arrays Identical | Medium | [Python](minimum-cost-to-make-arrays-identical.py) |
| 3868 | Minimum Cost to Equalize Arrays Using Swaps | Medium | [Python](3868-minimum-cost-to-equalize-arrays-using-swaps.py) |
| 1424 | Diagonal Traverse II | Medium | [Python](1424-diagonal-traverse-ii.py) |
| 779 | K-th Symbol in Grammar | Medium | [Python](779-k-th-symbol-in-grammar.py) |
| 78 | Subsets | Medium | [Python](78-subsets.py) |

## How to run

```bash
python 3649-number-of-perfect-pairs.py
python 2947-count-beautiful-substrings-i.py
```


Python solutions require Python 3.9 or newer. The SQL solution is written for MySQL and can be run in a MySQL-compatible SQL editor.

Run standalone solutions from the repository directory:

```bash
python 2947-count-beautiful-substrings-i.py
python 310-minimum-height-trees.py
python 1305-all-elements-in-two-binary-search-trees.py
python 1642-furthest-building-you-can-reach.py
python 3918-sum-of-primes-between-number-and-its-reverse.py
python 3071-minimum-operations-to-write-the-letter-y-on-a-grid.py
python 3458-select-k-disjoint-special-substrings.py
python 2289-steps-to-make-array-non-decreasing.py
python 1155-number-of-dice-rolls-with-target-sum.py
python 2391-minimum-amount-of-time-to-collect-garbage.py
python 1685-sum-of-absolute-differences-in-a-sorted-array.py
python 1472-design-browser-history.py
python 1105-filling-bookcase-shelves.py
python 1029-two-city-scheduling.py
python 841-keys-and-rooms.py
python 368-largest-divisible-subset.py
python 791-custom-sort-string.py
python 2095-delete-the-middle-node-of-a-linked-list.py
python 1621-number-of-sets-of-k-non-overlapping-line-segments.py
python 3271-hash-divided-string.py
python 1010-pairs-of-songs-with-total-durations-divisible-by-60.py
python 3462-maximum-sum-with-at-most-k-elements.py
python 1124-longest-well-performing-interval.py
python minimum-cost-to-make-arrays-identical.py
python 3868-minimum-cost-to-equalize-arrays-using-swaps.py
python 1424-diagonal-traverse-ii.py
python 779-k-th-symbol-in-grammar.py
python 78-subsets.py
```

The standalone scripts include sample assertions and print `All sample tests passed.` when those assertions succeed. The LeetCode 449 solution is a `Codec` class and relies on LeetCode's provided `TreeNode` definition.

## SQL Solutions

### 3521 — Find Product Recommendation Pairs

Self-join `ProductPurchases` on `user_id` to pair products bought by the same customer. Keep only pairs where the first product ID is smaller, join `ProductInfo` twice to retrieve both categories, group by the product pair, and retain pairs bought by at least three distinct customers. Sort by customer count descending, then product IDs ascending.

- **Time:** O(P²) in the worst case per customer’s purchases, where P is the total number of purchase rows; the join workload depends on how many products each customer purchased
- **Auxiliary space:** O(Q) for grouped product pairs, where Q is the number of distinct pairs generated

## Python Approaches

### 3649 — Number of Perfect Pairs

Convert every number to its absolute value and sort the resulting array. For a sorted pair with smaller value `x` and larger value `y`, the original conditions simplify to `y <= 2 * x`. Maintain a sliding window with two pointers; for each right endpoint, all earlier values from `left` through `right - 1` form valid pairs, so add `right - left` to the answer.

- **Time:** O(n log n) for sorting, followed by O(n) for the two-pointer scan
- **Auxiliary space:** O(n) for the sorted absolute-value array


### 2947 — Count Beautiful Substrings I

Enumerate all substrings and maintain vowel and consonant counts as the end index moves. Count a substring when both counts are equal and their product is divisible by `k`.

- **Time:** O(n²)
- **Auxiliary space:** O(1)

### 2139 — Minimum Moves to Reach Target Score

Work backward from `target`: halve it when it is even and a double remains; otherwise subtract one to reverse an increment. Once no doubles remain, add all remaining increments (`target - 1`).

- **Time:** O(log target)
- **Auxiliary space:** O(1)


### 3918 — Sum of Primes Between Number and Its Reverse

Reverse the digits of `n` to determine the inclusive range between the smaller and larger number. Check each number in that range for primality by testing divisors up to its square root, and add the primes to the total.

- **Time:** O(R√R), where R is the larger endpoint of the range
- **Auxiliary space:** O(1)

### 1642 — Furthest Building You Can Reach

Use a min-heap to track upward climbs. Initially treat each climb as ladder-covered; whenever climbs exceed the number of ladders, use bricks for the smallest climb. If bricks run out, the previous building is the furthest reachable one.

- **Time:** O(n log n)
- **Auxiliary space:** O(n)

### 1305 — All Elements in Two Binary Search Trees

Perform an inorder traversal of each BST to produce two sorted lists, then merge the lists in ascending order. This preserves duplicate values and also handles an empty tree.

- **Time:** O(n + m), where n and m are the numbers of nodes in the two trees
- **Auxiliary space:** O(n + m) for the traversal lists and merged result

### 310 — Minimum Height Trees

Repeatedly remove all current leaves (nodes with one neighbor) until one or two nodes remain. These remaining center nodes are the roots that produce minimum-height trees. Handle the single-node tree separately.

- **Time:** O(n)
- **Auxiliary space:** O(n)

### 3071 — Minimum Operations to Write the Letter Y on a Grid

Count the occurrences of each value (0, 1, or 2) inside the Y and outside it. Try every pair of different target values for the Y and the remaining cells; choose the pair that preserves the most existing cells, minimizing changes.

- **Time:** O(n²)
- **Auxiliary space:** O(1), using two arrays of three counters

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

### 368 — Largest Divisible Subset

Sort the numbers, then use dynamic programming. For each number, record the length of the largest divisible subset ending there and the previous number that extends that subset. Follow the parent links from the longest endpoint to reconstruct one valid subset.

- **Time:** O(n²)
- **Auxiliary space:** O(n)

### 791 — Custom Sort String

Count the characters in `s`. Append each character in `order` as many times as it occurs in `s`, following the custom order. Then append any remaining characters that do not appear in `order`.

- **Time:** O(|order| + |s|)
- **Auxiliary space:** O(|s|) for the character counts and result

### 2095 — Delete the Middle Node of a Linked List

Use slow and fast pointers to find the middle node. Keep track of the node before `slow`, then skip the middle node by updating its `next` pointer. If the list has one node, return `None`.

- **Time:** O(n)
- **Auxiliary space:** O(1)

### 1621 — Number of Sets of K Non-Overlapping Line Segments

The number of valid ways is the combination C(n + k - 1, 2k). Each segment contributes two endpoints, and allowing segments to share endpoints is accounted for by the k - 1 extra positions in the combination. Compute the combination using factorials and modular inverse under 10^9 + 7.

- **Time:** O(n + k + log MOD)
- **Auxiliary space:** O(n + k)

### 3271 — Hash Divided String

Split the string into chunks of length `k`. For each chunk, sum each character's zero-based alphabet index, take the sum modulo 26, and convert the result back to a lowercase letter.

- **Time:** O(n)
- **Auxiliary space:** O(n) for the result

### 1010 — Pairs of Songs With Total Durations Divisible by 60

Count song durations by their remainder modulo 60. For each song, add the number of previously seen songs with the complementary remainder needed to make the pair divisible by 60, then record the current remainder. This counts each pair exactly once.

- **Time:** O(n)
- **Auxiliary space:** O(1), using a fixed array of 60 remainder counts

### 3462 — Maximum Sum With at Most K Elements

For each row, take at most the number of elements allowed by its limit, choosing the largest values. Combine these candidates from all rows, sort them in descending order, and sum the largest `k` values. Since all grid values are non-negative, selecting fewer than `k` elements cannot improve the sum over selecting available positive candidates.

- **Time:** O(n × m log m + L log L), where L is the total number of candidates collected
- **Auxiliary space:** O(L)

### 1124 — Longest Well-Performing Interval

Convert each day into `+1` if it is tiring (more than 8 hours) or `-1` otherwise. A positive prefix sum means the interval from day 0 is well-performing. Otherwise, use the earliest index of a prefix sum one lower to find the longest valid interval ending at the current day.

- **Time:** O(n)
- **Auxiliary space:** O(n)

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

### 1424 — Diagonal Traverse II

Group each value by its diagonal index, `row + column`. Visit rows from bottom to top so values in each diagonal are already in the required order, then concatenate the diagonal groups.

- **Time:** O(N), where N is the total number of elements
- **Auxiliary space:** O(N) for the diagonal groups and result

## Goal

Keep adding solutions as I practice algorithms, problem-solving, and Python.
