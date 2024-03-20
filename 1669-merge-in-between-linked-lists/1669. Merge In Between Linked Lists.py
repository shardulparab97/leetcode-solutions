# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        # adding temp just in case
        
        cnt = 0
        st, en = None, None

        while True:
            if a == cnt+1:
                st = head
            
            if b == cnt:
                en = head.next
                break
            cnt += 1
            head = head.next

        
        st.next = list2
        head2 = list2

        while head2.next != None:
            head2 = head2.next

        head2.next = en

        return list1

        
