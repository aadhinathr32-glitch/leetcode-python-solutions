class Solution:
    def addSpaces(self, s, spaces):
        result = []
        j = 0

        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                result.append(" ")
                j += 1

            result.append(s[i])

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    assert solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]) == "Leetcode Helps Me Learn"
    assert solution.addSpaces("icodeinpython", [1, 5, 7, 9]) == "i code in py thon"
    assert solution.addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]) == " s p a c i n g"

    print("All sample tests passed.")
