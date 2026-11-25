class Solution:
    def countDigitOccurrences(self, nums, digit):
        count = 0

        for num in nums:
            count += str(num).count(str(digit))

        return count
