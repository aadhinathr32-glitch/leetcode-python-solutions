class Solution:
    def maxArea(self, mat):
        m = len(mat)
        n = len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                    + (mat[i][j] == 0)
                )

        def is_square(r, c, k):
            zeroes = (
                prefix[r + k][c + k]
                - prefix[r][c + k]
                - prefix[r + k][c]
                + prefix[r][c]
            )
            return zeroes == 0

        for k in range(min(m, n), 0, -1):
            squares = []

            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_square(i, j, k):
                        squares.append((i, j))

            for a in range(len(squares)):
                r1, c1 = squares[a]

                for b in range(a + 1, len(squares)):
                    r2, c2 = squares[b]

                    if (
                        r1 + k <= r2
                        or r2 + k <= r1
                        or c1 + k <= c2
                        or c2 + k <= c1
                    ):
                        return k * k

        return 0
