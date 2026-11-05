class Solution:
    def minOperations(self, nums):
        max_value = max(nums) + 100

        # Sieve of Eratosthenes
        is_prime = [True] * (max_value + 1)
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(max_value ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_value + 1, i):
                    is_prime[j] = False

        # Store all prime numbers
        primes = []

        for i in range(2, max_value + 1):
            if is_prime[i]:
                primes.append(i)

        operations = 0

        for i in range(len(nums)):
            value = nums[i]

            if i % 2 == 0:
                # Even index must be prime
                if is_prime[value]:
                    continue

                # Find the smallest prime greater than value
                left = 0
                right = len(primes) - 1

                while left < right:
                    mid = (left + right) // 2

                    if primes[mid] >= value:
                        right = mid
                    else:
                        left = mid + 1

                operations += primes[left] - value

            else:
                # Odd index must be non-prime
                if not is_prime[value]:
                    continue

                # 2 -> 3 -> 4 requires 2 operations.
                # Any other prime becomes non-prime after +1.
                if value == 2:
                    operations += 2
                else:
                    operations += 1

        return operations


solution = Solution()
assert solution.minOperations([1, 2, 3, 4]) == 3
assert solution.minOperations([5, 6, 7, 8]) == 0
assert solution.minOperations([4, 4]) == 1
print("All sample tests passed.")
