class Solution:
    def minimumOperationsToWriteY(self, grid):
        n = len(grid)
        mid = n // 2
        y_count = [0, 0, 0]
        other_count = [0, 0, 0]

        for r in range(n):
            for c in range(n):
                belongs_to_y = (
                    (r <= mid and (r == c or r + c == n - 1))
                    or (r > mid and c == mid)
                )

                if belongs_to_y:
                    y_count[grid[r][c]] += 1
                else:
                    other_count[grid[r][c]] += 1

        best = float("inf")
        for y_value in range(3):
            for other_value in range(3):
                if y_value != other_value:
                    changes = (
                        sum(y_count) - y_count[y_value]
                        + sum(other_count) - other_count[other_value]
                    )
                    best = min(best, changes)

        return best


if __name__ == "__main__":
    solution = Solution()

    assert solution.minimumOperationsToWriteY(
        [[1, 2, 2], [1, 1, 0], [0, 1, 0]]
    ) == 3

    assert solution.minimumOperationsToWriteY(
        [
            [0, 1, 0, 1, 0],
            [2, 1, 0, 1, 2],
            [2, 2, 2, 0, 1],
            [2, 2, 2, 2, 2],
            [2, 1, 2, 2, 2],
        ]
    ) == 12

    print("All sample tests passed.")
}
