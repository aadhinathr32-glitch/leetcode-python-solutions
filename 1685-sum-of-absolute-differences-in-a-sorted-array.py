"""LeetCode 1685: Sum of Absolute Differences in a Sorted Array

Approach:
Because nums is sorted, elements to the left are <= nums[i] and elements
to the right are >= nums[i]. Prefix sums let us calculate both sides
without repeatedly scanning the array.

For index i and value x:
- left  = x * i - prefix_sum
- right = (total_sum - prefix_sum - x) - x * (n - i - 1)

Time: O(n)
Auxiliary space: O(n) for the result array.
"""


class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        total = sum(nums)
        prefix = 0
        result = []

        for i, num in enumerate(nums):
            left = num * i - prefix
            right = (total - prefix - num) - num * (n - i - 1)

            result.append(left + right)
            prefix += num

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.getSumAbsoluteDifferences([2, 3, 5]) == [4, 3, 5]
    assert solution.getSumAbsoluteDifferences([1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]
    print("All sample tests passed.")
