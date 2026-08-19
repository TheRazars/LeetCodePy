# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        def cur(node, p, q):
            if node is None:
                return None
            if node.val == p or node.val == q:
                return node
            else:
                left = cur(node.left, p, q)
                right = cur(node.right, p, q)
                if left and right:
                    return node
                elif left is None:
                    return right
                else: 
                    return left
        return cur(root, p.val, q.val)
            