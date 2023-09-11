# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. split the list into 2 part : use slow, fast pointer to find middle
# 2. reverse second part of the list
# 3. merge 2 lists


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse second list
        second = slow.next
        prev = None
        slow.next = None # seperate 1st list from 2nd list
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        #merge
        first = head
        second = prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2