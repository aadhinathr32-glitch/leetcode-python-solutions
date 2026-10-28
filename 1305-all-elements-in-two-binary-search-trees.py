"""
LeetCode 1305: All Elements in Two Binary Search Trees

Perform an inorder traversal of each BST to get two sorted lists, then
merge the lists in ascending order.

Time: O(n + m)
Auxiliary space: O(n + m)
"""


class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root):
            values = []
            stack = []
            node = root

            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left

                node = stack.pop()
                values.append(node.val)
                node = node.right

            return values

        first = inorder(root1)
        second = inorder(root2)

        result = []
        i = j = 0

        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                result.append(first[i])
                i += 1
            else:
                result.append(second[j])
                j += 1

        result.extend(first[i:])
        result.extend(second[j:])
        return result


if __name__ == "__main__":
    class TestNode:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    solution = Solution()

    root1 = TestNode(2, TestNode(1), TestNode(4))
    root2 = TestNode(1, TestNode(0), TestNode(3))
    assert solution.getAllElements(root1, root2) == [0, 1, 1, 2, 3, 4]

    root1 = TestNode(1, None, TestNode(8))
    root2 = TestNode(8, TestNode(1))
    assert solution.getAllElements(root1, root2) == [1, 1, 8, 8]

    assert solution.getAllElements(None, None) == []
    assert solution.getAllElements(TestNode(-5), None) == [-5]

    print("All sample tests passed.")
