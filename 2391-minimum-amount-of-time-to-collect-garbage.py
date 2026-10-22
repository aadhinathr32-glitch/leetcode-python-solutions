"""
LeetCode 2391: Minimum Amount of Time to Collect Garbage

Approach:
1. Every garbage unit takes one minute to collect, so add len(house) for
   every house.
2. Each truck starts at house 0 and only needs to travel as far as the last
   house that contains its garbage type.
3. For each type (M, P, G), find its last house and add the travel time
   required to reach that house.

Time Complexity: O(n + total garbage characters)
Space Complexity: O(1) auxiliary space, excluding input.
"""


class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        # Time spent picking up every unit of garbage.
        total = sum(len(house) for house in garbage)

        # For each truck, add travel time up to its last required house.
        for garbage_type in ("M", "P", "G"):
            for i in range(len(garbage) - 1, -1, -1):
                if garbage_type in garbage[i]:
                    total += sum(travel[:i])
                    break

        return total


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    assert solution.garbageCollection(
        ["G", "P", "GP", "GG"], [2, 4, 3]
    ) == 21

    # Example 2
    assert solution.garbageCollection(
        ["MMM", "PGM", "GP"], [3, 10]
    ) == 37

    print("All sample tests passed.")
