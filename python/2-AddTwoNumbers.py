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
        sum = l1.val + l2.val #两个数相加的和
        resultList = ListNode(sum%10) #初始化结果链表
        p = resultList #中间指针
        while(l1.next != None and l2.next != None):
            l1 = l1.next
            l2 = l2.next
            sum = l1.val + l2.val + sum//10
            temp = ListNode(sum%10)
            p.next = temp
            p = p.next
        # 当l1不为空
        while(l1.next != None):
            l1 = l1.next
            sum = l1.val + sum//10
            temp = ListNode(sum%10)
            p.next = temp
            p = p.next
		# 当l2不为空
        while(l2.next != None):
            l2 = l2.next
            sum = l2.val + sum//10
            temp = ListNode(sum%10)
            p.next = temp
            p = p.next
		#还有进位时
        if(sum//10 == 1):
            temp = ListNode(1)
            p.next = temp
            p = p.next
        return resultList