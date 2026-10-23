"""
LeetCode 1029: Two City Scheduling
Difficulty: Medium
Topics: Greedy, Sorting

Time Complexity: O(n log n)
Space Complexity: O(log n) auxiliary space for sorting (implementation-dependent).
"""

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by the difference between the cost of city A and city B.
        costs.sort(key=lambda cost: cost[0] - cost[1])

        n = len(costs) // 2

        # Send the first half to city A and the second half to city B.
        total = 0
        for i in range(n):
            total += costs[i][0]

        for i in range(n, len(costs)):
            total += costs[i][1]

        return total
