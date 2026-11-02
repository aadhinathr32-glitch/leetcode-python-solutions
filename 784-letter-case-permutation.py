class Solution:
    def letterCasePermutation(self, s):
        result = []

        def backtrack(index, current):
            if index == len(s):
                result.append("".join(current))
                return

            char = s[index]

            if char.isdigit():
                current.append(char)
                backtrack(index + 1, current)
                current.pop()
            else:
                # Choose lowercase
                current.append(char.lower())
                backtrack(index + 1, current)
                current.pop()

                # Choose uppercase
                current.append(char.upper())
                backtrack(index + 1, current)
                current.pop()

        backtrack(0, [])
        return result


# Sample tests
solution = Solution()

assert set(solution.letterCasePermutation("a1b2")) == {
    "a1b2", "a1B2", "A1b2", "A1B2"
}
assert set(solution.letterCasePermutation("3z4")) == {"3z4", "3Z4"}
assert solution.letterCasePermutation("123") == ["123"]

print("All sample tests passed.")
