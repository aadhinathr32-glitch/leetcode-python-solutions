"""LeetCode 1029: Two City Scheduling

Sort people by the difference between their city A and city B costs.
Send the n people with the greatest relative advantage for city A to A,
and send the remaining n people to B.

Time: O(n log n)
Auxiliary space: O(n) for the sorted copy.
"""


class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs = sorted(costs, key=lambda cost: cost[0] - cost[1])
        n = len(costs) // 2

        total = 0
        for i in range(n):
            total += costs[i][0]

        for i in range(n, len(costs)):
            total += costs[i][1]

        return total


if __name__ == "__main__":
    solution = Solution()
    assert solution.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
    assert solution.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859
    assert solution.twoCitySchedCost([[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086
    print("All sample tests passed.")
