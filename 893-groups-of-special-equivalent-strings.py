class Solution:
    def numSpecialEquivGroups(self, words):
        groups = set()

        for word in words:
            even = sorted(word[::2])
            odd = sorted(word[1::2])

            signature = (tuple(even), tuple(odd))
            groups.add(signature)

        return len(groups)


if __name__ == "__main__":
    solution = Solution()

    assert solution.numSpecialEquivGroups(
        ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    ) == 3
    assert solution.numSpecialEquivGroups(
        ["abc", "acb", "bac", "bca", "cab", "cba"]
    ) == 3

    print("All sample tests passed.")
