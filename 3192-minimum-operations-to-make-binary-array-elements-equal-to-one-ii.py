class Solution:
    def minOperations(self, nums):
        operations = 0
        current_flip = 0

        for num in nums:
            value = num ^ current_flip

            if value == 0:
                operations += 1
                current_flip ^= 1

        return operations


solution = Solution()
assert solution.minOperations([0, 1, 1, 0, 1]) == 4
assert solution.minOperations([1, 0, 0, 0]) == 1
print("All sample tests passed.")
