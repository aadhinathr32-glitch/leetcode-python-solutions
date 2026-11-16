class Solution:
    def minOperations(self, k):
        answer = k - 1

        for x in range(1, k + 1):
            # Increase 1 to x
            increments = x - 1

            # Number of copies needed to make sum >= k
            copies = (k + x - 1) // x

            # Number of duplicate operations
            duplicates = copies - 1

            operations = increments + duplicates

            answer = min(answer, operations)

        return answer


solution = Solution()
assert solution.minOperations(11) == 5
assert solution.minOperations(1) == 0
print("All sample tests passed.")
