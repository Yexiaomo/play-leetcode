# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 改良版--2019/12/23
    #仔细阅读题之后，便会发现，也就是整体移动K个位置
    #首先要注意的是当前元素要移动的K个位置可能不在后面，在前面
    #移动第一个元素时，肯定会占用据后面未移动元素的位置，怎么保存未移动元素的值
    #但是本题确是链表移动，不能像数组一样
    #首先找到链表的尾结点，顺表计算一下链表的长度，判断是否对K进行处理
    #可以在纸上画一下
    # Test case： 1,2,3,4； k=6
    # 头结点是1，尾结点4，k=6>len=4,于是k=6%4=2
    # 后面需要移动到前面的节点是3,4, 
    # 拼接这两个链表即可 3,4 -> 1,2
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(not head): return None
        len_list = 0
        p = head
        while(p):
            len_list+=1
            end = p
            p = p.next
        k = k%len_list
        if(k == 0): return head
        # 此时,head指向了头结点,end指向了尾结点,k也是真正需要移动的距离
        # 再遍历一次,得到后面的k个节点
        k_node = head
        for i in range(len_list-k):
            p = k_node
            k_node = k_node.next
        #此时[k_node,end]就是需要移动前面的节点,[head, p]就是需要移动到后面的节点
        p.next = end.next
        end.next = head
        return k_node
    
    #后面的循环纯属多余
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
