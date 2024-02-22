# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root == None:
            return (0, 0)
        
        if root.left == 0 and root.right == 0:
            return (0, 0)
        
        ld, lh = self.solve(root.left)
        rd, rh = self.solve(root.right)

        md = max(ld, rd, 2 + lh + rh)
        mh = 1 + max(lh, rh)

        return (md, mh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return both d and h
        return self.solve(root)[0]-2
