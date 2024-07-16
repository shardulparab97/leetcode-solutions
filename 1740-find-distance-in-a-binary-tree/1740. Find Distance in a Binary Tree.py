# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        self.lca = None
        def find_lca(root, p, q):
            if root == None:
                return 0 
            
            l = find_lca(root.left, p, q)
            r = find_lca(root.right, p, q)

            m = root.val == p or root.val == q
            if m + l + r == 2:
                # print("Found LCA")
                self.lca = root
                # print(self.lca.val)

            return m or l or r

        def find_half_distance(root, val):
            if root == None:
                return 0, 0
            if root.val == val:
                return 0, 1

            l = find_half_distance(root.left, val)
            r = find_half_distance(root.right, val)

            dist, has_val = None, None
            if l[1] == 1:
                dist = l[0] + 1
                has_val = 1
            if r[1] == 1:
                dist = r[0] + 1
                has_val = 1
            
            return dist, has_val
        
        find_lca(root, p, q)
        # print(lca.val)
        lp = find_half_distance(self.lca, p)[0]
        rp = find_half_distance(self.lca, q)[0]

        return lp + rp



            