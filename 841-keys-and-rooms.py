"""LeetCode 841: Keys and Rooms

Approach:
Start in room 0 and use a stack to explore every room whose key we have.
Whenever a room is visited, collect its keys and add any unvisited rooms to
the stack. If the number of visited rooms equals the total number of rooms,
all rooms are reachable.

Time: O(n + k), where n is the number of rooms and k is the total number of keys.
Auxiliary space: O(n) for the stack and visited set.
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {0}
        stack = [0]

        while stack:
            room = stack.pop()

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == len(rooms)


if __name__ == "__main__":
    solution = Solution()
    assert solution.canVisitAllRooms([[1], [2], [3], []]) is True
    assert solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) is False
    print("All sample tests passed.")
