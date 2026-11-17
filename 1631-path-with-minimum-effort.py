import heapq


class Solution:
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        heap = [(0, 0, 0)]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while heap:
            effort, row, col = heapq.heappop(heap)

            if effort > efforts[row][col]:
                continue

            if row == rows - 1 and col == cols - 1:
                return effort

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(
                        effort,
                        abs(heights[row][col] - heights[nr][nc])
                    )

                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return 0


solution = Solution()

assert solution.minimumEffortPath(
    [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
) == 2

assert solution.minimumEffortPath(
    [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
) == 1

assert solution.minimumEffortPath(
    [[1, 2, 1, 1, 1],
     [1, 2, 1, 2, 1],
     [1, 2, 1, 2, 1],
     [1, 2, 1, 2, 1],
     [1, 1, 1, 2, 1]]
) == 0

print("All sample tests passed.")
