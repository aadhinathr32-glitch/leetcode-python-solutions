class Solution:
    def countDays(self, days, meetings):
        meetings.sort()

        covered = 0
        start, end = meetings[0]

        for i in range(1, len(meetings)):
            current_start, current_end = meetings[i]

            if current_start <= end + 1:
                end = max(end, current_end)
            else:
                covered += end - start + 1
                start = current_start
                end = current_end

        covered += end - start + 1

        return days - covered


solution = Solution()

assert solution.countDays(10, [[5, 7], [1, 3], [9, 10]]) == 2
assert solution.countDays(5, [[2, 4], [1, 3]]) == 1
assert solution.countDays(6, [[1, 6]]) == 0

print("All sample tests passed.")
