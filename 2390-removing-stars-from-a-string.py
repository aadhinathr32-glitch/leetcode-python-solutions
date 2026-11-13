class Solution:
    def removeStars(self, s):
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


solution = Solution()
assert solution.removeStars("leet**cod*e") == "lecoe"
assert solution.removeStars("erase*****") == ""
print("All sample tests passed.")
