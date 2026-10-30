class Solution:
    def perfectPairs(self, nums):
        nums = sorted(abs(num) for num in nums)

        left = 0
        total = 0

        for right in range(len(values)):
            while nums[right] > 2 * nums[left]:
                left += 1

            total += right - left

        return total


# Sample tests
solution = Solution()

assert solution.perfectPairs([0, 1, 2, 3]) == 2
assert solution.perfectPairs([-3, 2, -1, 4]) == 4
assert solution.perfectPairs([1, 10, 100, 1000]) == 0

print("All sample tests passed.")
