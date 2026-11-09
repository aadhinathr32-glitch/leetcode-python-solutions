class Solution:
    def equalPairs(self, grid):
        n = len(grid)

        # Store each row and its frequency
        row_count = {}

        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1

        answer = 0

        # Check each column
        for c in range(n):
            column = []

            for r in range(n):
                column.append(grid[r][c])

            column_tuple = tuple(column)

            if column_tuple in row_count:
                answer += row_count[column_tuple]

        return answer


solution = Solution()
assert solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
assert solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
print("All sample tests passed.")
