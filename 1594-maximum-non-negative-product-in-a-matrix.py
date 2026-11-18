class Solution:
    def maxProductPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # dp[i][j] = [minimum product, maximum product]
        dp = [[None] * n for _ in range(m)]

        dp[0][0] = [grid[0][0], grid[0][0]]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                candidates = []

                if i > 0:
                    candidates.append(dp[i - 1][j])

                if j > 0:
                    candidates.append(dp[i][j - 1])

                min_product = float("inf")
                max_product = float("-inf")

                for minimum, maximum in candidates:
                    min_product = min(
                        min_product,
                        minimum * value,
                        maximum * value
                    )
                    max_product = max(
                        max_product,
                        minimum * value,
                        maximum * value
                    )

                dp[i][j] = [min_product, max_product]

        result = dp[m - 1][n - 1][1]

        if result < 0:
            return -1

        return result % (10**9 + 7)


solution = Solution()
assert solution.maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]) == -1
assert solution.maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]) == 8
assert solution.maxProductPath([[1, 3], [0, -4]]) == 0
print("All sample tests passed.")
