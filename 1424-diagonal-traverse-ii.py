from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = []

        # For each diagonal, rows are visited from bottom to top.
        for row in range(len(nums) - 1, -1, -1):
            for col, value in enumerate(nums[row]):
                diagonal = row + col

                if diagonal == len(diagonals):
                    diagonals.append([])

                diagonals[diagonal].append(value)

        result = []
        for diagonal in diagonals:
            result.extend(diagonal)

        return result


# Sample tests
solution = Solution()

assert solution.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    1, 4, 2, 7, 5, 3, 8, 6, 9
]
assert solution.findDiagonalOrder([
    [1, 2, 3, 4, 5],
    [6, 7],
    [8],
    [9, 10, 11],
    [12, 13, 14, 15, 16],
]) == [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]

print("All sample tests passed.")
