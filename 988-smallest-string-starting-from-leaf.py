class Solution:
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if node is None:
                return None

            # Add current character
            path.append(chr(node.val + ord('a')))

            # If this is a leaf, build leaf -> root string
            if node.left is None and node.right is None:
                result = "".join(reversed(path))
                path.pop()
                return result

            left = dfs(node.left, path)
            right = dfs(node.right, path)

            path.pop()

            # Return the lexicographically smaller valid string
            if left is None:
                return right
            if right is None:
                return left

            return min(left, right)

        return dfs(root, [])
