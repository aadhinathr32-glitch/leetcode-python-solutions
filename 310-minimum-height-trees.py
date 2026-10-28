from collections import deque


class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque(i for i in range(n) if len(graph[i]) == 1)
        remaining = n

        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)


if __name__ == "__main__":
    solution = Solution()

    assert solution.findMinHeightTrees(
        4, [[1, 0], [1, 2], [1, 3]]
    ) == [1]

    assert set(solution.findMinHeightTrees(
        6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    )) == {3, 4}

    assert solution.findMinHeightTrees(1, []) == [0]

    print("All sample tests passed.")
}
