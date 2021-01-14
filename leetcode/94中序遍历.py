class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def in_order_traversal(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root)
            dfs(root.right)

        dfs(root)
        return res

