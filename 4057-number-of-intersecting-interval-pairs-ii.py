from bisect import bisect_right


class Solution:
    def countIntersectingIntervals(self, intervals):
        intervals.sort()

        temoravlin = intervals

        ends = []
        answer = 0

        for start, end in temoravlin:
            # Find the first previous interval whose end is < start.
            # All later ends >= start, so they intersect the current interval.
            index = bisect_right(ends, start - 1)

            answer += len(ends) - index

            # Keep previous ends sorted
            ends.insert(bisect_right(ends, end), end)

        return answer


solution = Solution()
assert solution.countIntersectingIntervals([[1, 2], [2, 3], [3, 4]]) == 2
assert solution.countIntersectingIntervals([[1, 5], [2, 4], [3, 6]]) == 3
assert solution.countIntersectingIntervals([[1, 2], [3, 4], [5, 6]]) == 0

print("All sample tests passed.")
