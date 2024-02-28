# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        lev = -1
        ans = -1

        q.append((root, 0))
        while q:
            node, l = q.popleft()
            if l > lev:
                lev = l
                ans = node.val

            if node.left:
                q.append((node.left, l+1))
            if node.right:
                q.append((node.right, l+1))
            
        return ans