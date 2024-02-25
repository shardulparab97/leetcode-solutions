"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        self.diameter = 0
        
        
        def height(node):
            if node == None:
                return 0
            if len(node.children) == 0:
                return 0
            mh1, mh2 = 0, 0

            for c in node.children:
                ph = height(c) + 1
                if ph > mh1:
                    mh1, mh2 = ph, mh1
                elif ph > mh2:
                    mh2 = ph
            
            distance = mh1 + mh2
            self.diameter = max(self.diameter, distance)

            return mh1
        
        height(root)
        return self.diameter
