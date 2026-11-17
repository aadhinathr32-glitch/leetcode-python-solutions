class Solution:
    def getSmallestString(self, s, k):
        result = []

        for ch in s:
            current = ord(ch) - ord('a')

            # Minimum cyclic distance from ch to 'a'
            cost = min(current, 26 - current)

            if cost <= k:
                result.append('a')
                k -= cost
            else:
                # Move towards 'a' using the remaining budget.
                # Moving backward gives the smallest possible character.
                if current <= k:
                    result.append('a')
                    k -= current
                else:
                    result.append(chr(ord('a') + current - k))
                    k = 0

        return ''.join(result)


solution = Solution()
assert solution.getSmallestString("zbbz", 3) == "aaaz"
assert solution.getSmallestString("xaxcd", 4) == "aawcd"
assert solution.getSmallestString("lol", 0) == "lol"
print("All sample tests passed.")
