class Solution:
    def countPerfectPairs(self, nums):
        values = sorted(abs(num) for num in nums)

        left = 0
        total = 0

        for right in range(len(values)):
            while values[right] > 2 * values[left]:
                left += 1

            total += right - left

        return total


# Sample tests
solution = Solution()

assert solution.countPerfectPairs([0, 1, 2, 3]) == 2
assert solution.countPerfectPairs([-3, 2, -1, 4]) == 4
assert solution.countPerfectPairs([1, 10, 100, 1000]) == 0

print("All sample tests passed.")
