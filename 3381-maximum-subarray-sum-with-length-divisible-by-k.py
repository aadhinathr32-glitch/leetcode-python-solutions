class Solution:
    def maxSubarraySum(self, nums, k):
        # min_prefix[r] = smallest prefix sum
        # seen at an index whose index % k == r
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0

        prefix_sum = 0
        answer = float('-inf')

        for i, num in enumerate(nums, 1):
            prefix_sum += num

            remainder = i % k

            if min_prefix[remainder] != float('inf'):
                answer = max(answer, prefix_sum - min_prefix[remainder])

            min_prefix[remainder] = min(
                min_prefix[remainder],
                prefix_sum
            )

        return answer


solution = Solution()
assert solution.maxSubarraySum([1, 2], 1) == 3
assert solution.maxSubarraySum([-1, -2, -3, -4, -5], 4) == -10
assert solution.maxSubarraySum([-5, 1, 2, -3, 4], 2) == 4
print("All sample tests passed.")
