from collections import Counter


class Solution:
    def minCost(self, nums1, nums2):
        count1 = Counter(nums1)
        total = count1 + Counter(nums2)

        # Each value must occur an even number of times overall.
        for count in total.values():
            if count % 2:
                return -1

        # Each array must end up with half of every value's occurrences.
        # Every surplus value in nums1 needs one paid cross-array swap.
        cost = 0
        for value, count in count1.items():
            target = total[value] // 2
            if count > target:
                cost += count - target

        return cost


# Sample tests
solution = Solution()
assert solution.minCost([10, 20], [20, 10]) == 0
assert solution.minCost([10, 10], [20, 20]) == 1
assert solution.minCost([10, 20], [30, 40]) == -1

print("All sample tests passed.")
