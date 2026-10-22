"""
LeetCode 1155: Number of Dice Rolls With Target Sum

Dynamic programming:
dp[s] stores the number of ways to make sum s using the dice processed
so far. For each new die, try each face from 1 through k.

Time Complexity: O(n * target * k)
Space Complexity: O(target)
"""


class Solution:
    def numRollsToTarget(self, n, k, target):
        MOD = 10**9 + 7

        dp = [0] * (target + 1)
        dp[0] = 1

        for _ in range(n):
            next_dp = [0] * (target + 1)

            for current_sum in range(target + 1):
                if dp[current_sum] == 0:
                    continue

                for face in range(1, k + 1):
                    new_sum = current_sum + face
                    if new_sum <= target:
                        next_dp[new_sum] = (
                            next_dp[new_sum] + dp[current_sum]
                        ) % MOD

            dp = next_dp

        return dp[target]


if __name__ == "__main__":
    solution = Solution()

    assert solution.numRollsToTarget(1, 6, 3) == 1
    assert solution.numRollsToTarget(2, 6, 7) == 6
    assert solution.numRollsToTarget(30, 30, 500) == 222616187

    print("All sample tests passed.")
