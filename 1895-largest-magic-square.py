class Solution:
    def largestMagicSquare(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Prefix sums for rows and columns
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * n for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                row_prefix[r][c + 1] = row_prefix[r][c] + grid[r][c]
                col_prefix[r + 1][c] = col_prefix[r][c] + grid[r][c]

        # Try every possible size, starting from the largest
        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    # Target sum from the first row
                    target = row_prefix[r][c + k] - row_prefix[r][c]

                    # Check all rows
                    valid = True
                    for i in range(r, r + k):
                        row_sum = row_prefix[i][c + k] - row_prefix[i][c]
                        if row_sum != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check all columns
                    for j in range(c, c + k):
                        col_sum = col_prefix[r + k][j] - col_prefix[r][j]
                        if col_sum != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check both diagonals
                    diagonal1 = 0
                    diagonal2 = 0

                    for i in range(k):
                        diagonal1 += grid[r + i][c + i]
                        diagonal2 += grid[r + i][c + k - 1 - i]

                    if diagonal1 == target and diagonal2 == target:
                        return k

        return 1


solution = Solution()
assert solution.largestMagicSquare([
    [7, 1, 4, 5, 6],
    [2, 5, 1, 6, 4],
    [1, 5, 4, 3, 2],
    [1, 2, 7, 3, 4]
]) == 3

assert solution.largestMagicSquare([
    [5, 1, 3, 1],
    [9, 3, 3, 1],
    [1, 3, 3, 8]
]) == 2

print("All sample tests passed.")
