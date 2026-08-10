# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        tail = d
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        while s:
            tail.next = s
            tail = tail.next
            s = s.next
        return d.next