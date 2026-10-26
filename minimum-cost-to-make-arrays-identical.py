"""Minimum Cost to Make Arrays Identical.

Free swaps within either array let us reorder each array arbitrarily.
For every value, the final arrays must each contain half of its total
occurrences across both arrays. If any combined frequency is odd, this
is impossible. Otherwise, each cross-array swap can fix one surplus
occurrence in nums1, so the answer is the total surplus.

Time: O(n)
Auxiliary space: O(u), where u is the number of distinct values.
"""

from collections import Counter


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        combined = count1 + count2

        if any(count % 2 for count in combined.values()):
            return -1

        cost = 0
        for value, total_count in combined.items():
            target = total_count // 2
            cost += max(0, count1[value] - target)

        return cost


if __name__ == "__main__":
    solution = Solution()
    assert solution.minCost([10, 20], [20, 10]) == 0
    assert solution.minCost([10, 10], [20, 20]) == 1
    assert solution.minCost([10, 20], [30, 40]) == -1
    print("All sample tests passed.")
