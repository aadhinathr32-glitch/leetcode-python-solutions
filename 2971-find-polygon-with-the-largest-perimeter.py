class Solution:
    def largestPerimeter(self, nums):
        nums.sort()

        total = sum(nums)

        for i in range(len(nums) - 1, 1, -1):
            # nums[i] is the largest side
            if total - nums[i] > nums[i]:
                return total

            total -= nums[i]

        return -1
