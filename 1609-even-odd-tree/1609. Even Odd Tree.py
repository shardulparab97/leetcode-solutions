# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        level = 0
        q = collections.deque()
        q.append((root, level))
        l_nodes = []
        while q:
            sz = len(q)
            level += 1
            while sz > 0:
                sz -= 1 
                node, curr_level = q.popleft()
                l_nodes.append(node.val)
                if node.left:
                    q.append((node.left, curr_level+1))
                if node.right:
                 q.append((node.right, curr_level+1))

            if (level-1) == 0:
                if l_nodes[0] % 2 == 0:
                    return False
                l_nodes = []
                continue
            if (level-1)%2 == 1:
                n = len(l_nodes)
                if n == 1 and l_nodes[0]%2 != 0:
                    return False
                for i in range(1, n):
                    if l_nodes[i-1]%2 !=0 or l_nodes[i]%2 != 0 or l_nodes[i] >= l_nodes[i-1]:
                        return False
            else:
                n = len(l_nodes)
                if n == 1 and l_nodes[0] % 2 == 0:
                    return False
                for i in range(1, n):
                    if l_nodes[i-1]%2 ==0 or l_nodes[i]%2 == 0 or l_nodes[i] <= l_nodes[i-1]:
                        return False
            l_nodes = []
        return True

            

