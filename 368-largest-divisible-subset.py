from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        # dp[i] = length of the largest divisible subset ending at nums[i].
        dp = [1] * n
        parent = [-1] * n
        best_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > dp[best_index]:
                best_index = i

        # Reconstruct the subset by following parent links.
        result = []
        while best_index != -1:
            result.append(nums[best_index])
            best_index = parent[best_index]

        return result[::-1]


# Sample tests
solution = Solution()

result1 = solution.largestDivisibleSubset([1, 2, 3])
assert result1 in ([1, 2], [1, 3], [2, 3])

assert solution.largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]

print("All sample tests passed.")
