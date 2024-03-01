"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.vis = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        
        if node in self.vis:
            return self.vis[node]
        
        clone_node = Node(node.val, [])
        self.vis[node] = clone_node

        if node.neighbors:
                clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node