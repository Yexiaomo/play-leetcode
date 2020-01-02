# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #使用额外的空间O(N)
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        arrList = []
        while(p != None):
            arrList.append(p.val)
            p=p.next
        p = head
        for i in sorted(arrList):
            p.val = i
            p = p.next
        return head
    #归并排序
    def sortList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None): return head
        slow, fast = head, head.next
        while(fast and fast.next):
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        #找到链表中间的位置,进行递归
        left, right = self.sortList(head), self.sortList(mid)
        #当递归到最深处的时候,也就是,一对一比较
        #递归回上层的时候,两两一组,相邻的进行比较
        p = rst = ListNode(0)
        while(left and right):
            if(left.val < right.val):
                p.next, left = left, left.next
            else:
                p.next, right = right, right.next
            p = p.next
        p.next = left if(left) else right
        return rst.next
