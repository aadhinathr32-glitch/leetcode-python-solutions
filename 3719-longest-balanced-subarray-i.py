class Solution:
    def longestBalanced(self, nums):
        max_length = 0

        for i in range(len(nums)):
            even = set()
            odd = set()

            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(even) == len(odd):
                    max_length = max(max_length, j - i + 1)

        return max_length


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestBalanced([2, 5, 4, 3]) == 4
    assert solution.longestBalanced([3, 2, 2, 5, 4]) == 5
    assert solution.longestBalanced([1, 2, 3, 2]) == 3

    print("All sample tests passed.")
