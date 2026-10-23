"""LeetCode 779: K-th Symbol in Grammar.

Approach:
Each symbol at position k comes from position (k + 1) // 2 in the
previous row. Odd positions keep the parent's value; even positions flip it.
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        return parent if k % 2 == 1 else 1 - parent


if __name__ == "__main__":
    solution = Solution()
    assert solution.kthGrammar(1, 1) == 0
    assert solution.kthGrammar(2, 1) == 0
    assert solution.kthGrammar(2, 2) == 1
    assert solution.kthGrammar(3, 4) == 0
    assert solution.kthGrammar(4, 5) == 1
    print("All sample tests passed.")
