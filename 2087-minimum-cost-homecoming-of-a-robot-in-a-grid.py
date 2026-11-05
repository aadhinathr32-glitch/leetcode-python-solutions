class Solution:
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        start_row, start_col = startPos
        home_row, home_col = homePos

        total_cost = 0

        # Move vertically
        if start_row < home_row:
            for row in range(start_row + 1, home_row + 1):
                total_cost += rowCosts[row]
        else:
            for row in range(start_row - 1, home_row - 1, -1):
                total_cost += rowCosts[row]

        # Move horizontally
        if start_col < home_col:
            for col in range(start_col + 1, home_col + 1):
                total_cost += colCosts[col]
        else:
            for col in range(start_col - 1, home_col - 1, -1):
                total_cost += colCosts[col]

        return total_cost


solution = Solution()
assert solution.minCost(
    [1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]
) == 18
assert solution.minCost([0, 0], [0, 0], [5], [26]) == 0
print("All sample tests passed.")
