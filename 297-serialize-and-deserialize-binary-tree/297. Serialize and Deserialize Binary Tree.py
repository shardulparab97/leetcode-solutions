# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        q = collections.deque()

        q.append(root)

        while q:
            curr = q.popleft()
            if curr == None:
                ans.append("null")
                continue
                # ans.append(",")
            else:
                ans.append(str(curr.val))
                # ans.append(",")
            
            # if curr.left:
            q.append(curr.left)
                # curr = curr.left
            
            # if curr.right:
            q.append(curr.right)
                # curr = curr.right

        # print(ans)
        return ','.join(ans[:-1])

            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        
        vals = data.split(",")
        n = len(vals)

        root = TreeNode(vals[0])
        

        curr = root

        q = collections.deque()
        q.append(curr)

        idx = 0
        
        while q and idx<n:
            curr = q.popleft()

            idx += 1
            if idx >= n:
                break

            if vals[idx] != "null":
                curr.left = TreeNode(vals[idx])
                q.append(curr.left)

            idx += 1
            if idx >= n:
                break
            if  vals[idx] != "null":
                curr.right = TreeNode(vals[idx])
                q.append(curr.right)

        return root
                

            


        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))