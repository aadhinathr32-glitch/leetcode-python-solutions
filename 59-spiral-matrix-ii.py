class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:
            # Move left to right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # Move top to bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # Move right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # Move bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix


solution = Solution()
assert solution.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert solution.generateMatrix(1) == [[1]]
print("All sample tests passed.")
