class Solution:
    def minRemoval(self, nums, k):
        nums.sort()

        n = len(nums)
        left = 0
        max_balanced = 1

        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1

            max_balanced = max(max_balanced, right - left + 1)

        return n - max_balanced


solution = Solution()
assert solution.minRemoval([2, 1, 5], 2) == 1
assert solution.minRemoval([1, 6, 2, 9], 3) == 2
assert solution.minRemoval([4, 6], 2) == 0
print("All sample tests passed.")
