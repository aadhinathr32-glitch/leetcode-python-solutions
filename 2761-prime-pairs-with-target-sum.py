class Solution:
    def findPrimePairs(self, n):
        # Sieve of Eratosthenes
        is_prime = [True] * (n + 1)

        if n >= 0:
            is_prime[0] = False
        if n >= 1:
            is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1

        result = []

        for x in range(2, n // 2 + 1):
            y = n - x

            if is_prime[x] and is_prime[y]:
                result.append([x, y])

        return result


solution = Solution()

assert solution.findPrimePairs(10) == [[3, 7], [5, 5]]
assert solution.findPrimePairs(2) == []

print("All sample tests passed.")
