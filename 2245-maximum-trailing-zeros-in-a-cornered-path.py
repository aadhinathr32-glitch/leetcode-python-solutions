class Solution:
    def maxTrailingZeros(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Count factors of 2 and 5 in every cell
        twos = [[0] * n for _ in range(m)]
        fives = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                num = grid[r][c]

                count2 = 0
                count5 = 0

                while num % 2 == 0:
                    count2 += 1
                    num //= 2

                num = grid[r][c]

                while num % 5 == 0:
                    count5 += 1
                    num //= 5

                twos[r][c] = count2
                fives[r][c] = count5

        # Row prefix sums
        row2 = [[0] * (n + 1) for _ in range(m)]
        row5 = [[0] * (n + 1) for _ in range(m)]

        for r in range(m):
            for c in range(n):
                row2[r][c + 1] = row2[r][c] + twos[r][c]
                row5[r][c + 1] = row5[r][c] + fives[r][c]

        # Column prefix sums
        col2 = [[0] * n for _ in range(m + 1)]
        col5 = [[0] * n for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                col2[r + 1][c] = col2[r][c] + twos[r][c]
                col5[r + 1][c] = col5[r][c] + fives[r][c]

        answer = 0

        for r in range(m):
            for c in range(n):
                cell2 = twos[r][c]
                cell5 = fives[r][c]

                # Up + Left
                total2 = col2[r + 1][c] + row2[r][c + 1] - cell2
                total5 = col5[r + 1][c] + row5[r][c + 1] - cell5
                answer = max(answer, min(total2, total5))

                # Up + Right
                total2 = col2[r + 1][c] + (row2[r][n] - row2[r][c]) - cell2
                total5 = col5[r + 1][c] + (row5[r][n] - row5[r][c]) - cell5
                answer = max(answer, min(total2, total5))

                # Down + Left
                total2 = (col2[m][c] - col2[r][c]) + row2[r][c + 1] - cell2
                total5 = (col5[m][c] - col5[r][c]) + row5[r][c + 1] - cell5
                answer = max(answer, min(total2, total5))

                # Down + Right
                total2 = (col2[m][c] - col2[r][c]) + (row2[r][n] - row2[r][c]) - cell2
                total5 = (col5[m][c] - col5[r][c]) + (row5[r][n] - row5[r][c]) - cell5
                answer = max(answer, min(total2, total5))

        return answer


solution = Solution()
assert solution.maxTrailingZeros(
    [[23,17,15,3,20],
     [8,1,20,27,11],
     [9,4,6,2,21],
     [40,9,1,10,6],
     [22,7,4,5,3]]
) == 3

assert solution.maxTrailingZeros(
    [[4,3,2],
     [7,6,1],
     [8,8,8]]
) == 0

print("All sample tests passed.")
