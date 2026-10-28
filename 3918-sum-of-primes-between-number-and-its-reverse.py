class Solution:
    def sumOfPrimesInRange(self, n):
        reversed_n = int(str(n)[::-1])
        low = min(n, reversed_n)
        high = max(n, reversed_n)

        total = 0

        for number in range(max(2, low), high + 1):
            is_prime = True

            for divisor in range(2, int(number ** 0.5) + 1):
                if number % divisor == 0:
                    is_prime = False
                    break

            if is_prime:
                total += number

        return total


if __name__ == "__main__":
    solution = Solution()

    assert solution.sumOfPrimesInRange(13) == 132
    assert solution.sumOfPrimesInRange(10) == 17
    assert solution.sumOfPrimesInRange(8) == 0

    print("All sample tests passed.")
