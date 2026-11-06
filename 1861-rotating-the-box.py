class Solution:
    def rotateTheBox(self, boxGrid):
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Let stones fall to the right.
        for r in range(m):
            empty = n - 1

            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '*':
                    empty = c - 1

                elif boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty] = '#'
                    empty -= 1

        # Rotate the box 90 degrees clockwise.
        result = [[None] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                result[c][m - 1 - r] = boxGrid[r][c]

        return result


solution = Solution()

assert solution.rotateTheBox([["#", ".", "#"]]) == [["."], ["#"], ["#"]]

assert solution.rotateTheBox([
    ["#", ".", "*", "."],
    ["#", "#", "*", "."]
]) == [
    ["#", "."],
    ["#", "#"],
    ["*", "*"],
    [".", "."]
]

assert solution.rotateTheBox([
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."]
]) == [
    [".", "#", "#"],
    [".", "#", "#"],
    ["#", "#", "*"],
    ["#", "*", "."],
    ["#", ".", "*"],
    ["#", ".", "."]
]

print("All sample tests passed.")
