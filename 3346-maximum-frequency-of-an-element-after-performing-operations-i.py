from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        count = Counter(nums)

        ans = max(count.values())

        # 1. Target is already present in nums.
        # We can use existing occurrences plus at most
        # numOperations other elements within distance k.
        for target, freq in count.items():
            left = bisect_left(nums, target - k)
            right = bisect_right(nums, target + k)

            possible = right - left
            ans = max(ans, freq + min(numOperations, possible - freq))

        # 2. Target is not present.
        # For an optimal target, we can move it to nums[i] + k,
        # where nums[i] is the smallest element in its useful range.
        # Then every element in [nums[i], nums[i] + 2*k] can become target.
        for x in nums:
            left = bisect_left(nums, x)
            right = bisect_right(nums, x + 2 * k)

            possible = right - left
            ans = max(ans, min(possible, numOperations))

        return ans
