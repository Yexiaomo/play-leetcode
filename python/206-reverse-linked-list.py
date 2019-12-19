# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #分析一波就是头插法创建单链表
        p = new = ListNode(0)
        while(head):
            p = head
            head = head.next
            p.next = new.next
            new.next = p
        return new.next
