class Solution:
    def kClosest(self, points, k):
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)

        return points[:k]


solution = Solution()
assert solution.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
assert solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
print("All sample tests passed.")
