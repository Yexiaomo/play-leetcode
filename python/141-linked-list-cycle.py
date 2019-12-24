# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #快慢指针
    def hasCycle(self, head: ListNode) -> bool:
        if(head == None or head.next == None): return False
        slow = head
        fast = head.next
        while(fast != slow):
            if(fast == None or fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    #集合判定
    def hasCycle(self, head: ListNode) -> bool:
        ans = set()
        while(head!=None):
            if(head in ans):
                return True
            else:
                ans.add(head)
                head = head.next
        return False

    # 看了知识点，标签是双指针，但这又是链表，所以这个双指针就应该是快慢指针
    # 又因为判断是否有环，所以如果存在环，那么两个指针一定会遇见
    # 但是，如果没有环，怎么判断呢。。。显然，快指针指向的元素不能为空
    # OK，主要就是双指针移动
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        flag = 0
        while(fast):
            fast = fast.next
            if(fast == slow):
                return True
            flag += 1
            if(flag == 2):
                flag = 0
                slow = slow.next
        return False
