# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. use fast, slow pointer to find nth node
# 2. skip target node (slow.next = slow.next.next)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = fast =slow = ListNode(0, next=head)
        
        #     s   f
        #[0,1,2,3,4]

        # move fast ahead n steps
        for i in range(n):
            fast = fast.next
        
        while fast.next:
            slow= slow.next
            fast = fast.next
        
        #skip 1 node
        slow.next = slow.next.next
        
        return dummy.next
    
