class Solution:
    def checkMove(self, board, rMove, cMove, color):
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # down-right
            (1, -1),  # down-left
            (-1, 1),  # up-right
            (-1, -1)  # up-left
        ]

        opponent = 'W' if color == 'B' else 'B'

        for dr, dc in directions:
            r = rMove + dr
            c = cMove + dc
            count = 0

            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                count += 1
                r += dr
                c += dc

            if count >= 1 and 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == color:
                    return True

        return False

solution = Solution()
board1 = [
    [".", ".", ".", "B", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."],
    ["W", "B", "B", ".", "W", "W", "W", "B"],
    [".", ".", ".", "B", ".", ".", ".", "."],
    [".", ".", ".", "B", ".", ".", ".", "."],
    [".", ".", ".", "W", ".", ".", ".", "."]
]
board2 = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", "B", ".", ".", "W", ".", ".", "."],
    [".", ".", "W", ".", ".", ".", ".", "."],
    [".", ".", ".", "W", "B", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "B", "W", ".", "."],
    [".", ".", ".", ".", ".", ".", "W", "."],
    [".", ".", ".", ".", ".", ".", ".", "B"]
]
assert solution.checkMove(board1, 4, 3, "B") is True
assert solution.checkMove(board2, 4, 4, "W") is False
print("All sample tests passed.")
