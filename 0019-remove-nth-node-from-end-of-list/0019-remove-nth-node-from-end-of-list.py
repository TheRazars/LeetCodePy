# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            tail.next = slow
            tail = tail.next
            slow = slow.next
        if slow:
            tail.next = slow.next
        return dummy.next