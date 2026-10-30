class Solution:
    def canConstruct(self, s, k):
        if len(s) < k:
            return False

        frequencies = [0] * 26

        for char in s:
            frequencies[ord(char) - ord('a')] += 1

        odd_count = 0

        for frequency in frequencies:
            if frequency % 2 != 0:
                odd_count += 1

        return odd_count <= k


# Sample tests
solution = Solution()

assert solution.canConstruct("annabelle", 2) is True
assert solution.canConstruct("leetcode", 3) is False
assert solution.canConstruct("true", 4) is True

print("All sample tests passed.")
