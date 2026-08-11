# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest = float("inf")

        def traverse(root):
            if root.val < p.val and root.val < q.val:
                return traverse(root.right)
            if root.val > p.val and root.val > q.val:
                return traverse(root.left)
            else:
                return root
        
        return traverse(root)