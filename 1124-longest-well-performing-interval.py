class Solution:
    def longestWPI(self, hours):
        prefix = 0
        first_seen = {}
        longest = 0

        for i, hour in enumerate(hours):
            prefix += 1 if hour > 8 else -1

            if prefix > 0:
                longest = i + 1
            elif prefix - 1 in first_seen:
                longest = max(longest, i - first_seen[prefix - 1])

            if prefix not in first_seen:
                first_seen[prefix] = i

        return longest


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestWPI([9, 9, 6, 0, 6, 6, 9]) == 3
    assert solution.longestWPI([6, 6, 6]) == 0

    print("All sample tests passed.")
