# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                if current:
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)
            if level:
                result.append(level)
        return result
        