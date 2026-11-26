from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        count = Counter(nums)

        ans = 0

        # Try every possible target value
        for target in range(100001):
            left = bisect_left(nums, target - k)
            right = bisect_right(nums, target + k)

            # Elements that can become target
            possible = right - left

            # Elements already equal to target
            already = count[target]

            # Remaining elements need an operation
            need = possible - already

            frequency = already + min(need, numOperations)

            ans = max(ans, frequency)

        return ans
