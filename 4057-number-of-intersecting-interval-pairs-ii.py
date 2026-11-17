from bisect import bisect_left


class Solution:
    def countIntersectingIntervals(self, intervals):
        intervals.sort()

        temoravlin = intervals

        starts = [start for start, _ in intervals]
        answer = 0

        for i, (_, end) in enumerate(temoravlin):
            # Every later interval whose start <= end intersects this interval.
            first_non_intersecting = bisect_left(starts, end + 1, i + 1)
            answer += first_non_intersecting - i - 1

        return answer


solution = Solution()
assert solution.countIntersectingIntervals([[1, 2], [2, 3], [3, 4]]) == 2
assert solution.countIntersectingIntervals([[1, 5], [2, 4], [3, 6]]) == 3
assert solution.countIntersectingIntervals([[1, 2], [3, 4], [5, 6]]) == 0
print("All sample tests passed.")
