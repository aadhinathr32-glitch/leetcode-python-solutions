class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)

        # dp[i][j] = minimum score to triangulate
        # the polygon section from i to j
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Length of interval
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")

                # Choose k as the third vertex of the triangle
                for k in range(i + 1, j):
                    score = (
                        dp[i][k]
                        + dp[k][j]
                        + values[i] * values[k] * values[j]
                    )
                    dp[i][j] = min(dp[i][j], score)

        return dp[0][n - 1]


solution = Solution()
assert solution.minScoreTriangulation([1, 2, 3]) == 6
assert solution.minScoreTriangulation([3, 7, 4, 5]) == 144
assert solution.minScoreTriangulation([1, 3, 1, 4, 1, 5]) == 13

print("All sample tests passed.")
