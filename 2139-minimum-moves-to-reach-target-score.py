"""
LeetCode 2139: Minimum Moves to Reach Target Score

Work backward from target. If the current target is even and doubles remain,
reverse a doubling by dividing by two. Otherwise, reverse an increment by
subtracting one. When no doubles remain, all remaining moves are increments.

Time: O(log target)
Auxiliary space: O(1)
"""


class Solution:
    def minMoves(self, target, maxDoubles):
        moves = 0

        while target > 1:
            if maxDoubles == 0:
                moves += target - 1
                break

            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1

            moves += 1

        return moves


if __name__ == "__main__":
    solution = Solution()

    assert solution.minMoves(5, 0) == 4
    assert solution.minMoves(19, 2) == 7
    assert solution.minMoves(10, 4) == 4
    assert solution.minMoves(1, 0) == 0

    print("All sample tests passed.")
