# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        result_head = None
        result = None

        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    smaller = curr1
                    curr1 = curr1.next
                else:
                    smaller = curr2
                    curr2 = curr2.next
            
            elif curr1:
                smaller = curr1
                curr1 = curr1.next
            
            elif curr2:
                smaller = curr2
                curr2 = curr2.next

            if result_head is None:
                result_head = smaller
                result = result_head
                result.next = None
            else:
                result.next = smaller
                result = result.next
        return result_head