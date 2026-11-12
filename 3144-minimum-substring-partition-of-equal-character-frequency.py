class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            freq = [0] * 26
            max_freq = 0
            distinct = 0

            for j in range(i, n):
                index = ord(s[j]) - ord('a')

                if freq[index] == 0:
                    distinct += 1

                freq[index] += 1
                max_freq = max(max_freq, freq[index])

                length = j - i + 1

                if length == distinct * max_freq:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)

        return dp[n]


solution = Solution()

assert solution.minimumSubstringsInPartition("fabccddg") == 3
assert solution.minimumSubstringsInPartition("abababaccddb") == 2

print("All sample tests passed.")
