# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def tree(node, remain):
            if node is None:
                return False
            if node.left == None and node.right == None:
                return node.val == remain
            return tree(node.left, remain - node.val) or tree(node.right, remain - node.val)
        return tree(root, targetSum)