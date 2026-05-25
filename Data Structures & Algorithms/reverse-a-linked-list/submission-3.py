# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if prev is None:
            return None
        
        curr = prev.next

        if curr is None:
            head.next = None
            return head
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head.next = None
        return prev

        
        