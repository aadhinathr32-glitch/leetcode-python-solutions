import heapq


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        min_heap = []

        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]

            if climb > 0:
                heapq.heappush(min_heap, climb)

            if len(min_heap) > ladders:
                bricks -= heapq.heappop(min_heap)

            if bricks < 0:
                return i

        return len(heights) - 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.furthestBuilding(
        [4, 2, 7, 6, 9, 14, 12], 5, 1
    ) == 4

    assert solution.furthestBuilding(
        [4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2
    ) == 7

    assert solution.furthestBuilding([14, 3, 19, 3], 17, 0) == 3

    print("All sample tests passed.")
