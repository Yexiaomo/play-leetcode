# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        p = l
        pl1 = l1
        pl2 = l2
        while(pl1 and pl2):
            if(pl1.val <= pl2.val):
                tmp = ListNode(pl1.val)
                pl1 = pl1.next
            else:
                tmp = ListNode(pl2.val)
                pl2 = pl2.next
            p.next = tmp
            p = p.next
        if(pl1):
            p.next = pl1
        if(pl2):
            p.next = pl2
        return l.next