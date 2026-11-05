class Solution:
    def kthFactor(self, n, k):
        factors = []

        # Find factors up to sqrt(n)
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)

                if i != n // i:
                    factors.append(n // i)

        # Sort all factors
        factors.sort()

        if k <= len(factors):
            return factors[k - 1]

        return -1


solution = Solution()
assert solution.kthFactor(12, 3) == 3
assert solution.kthFactor(7, 2) == 7
assert solution.kthFactor(4, 4) == -1
print("All sample tests passed.")
