class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)

        answer = []

        for spell in spells:
            required = (success + spell - 1) // spell

            left = 0
            right = m

            while left < right:
                mid = (left + right) // 2

                if potions[mid] >= required:
                    right = mid
                else:
                    left = mid + 1

            answer.append(m - left)

        return answer


solution = Solution()
assert solution.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
assert solution.successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]
print("All sample tests passed.")
