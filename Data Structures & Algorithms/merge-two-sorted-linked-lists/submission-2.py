# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result, last = None, None

        while list1 or list2:
            if list1 and list2:
                smaller = None
                if list1.val < list2.val:
                    smaller = list1
                    list1 = list1.next
                else:
                    smaller = list2
                    list2 = list2.next
                if not result:
                    result = smaller
                    last = result
                else:
                    last.next = smaller
                    last = last.next
            else:
                rem = None
                if list1:
                    rem = list1
                else:
                    rem = list2
                if not result:
                    result = rem
                else:
                    last.next = rem
                break
        return result

        