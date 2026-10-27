from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []

        for row, limit in zip(grid, limits):
            candidates.extend(sorted(row, reverse=True)[:limit])

        candidates.sort(reverse=True)
        return sum(candidates[:k])


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxSum([[1, 2], [3, 4]], [1, 2], 2) == 7
    assert solution.maxSum([[5, 3, 7], [8, 2, 6]], [2, 2], 3) == 21
    assert solution.maxSum([[1, 2], [3, 4]], [0, 0], 0) == 0

    print("All sample tests passed.")
