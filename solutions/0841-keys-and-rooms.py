"""
LeetCode 841: Keys and Rooms
Difficulty: Medium
Topics: Depth-First Search, Breadth-First Search, Graph

Time Complexity: O(n + k), where n is the number of rooms and k is the total number of keys.
Space Complexity: O(n) for the visited set and traversal stack.
"""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [0]

        while stack:
            room = stack.pop()

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == len(rooms)
