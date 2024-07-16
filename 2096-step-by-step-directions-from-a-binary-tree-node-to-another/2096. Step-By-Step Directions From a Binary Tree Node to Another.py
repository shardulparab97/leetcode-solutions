# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.lca = None
        def get_lca(root):
            if root == None:
                return 0 

            l = get_lca(root.left)
            r = get_lca(root.right)

            m = root.val == startValue or root.val == destValue

            if m + l + r == 2:
                self.lca = root
            
            return m or l or r

        get_lca(root)

        first_half, second_half = "", ""

        # def get_first_half(root):
        #     if root == None:
        #         return ""
            
        #     if root.val == startValue:
        #         return "U"

        #     l = get_first_half(root.left)
        #     r = get_first_half(root.right)

        #     ans = ""
        #     if l != "":
        #         ans = "U" + l
        #     if r != "":
        #         ans = "U" + r

        #     return ans

        # first_half = get_first_half(self.lca)[:-1]

        # print(first_half[:-1])

        def get_half(root, val):
            if root == None:
                return "", 0
            
            if root.val == val:
                return "", 1

            # ans = ("", 0)
            s, has_dest = "", 0
            l = get_half(root.left, val)
            r = get_half(root.right, val)

            if l[1] == 1:
                s = "L" + l[0]
                has_dest = 1
            if r[1] == 1:
                s  = "R" + r[0]
                has_dest = 1

            return s, has_dest

        first_half = get_half(self.lca, startValue)[0]
        second_half = get_half(self.lca, destValue)[0]

        # print(f"second_half: {second_half}")

        return "".join(['U']*len(first_half)) + second_half

                



            
 