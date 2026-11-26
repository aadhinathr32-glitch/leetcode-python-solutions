from bisect import bisect_left, bisect_right
from collections import Counter


class Solution:
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        count = Counter(nums)

        ans = 0

        # Try every possible target value
        for target in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, target - k)
            right = bisect_right(nums, target + k)

            # Elements that can become target
            while nums[right - 1] - nums[left] > 2 * k:
                left += 1

            window = right - left

            # If target is not an existing value,
            # every element needs one operation.
            ans = max(ans, min(window, numOperations))

        # Check every value that already exists.
        # Existing elements do not need an operation.
        for target in count:
            left = bisect_left(nums, target - k)
            right = bisect_right(nums, target + k)

            possible = right - left

            frequency = min(
                possible,
                count[target] + numOperations
            )

            ans = max(ans, frequency)

        return ans
