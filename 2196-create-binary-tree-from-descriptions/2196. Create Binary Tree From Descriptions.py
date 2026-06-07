# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        treeDict = {}
        hasparents = set()

        for p, c, d in descriptions:
            if p not in treeDict:
                newNode = TreeNode(val = p)
                treeDict[p] = newNode
            else: 
                newNode = treeDict[p]

            if c not in treeDict:
                childNode = TreeNode(val=c)
                treeDict[c] = childNode
            else:
                childNode = treeDict[c]
            
            if d == 1:
                newNode.left = childNode
            else:
                newNode.right = childNode

            hasparents.add(c)
        
        rootval = [p for p,_,_ in descriptions if p not in hasparents][0]

        return treeDict[rootval]
