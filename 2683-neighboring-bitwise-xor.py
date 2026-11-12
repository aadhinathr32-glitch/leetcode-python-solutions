class Solution:
    def doesValidArrayExist(self, derived):
        xor_sum = 0

        for value in derived:
            xor_sum ^= value

        return xor_sum == 0


solution = Solution()
assert solution.doesValidArrayExist([1, 1, 0]) is True
assert solution.doesValidArrayExist([1, 1]) is True
assert solution.doesValidArrayExist([1, 0]) is False
print("All sample tests passed.")
