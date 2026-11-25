class Solution:
    def isDigitorialPermutation(self, n):
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        digits = str(n)
        total = 0

        for digit in digits:
            total += factorial[int(digit)]

        return total == n
