# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result, current = None, None
        carry = 0

        while l1 or l2 or carry:
            op1, op2 = 0, 0
            if l1:
                op1 = l1.val
                l1 = l1.next
            if l2:
                op2 = l2.val
                l2 = l2.next
            
            sum = op1 + op2 + carry
            carry = sum // 10
            sum = sum % 10

            new_node = ListNode(sum, None)

            if not result:
                result = new_node
                current = result
            else:
                current.next = new_node
                current = current.next
        return result

        