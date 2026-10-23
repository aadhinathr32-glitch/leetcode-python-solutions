"""LeetCode 78: Subsets.

Build the power set incrementally: for each number, add that number to
every subset already collected.
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result


if __name__ == "__main__":
    solution = Solution()

    actual = solution.subsets([1, 2, 3])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert len(actual) == 8
    assert {tuple(sorted(subset)) for subset in actual} == {
        tuple(sorted(subset)) for subset in expected
    }

    assert solution.subsets([0]) == [[], [0]]
    print("All sample tests passed.")
