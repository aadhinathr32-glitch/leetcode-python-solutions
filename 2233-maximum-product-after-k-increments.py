class Solution:
    def maximumProduct(self, nums, k):
        MOD = 10**9 + 7

        nums.sort()
        n = len(nums)

        i = 0
        level = nums[0]

        # Raise the smallest elements up to the next value
        while i < n - 1:
            cost = (nums[i + 1] - level) * (i + 1)

            if cost <= k:
                k -= cost
                level = nums[i + 1]
                i += 1
            else:
                break

        # Distribute remaining increments
        q, r = divmod(k, i + 1)

        ans = 1

        # First i+1 elements
        for j in range(i + 1):
            value = level + q

            if j < r:
                value += 1

            ans = (ans * value) % MOD

        # Remaining elements
        for j in range(i + 1, n):
            ans = (ans * nums[j]) % MOD

        return ans
