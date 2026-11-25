from collections import deque


class Solution:
    def amountOfTime(self, root, start):
        parent = {}
        start_node = None

        # Build parent links
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.val == start:
                start_node = node

            if node.left:
                parent[node.left] = node
                queue.append(node.left)

            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        # BFS from infected node
        queue = deque([start_node])
        visited = {start_node}
        minutes = -1

        while queue:
            minutes += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                neighbors = [
                    node.left,
                    node.right,
                    parent.get(node)
                ]

                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return minutes
