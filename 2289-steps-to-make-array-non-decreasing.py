"""
LeetCode 2289: Steps to Make Array Non-decreasing

Use a monotonic stack. Each stack entry stores (value, steps_needed).
When the current value is at least the stack top, pop smaller/equal values
and keep the maximum steps among them. If a larger value remains, the
current element needs one additional step to be removed.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def totalSteps(self, nums):
        stack = []
        max_steps = 0

        for num in nums:
            steps = 0

            while stack and stack[-1][0] <= num:
                steps = max(steps, stack.pop()[1])

            if stack:
                steps += 1
            else:
                steps = 0

            max_steps = max(max_steps, steps)
            stack.append((num, steps))

        return max_steps


if __name__ == "__main__":
    solution = Solution()

    assert solution.totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]) == 3
    assert solution.totalSteps([4, 5, 7, 7, 13]) == 0
    assert solution.totalSteps([10, 1, 2, 3, 4, 5, 6, 7]) == 1

    print("All sample tests passed.")
