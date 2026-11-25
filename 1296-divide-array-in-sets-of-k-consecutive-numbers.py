class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        nums.sort()

        for num in nums:
            if count[num] == 0:
                continue

            for x in range(num, num + k):
                if count.get(x, 0) == 0:
                    return False

                count[x] -= 1

        return True
