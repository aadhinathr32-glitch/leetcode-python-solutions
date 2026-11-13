class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        n = len(stones)

        # Maximum number of moves
        max_moves = max(
            stones[n - 2] - stones[0],
            stones[n - 1] - stones[1]
        ) - (n - 2)

        # Minimum number of moves using a sliding window
        min_moves = n
        left = 0

        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1

            count = right - left + 1

            # Special case:
            # n-1 stones are consecutive and the remaining stone
            # is too far away to be moved normally.
            if count == n - 1 and stones[right] - stones[left] == n - 2:
                moves = 2
            else:
                moves = n - count

            min_moves = min(min_moves, moves)

        return [min_moves, max_moves]


solution = Solution()
assert solution.numMovesStonesII([7, 4, 9]) == [1, 2]
assert solution.numMovesStonesII([6, 5, 4, 3, 10]) == [2, 3]
print("All sample tests passed.")
