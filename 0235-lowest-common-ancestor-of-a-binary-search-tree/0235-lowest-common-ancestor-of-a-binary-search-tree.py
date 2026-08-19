# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tree = root
        while tree:
            if p.val > tree.val and q.val > tree.val:
                tree = tree.right
            elif p.val < tree.val and q.val < tree.val:
                tree = tree.left
            else:
                return tree