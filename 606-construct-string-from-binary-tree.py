class Solution:
    def tree2str(self, root):
        if root is None:
            return ""

        # Leaf node
        if root.left is None and root.right is None:
            return str(root.val)

        # Only right child exists
        if root.left is None:
            return str(root.val) + "()(" + self.tree2str(root.right) + ")"

        # Only left child exists
        if root.right is None:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"

        # Both children exist
        return (
            str(root.val)
            + "(" + self.tree2str(root.left) + ")"
            + "(" + self.tree2str(root.right) + ")"
        )


if __name__ == "__main__":
    class TestNode:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    solution = Solution()

    root = TestNode(1, TestNode(2, TestNode(4)), TestNode(3))
    assert solution.tree2str(root) == "1(2(4))(3)"

    root = TestNode(1, TestNode(2, None, TestNode(4)), TestNode(3))
    assert solution.tree2str(root) == "1(2()(4))(3)"

    print("All sample tests passed.")
