# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    #很巧妙,推导一下便可知
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if(headA == None or headB == None): return None
        pA = headA
        pB = headB
        while(pA!=pB):
            pA = pA.next if(pA) else headB
            pB = pB.next if(pB) else headA
        return pA

    #集合
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 因为,是判断两个链表是否相交
        # 所以,用先遍历一遍一个链表,存入集合中
        # 遍历第二个链表,判断是否在集合中
        # 如果
        ans = set()
        while(headA):
            ans.add(headA)
            headA = headA.next
        if(ans == None): return None
        while(headB):
            if(headB in ans):
                return headB
            headB = headB.next
        return None
