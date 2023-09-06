# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#    self.next = next

# use dummy list to start
# while both list !=null
# 1. compare 2 nodes(l1, l2)
# 2. put smaller one to the tail of the new list
# 3. update smaller list's pointer and tail pointer
# if only 1 list is empty, just simply put another list to the last part of new list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
                
                
                