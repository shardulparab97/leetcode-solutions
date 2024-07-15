# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        treeDict = {}
        has_parents = set()
         # find root - no parents
        for p, c, isLeft in descriptions:
            if p not in treeDict:
                node = TreeNode(val = p)
                treeDict[p] = node
            else:
                node = treeDict[p]

            if c not in treeDict:
                childNode = TreeNode(val = c)
                treeDict[c] = childNode
            else:
                childNode = treeDict[c]
            
            if isLeft:
                node.left = childNode
            else:
                node.right = childNode
            
            has_parents.add(c)

        rootVal = [p for p,_,_ in descriptions if p not in has_parents][0]
        # print(rootVal)
        return treeDict[rootVal]



        