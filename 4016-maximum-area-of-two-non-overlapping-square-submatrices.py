class Solution:
    def maxArea(self, mat):
        m = len(mat)
        n = len(mat[0])

        # Build prefix sum of zero cells.
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                    + (mat[i][j] == 0)
                )

        def is_square_ones(r, c, k):
            zeros = (
                prefix[r + k][c + k]
                - prefix[r][c + k]
                - prefix[r + k][c]
                + prefix[r][c]
            )
            return zeros == 0

        def can_make_two(k):
            min_row = m
            max_row = -1
            min_col = n
            max_col = -1

            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_square_ones(r, c, k):
                        min_row = min(min_row, r)
                        max_row = max(max_row, r)
                        min_col = min(min_col, c)
                        max_col = max(max_col, c)

            if max_row == -1:
                return False

            return (max_row - min_row >= k) or (max_col - min_col >= k)

        left = 1
        right = min(m, n)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if can_make_two(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer * answer
