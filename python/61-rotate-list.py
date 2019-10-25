# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head == None or head.next == None or k<=0): return head
        p = end_p = head
        len_l = 1
        #遍历得到链表的长度
        while(True):
            if(p.next):
                p = p.next
                len_l += 1
            else:
                break
        #如果k超过链表长度,进行处理
        if(k>=len_l):
            k = k%len_l
            if(k==0): return head
        #p指向第一个要移动的元素,也是结束的标志
        p = end_p
        tmp_queue = []
        for i in range(k):
            tmp_queue.append(p.val)
            end_p = p
            p = p.next if(p.next) else head
        #开始循环
        while(True):
            tmp_queue.append(p.val)
            p.val = tmp_queue.pop(0)
            p = p.next if(p.next) else head
            if(p == end_p.next): break
        return head