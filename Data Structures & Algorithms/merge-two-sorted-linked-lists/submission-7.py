# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = None
        result = None
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    smaller = list1
                    list1 = list1.next
                else:
                    smaller = list2
                    list2 = list2.next
            elif list1:
                smaller = list1
                list1 = list1.next
            else:
                smaller = list2
                list2 = list2.next
            
            if result_head is None:
                result_head = smaller
                result = result_head
            else:
                result.next = smaller
                result = result.next
        return result_head