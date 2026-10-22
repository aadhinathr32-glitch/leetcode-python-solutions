"""
LeetCode 449: Serialize and Deserialize BST

Use preorder traversal (root, left, right). Since the input is a BST,
the values and BST ordering rules are enough to reconstruct the tree, so
there is no need to encode null children.

Serialization time: O(n)
Deserialization time: O(n)
Encoded space: O(n); recursion stack: O(h)
"""


# LeetCode provides the TreeNode definition.
class Codec:

    def serialize(self, root):
        values = []

        def preorder(node):
            if node is None:
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data):
        if not data:
            return None

        values = list(map(int, data.split(",")))
        index = [0]

        def build(lower, upper):
            if index[0] >= len(values):
                return None

            value = values[index[0]]
            if value < lower or value > upper:
                return None

            index[0] += 1
            node = TreeNode(value)
            node.left = build(lower, value)
            node.right = build(value, upper)
            return node

        return build(float("-inf"), float("inf"))
