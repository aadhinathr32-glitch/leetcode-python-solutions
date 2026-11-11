class Solution:
    def sumDigitDifferences(self, nums):
        n = len(nums)
        digits = len(str(nums[0]))
        answer = 0

        for pos in range(digits):
            count = [0] * 10

            for num in nums:
                digit = (num // (10 ** pos)) % 10
                count[digit] += 1

            for c in count:
                answer += c * (n - c)

        return answer // 2


solution = Solution()
assert solution.sumDigitDifferences([13, 23, 12]) == 4
assert solution.sumDigitDifferences([10, 10, 10, 10]) == 0
print("All sample tests passed.")
