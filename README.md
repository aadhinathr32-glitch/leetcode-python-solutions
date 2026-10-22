# LeetCode Python Solutions

A collection of Python solutions to LeetCode problems, with explanations, complexity analysis, and example tests.

## Problems

| # | Problem | Difficulty | Solution |
|---|---|---|---|
| 449 | Serialize and Deserialize BST | Medium | [Python](449-serialize-and-deserialize-bst.py) |
| 1155 | Number of Dice Rolls With Target Sum | Medium | [Python](1155-number-of-dice-rolls-with-target-sum.py) |
| 2391 | Minimum Amount of Time to Collect Garbage | Medium | [Python](2391-minimum-amount-of-time-to-collect-garbage.py) |

## How to run

Requires Python 3.9 or newer.

Run the standalone solutions from the repository directory:

```bash
python 1155-number-of-dice-rolls-with-target-sum.py
python 2391-minimum-amount-of-time-to-collect-garbage.py
```

The scripts include sample assertions and print `All sample tests passed.` when those assertions succeed. The LeetCode 449 solution is a `Codec` class and relies on LeetCode's provided `TreeNode` definition.

## Approaches

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

## Goal

Keep adding solutions as I practice algorithms, problem-solving, and Python.
