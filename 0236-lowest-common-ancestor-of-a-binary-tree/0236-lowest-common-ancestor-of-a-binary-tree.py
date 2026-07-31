# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def has(self, root, node):
        if not root:
            return False
        return root==node or self.has(root.left,node) or self.has(root.right, node)
    def find(self, root, p, q):
        if not root:
            return None
        left, right = self.find(root.left,p,q), self.find(root.right,p,q)
        if left or right:
            return left or right
        if self.has(root, p) and self.has(root, q):
            return root
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)
        