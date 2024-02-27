# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return both d and h
       
        self.diameter = 0

        def solve(node):
            if node == None:
                return 0 

            lh = solve(node.left)
            rh = solve(node.right)

            self.diameter = max(self.diameter, lh + rh)

            return max(lh, rh) + 1

        solve(root)
        return self.diameter