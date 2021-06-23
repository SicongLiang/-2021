class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哨兵机制
        p = ListNode(0)
        curr = p

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1 is None:
            while l2 is not None:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        if l2 is None:
            while l1 is not None:
                curr.next = l1
                l1 = l1.next
                curr = curr.next

        return p.next
