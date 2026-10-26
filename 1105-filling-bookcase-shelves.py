"""LeetCode 1105: Filling Bookcase Shelves

Dynamic programming:
dp[i] is the minimum height needed to place the first i books.
For each ending position i, work backwards to try every consecutive group
of books that fits on the current shelf. Track the group's total width and
maximum height, then combine that shelf height with dp[j] for the books before it.

Time: O(n^2)
Auxiliary space: O(n)
"""


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            width = 0
            height = 0
            dp[i] = float("inf")

            for j in range(i - 1, -1, -1):
                width += books[j][0]

                if width > shelfWidth:
                    break

                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    assert solution.minHeightShelves(
        [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
    ) == 6
    assert solution.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6) == 4
    print("All sample tests passed.")
