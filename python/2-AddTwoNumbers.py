# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 因为是非负整数，不用考虑正负号
    # 每次注意加上进位就ok了
    # 注意判断是不是已经到头了
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0#代表进位
        l3 = ListNode(0)
        p = l3
        while(l1 and l2):
            tmp = ListNode(l1.val+l2.val+ flag)
            tmp.val, flag = tmp.val % 10, tmp.val // 10
            p.next = tmp
            p = p.next
            l1 = l1.next
            l2 = l2.next
        if(l1): p.next = l1
        if(l2): p.next = l2
        while(p.next):
            p.next.val += flag
            p.next.val, flag = p.next.val % 10, p.next.val // 10
            p = p.next
        if(flag == 1):
            p.next = ListNode(1)
        return l3.next

# 改进代码
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 进行输入值判断
        if(l1 == None or l2 == None):
            return None
        sum = l1.val + l2.val #两个数相加的和
        resultList = ListNode(sum%10) #初始化结果链表
        p = resultList #移动指针
        while(l1.next != None or l2.next != None):
            l1.val = 0
            l2.val = 0
            l1 = l1 if(l1.next==None) else l1.next
            l2 = l2 if(l2.next==None) else l2.next
            sum = l1.val + l2.val + sum//10
            temp = ListNode(sum%10)
            p.next = temp
            p = p.next
        #还有进位时
        if(sum//10 == 1):
            p.next = ListNode(1)
        return resultList
