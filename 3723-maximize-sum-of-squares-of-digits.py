class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > num * 9:
            return ""

        nines = sum // 9
        remainder = sum % 9

        result = "9" * nines

        if remainder > 0:
            result += str(remainder)

        result += "0" * (num - len(result))

        return result


solution = Solution()
assert solution.maxSumOfSquares(2, 3) == "30"
assert solution.maxSumOfSquares(2, 17) == "98"
assert solution.maxSumOfSquares(1, 10) == ""
assert solution.maxSumOfSquares(3, 27) == "999"
print("All sample tests passed.")
