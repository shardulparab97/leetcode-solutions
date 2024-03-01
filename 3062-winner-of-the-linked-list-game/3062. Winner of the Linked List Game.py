# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        # only loop till pair is there 
        node = head
        oc, ec = 0, 0
        while node and node.next:
            if node.val > node.next.val:
                ec += 1
            else:
                oc += 1
            node = node.next.next
        
        if oc > ec:
            return "Odd"
        elif oc < ec:
            return "Even"
        else:
            return "Tie"
            
