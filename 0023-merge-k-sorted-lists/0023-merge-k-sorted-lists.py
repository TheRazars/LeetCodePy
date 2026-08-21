class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        inter = 1
        while inter < len(lists):
            for i in range(0, len(lists) - inter, inter * 2):
                lists[i] = self.merge(lists[i], lists[i + inter])
            inter *= 2
        return lists[0]
    def merge(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            dummy = ListNode()
            tail = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                    tail = tail.next
                else:
                    tail.next = list2
                    list2 = list2.next
                    tail = tail.next
            tail.next = list1 if list1 else list2
            return dummy.next