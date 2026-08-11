# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def count_depth(root):
            if root is None:
                return 0
            if not (root.right or root.left):
                return 1
            else:
                return 1 + max(count_depth(root.right), count_depth(root.left))
        
        return count_depth(root)