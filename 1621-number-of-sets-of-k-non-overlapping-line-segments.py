class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # The answer is C(n + k - 1, 2k).
        top = n + k - 1
        factorial = [1] * (top + 1)

        for i in range(1, top + 1):
            factorial[i] = factorial[i - 1] * i % MOD

        def mod_inverse(value):
            return pow(value, MOD - 2, MOD)

        numerator = factorial[top]
        denominator = factorial[2 * k] * factorial[top - 2 * k] % MOD

        return numerator * mod_inverse(denominator) % MOD


if __name__ == "__main__":
    solution = Solution()

    assert solution.numberOfSets(4, 2) == 5
    assert solution.numberOfSets(3, 1) == 3
    assert solution.numberOfSets(30, 7) == 796297179

    print("All sample tests passed.")
