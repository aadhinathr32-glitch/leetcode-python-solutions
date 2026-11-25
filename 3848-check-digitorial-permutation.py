class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        total = 0

        for digit in str(n):
            total += factorial[int(digit)]

        # The factorial sum must contain exactly the same digits as n.
        # If so, it can be rearranged into a valid permutation.
        return sorted(str(total)) == sorted(str(n))
