# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # zc = 0
        dummy = ListNode(val=-1)
        dummy.next = head

        ptr = head
        curr_sum = 0 
        # z1_ptr, z2_ptr = None, None
        prev_z1_ptr, next_z2_ptr = None, None
        prev_ptr = dummy


        while ptr!=None:
            if ptr.val == 0:
                if prev_z1_ptr == None: # shows if this is the first zero
                    prev_z1_ptr = prev_ptr
                else: # check for none option
                    next_z2_ptr = ptr.next
                    # calc sum 
                    temp_node = ListNode(curr_sum)
                    prev_z1_ptr.next = temp_node
                    temp_node.next = next_z2_ptr
                    prev_z1_ptr, next_z2_ptr = temp_node, None
                    curr_sum = 0
            else:
                if prev_z1_ptr != None:
                    curr_sum += ptr.val

            prev_ptr = ptr
            ptr = ptr.next
           

        return dummy.next