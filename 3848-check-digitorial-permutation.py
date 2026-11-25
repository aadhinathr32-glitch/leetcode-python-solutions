class Solution:
    def isDigitorialPermutation(self, n):
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        total = 0

        for digit in str(n):
            total += factorial[int(digit)]

        # A permutation of n is digitorial if its value is equal
        # to the sum of the factorials of its digits.
        # The sum depends only on the digits, not their order.
        # So total must contain exactly the same digits as n.
        return sorted(str(total)) == sorted(str(n))
