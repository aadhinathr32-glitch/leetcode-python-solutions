class Solution:
    def minOperations(self, nums):
        n = len(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # If 1 already exists, spread it to all other elements.
        ones = nums.count(1)

        if ones > 0:
            return n - ones

        # Find the shortest subarray whose GCD is 1.
        min_length = n + 1

        for i in range(n):
            current_gcd = 0

            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])

                if current_gcd == 1:
                    min_length = min(min_length, j - i + 1)
                    break

        # Impossible to create a 1.
        if min_length == n + 1:
            return -1

        # min_length - 1 operations to create the first 1
        # and n - 1 operations to spread it.
        return (min_length - 1) + (n - 1)


solution = Solution()
assert solution.minOperations([2, 6, 3, 4]) == 4
assert solution.minOperations([2, 10, 6, 14]) == -1
assert solution.minOperations([1, 2, 3]) == 2
print("All sample tests passed.")
