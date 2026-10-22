# LeetCode Python Solutions

A collection of Python solutions to LeetCode problems, with explanations, complexity analysis, and example tests.

## Problems

| # | Problem | Difficulty | Solution |
|---|---|---|---|
| 2391 | Minimum Amount of Time to Collect Garbage | Medium | [Python](2391-minimum-amount-of-time-to-collect-garbage.py) |

## How to run

Requires Python 3.9 or newer.

```bash
python 2391-minimum-amount-of-time-to-collect-garbage.py
```

The script includes sample assertions. A successful run prints:

```text
All sample tests passed.
```

## Problem-solving approach

For each garbage type, its truck only needs to travel as far as the last house containing that type. The total time is the number of garbage units (pickup time) plus each truck's travel time to its last required house.

## Complexity for problem 2391

- **Time:** O(n + total garbage characters) for the intended approach. (The current solution sums a travel prefix for each of at most three types; with the bounded three types this is linear overall.)
- **Auxiliary space:** O(1), excluding input and temporary travel slices.
