class Solution:
    def longestSubsequence(self, arr, difference):
        dp = {}
        longest = 0

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            longest = max(longest, dp[num])

        return longest


solution = Solution()
assert solution.longestSubsequence([1, 2, 3, 4], 1) == 4
assert solution.longestSubsequence([1, 3, 5, 7], 1) == 1
assert solution.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
print("All sample tests passed.")
