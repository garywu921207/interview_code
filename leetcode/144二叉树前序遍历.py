# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def pre_order_recursive(root):
            if not root:
                return
            res.append(root.val)
            pre_order_recursive(root.left)
            pre_order_recursive(root.right)

        res = []
        pre_order_recursive(root)
        return res
