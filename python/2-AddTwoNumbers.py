# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 进行输入值判断
        if(l1 == None or l2 == None):
            return None
        sum = l1.val + l2.val
        resultList = ListNode(sum%10)
        p = resultList
        while(l1.next != None and l2.next != None):
            l1 = l1.next
            l2 = l2.next
            sum = l1.val + l2.val + sum//10
            temp = ListNode(sum%10)
            p.next = temp
            p = p.next
        while(l1.next != None):
            l1 = l1.next
            sum = l1.val + sum//10
            temp = ListNode(sum%10)
            p.next = temp
            p = p.next

        while(l2.next != None):
            l2 = l2.next
            sum = l2.val + sum//10
            temp = ListNode(sum%10)
            p.next = temp
            p = p.next

        if(sum//10 == 1):
            temp = ListNode(1)
            p.next = temp
            p = p.next
        return resultList