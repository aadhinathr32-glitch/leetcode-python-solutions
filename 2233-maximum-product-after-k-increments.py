class Solution:
    def maximumProduct(self, nums, k):
        MOD = 10**9 + 7

        nums.sort()
        n = len(nums)

        i = 0

        # Raise the smallest group until it reaches the next number.
        while i < n - 1:
            diff = nums[i + 1] - nums[i]
            cost = diff * (i + 1)

            if cost <= k:
                k -= cost
                i += 1
            else:
                break

        # Distribute the remaining increments among the smallest group.
        group_size = i + 1
        q = k // group_size
        r = k % group_size

        product = 1

        for j in range(group_size):
            value = nums[i] + q
            if j < r:
                value += 1

            product = (product * value) % MOD

        # The remaining elements are unchanged.
        for j in range(i + 1, n):
            product = (product * nums[j]) % MOD

        return product
